"""

"""

# ENVIRONMENT
SHIMMY = "SHIMMY"
RAZ = "RAZ"
HOSTS = {RAZ, SHIMMY}
HOST2DEV = {SHIMMY : "/dev/tty.wchusbserial1420",
            RAZ : "NO DEVICE"}
DEFAULT_BAUD_RATE = 9600


# signal_size = 250
# frames = 1
#
# MAX_DIST = 50

# CURRENT HOST #
# ============ #
HOST = SHIMMY  #
# ============ #
device = HOST2DEV[HOST]

# guassian = g_kernel(7, one_d=True)
# signal = np.zeros((signal_size, frames))

SENSORS = 12
FRAME_WIDTH = 32


class Reader():

    def __init__(self):
        pass

    def open_seriel(self):
        """
        opens communication with arudino port
        :return:
        """
        pass

    def close_seriel(self):
        pass

    def read_frame(self):
        """
        Returns a single reading from all the sonsors, reduced to one frame.
        :return:
        """
        pass
