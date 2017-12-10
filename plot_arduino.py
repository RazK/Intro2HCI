import serial
import numpy as np

# ENVIRONMENT
SHIMMY = "SHIMMY"
RAZ = "RAZ"
HOSTS = {RAZ, SHIMMY}
HOST2DEV = {SHIMMY : "/dev/tty.wchusbserial1420",
            RAZ : "NO DEVICE"}
DEFAULT_BAUD_RATE = 9600

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #

device = HOST2DEV[HOST]

with serial.Serial(device, DEFAULT_BAUD_RATE) as ser:
    while True:
        signal = np.array(ser.read_until(ser))
        print(ser.readline())
