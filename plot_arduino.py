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
        # signal = np.array([ser.readline())])
        b_bytes = ser.readline()
        print(b_bytes)
        s = str(b_bytes, 'utf-8')
        print(s)


        plt.plot(s)
        # plt.imshow(signal.reshape(frames, signal_size))
        # plt.show()


