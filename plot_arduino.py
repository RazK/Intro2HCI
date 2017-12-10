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

DELIMITER = ';'

signal_size = 10
frames = 10

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #

device = HOST2DEV[HOST]

with serial.Serial(device, DEFAULT_BAUD_RATE) as ser:
    while True:
        # signal = np.array([str(ser.readline()).split("\\r;")[0].split(
        #     "b'")[1] for _ in range(signal_size * frames)]).astype(np.float64)



        # plt.plot(signal)
        plt.imshow(signal.reshape(frames, signal_size))
        plt.show()

