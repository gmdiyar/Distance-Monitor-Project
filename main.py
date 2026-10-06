import re
import serial
import numpy as np
import sounddevice as sd

PORT = "/dev/ttyUSB0"
BAUD = 9600

MIN_DIST, MAX_DIST = 30, 600
MIN_FREQ, MAX_FREQ = 200, 2000
SAMPLE_RATE = 44100

ser = serial.Serial(PORT, BAUD, timeout=0.1)

freq = MIN_FREQ
cur_freq = MIN_FREQ
volume = 0.0
phase = 0.0

def callback(outdata, frames, time, status):
    global phase, cur_freq
    f = np.linspace(cur_freq, freq, frames)
    cur_freq = freq
    phases = phase + np.cumsum(2 * np.pi * f / SAMPLE_RATE)
    phase = phases[-1] % (2 * np.pi)
    outdata[:, 0] = volume * np.sin(phases)

with sd.OutputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback):
    print("Running. Ctrl+C to stop.")
    try:
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            m = re.search(r"\d+", line)
            if not m:
                continue
            mm = int(m.group())

            if mm > 2000:  
                volume = 0.0
                continue

            mm = max(MIN_DIST, min(MAX_DIST, mm))
            t = (mm - MIN_DIST) / (MAX_DIST - MIN_DIST)
            freq = MIN_FREQ + t * (MAX_FREQ - MIN_FREQ)
            volume = 0.3
    except KeyboardInterrupt:
        pass