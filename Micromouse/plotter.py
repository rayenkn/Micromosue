import serial
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np
import struct
import time

# --- Config ---
PORT   = 'COM3'
BAUD   = 115200
DT       = 0.020         # firmware TELEMETRY_PERIOD = 20 ms (used only for initial view sizing)
INIT_WIN = 20.0           # seconds shown in the view before it starts growing
SANITY   = 500.0          # reject implausible floats (resync guard)

ser = serial.Serial(PORT, BAUD, timeout=0.01)

HEADERS = {
    0xAA: 'target_r',
    0xAB: 'speed_r',
    0xAC: 'target_l',
    0xAD: 'speed_l',
}

# Full-history buffers: nothing ever gets dropped, they just keep growing
t_buf = {name: [] for name in HEADERS.values()}
v_buf = {name: [] for name in HEADERS.values()}

t0 = time.monotonic()  # reference so timestamps start near 0

win = pg.GraphicsLayoutWidget(show=True, title="Trapezoidal profile + PID telemetry", size=(1850, 1000))
win.setGeometry(0, 29, 1800, 840)

p1 = win.addPlot(title="Target (trapezoid) vs measured wheel speed [cm/s]")
p1.addLegend()

c_target_r = p1.plot(pen=pg.mkPen('c', width=2), name="Target R (0xAA)  <- trapezoid", connect="finite")
c_target_l = p1.plot(pen=pg.mkPen('m', width=2), name="Target L (0xAC)  <- trapezoid", connect="finite")
c_speed_r  = p1.plot(pen=pg.mkPen('w', width=1), name="Speed R  (0xAB)", connect="finite")
c_speed_l  = p1.plot(pen=pg.mkPen('y', width=1), name="Speed L  (0xAD)", connect="finite")

p1.setYRange(-25, 25)
p1.showGrid(x=True, y=True)
p1.setLabel('bottom', 'time', units='s')
p1.setXRange(0, INIT_WIN)

buf = bytearray()

def update():
    try:
        buf.extend(ser.read(ser.in_waiting or 1))

        now = time.monotonic() - t0

        while len(buf) >= 5:
            h = buf[0]
            if h not in HEADERS:
                del buf[0]                      # noise, resync
                continue
            value = struct.unpack('<f', bytes(buf[1:5]))[0]
            if not np.isfinite(value) or abs(value) > SANITY:
                del buf[0]                      # was a payload byte, resync
                continue

            name = HEADERS[h]
            t_buf[name].append(now)
            v_buf[name].append(value)

            del buf[0:5]

        c_target_r.setData(t_buf['target_r'], v_buf['target_r'])
        c_target_l.setData(t_buf['target_l'], v_buf['target_l'])
        c_speed_r.setData(t_buf['speed_r'], v_buf['speed_r'])
        c_speed_l.setData(t_buf['speed_l'], v_buf['speed_l'])

        # Grow the view to fit everything seen so far - nothing ever scrolls
        # off or gets overwritten, the plot just keeps extending to the right.
        p1.setXRange(0.0, max(now, INIT_WIN), padding=0)

    except Exception as e:
        print("Error reading serial:", e)
        buf.clear()
        ser.reset_input_buffer()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20)

if __name__ == '__main__':
    pg.exec()