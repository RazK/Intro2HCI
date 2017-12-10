import serial
import numpy as np
import matplotlib.pyplot as plt

# ENVIRONMENT
SHIMMY = "SHIMMY"
RAZ = "RAZ"
HOSTS = {RAZ, SHIMMY}
HOST2DEV = {SHIMMY : "/dev/tty.wchusbserial1420",
            RAZ : "NO DEVICE"}
DEFAULT_BAUD_RATE = 9600

signal_size = 100

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #

device = HOST2DEV[HOST]

with serial.Serial(device, DEFAULT_BAUD_RATE) as ser:
    while True:
        signal = np.array([str(ser.readline()).split("\\r\\n")[0].split(
            "b'")[1] for _ in range(signal_size)]).astype(np.float64)

        plt.plot(signal)
        plt.imshow(signal.reshape(1, signal_size))
        plt.show()


