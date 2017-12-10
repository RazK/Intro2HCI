import serial

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

ser = serial.Serial(device, DEFAULT_BAUD_RATE)
while True:
    print(str(ser.readline()))
