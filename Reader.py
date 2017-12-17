"""

"""

# ENVIRONMENT
SHIMMY = "SHIMMY"
RAZ = "RAZ"
HOSTS = {RAZ, SHIMMY}
HOST2DEV = {SHIMMY : "/dev/tty.wchusbserial1420",
            RAZ : "NO DEVICE"}
DEFAULT_BAUD_RATE = 9600


signal_size = 250
frames = 1

MAX_DIST = 50

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #
device = HOST2DEV[HOST]

# guassian = g_kernel(7, one_d=True)
# signal = np.zeros((signal_size, frames))


class Reader():

    def __init__(self):
        pass