"""

"""
import serial
import numpy as np

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
# HOST = SHIMMY  #
HOST = RAZ     #
# ============ #


SENSORS = 12
FRAME_WIDTH = 32


class Reader:

    def __init__(self):
        self.device = HOST2DEV[HOST]

        self.serial = serial.Serial(self.device, DEFAULT_BAUD_RATE)

    def open_serial(self):
        """
        opens communication with arudino port
        :return:
        """

        self.serial.open()

    def close_serial(self):
        self.serial.close()

    def read_frame(self):
        """
        Returns a single reading from all the sonsors, reduced to one frame.
        :return:
        """
        while (self.serial.inWaiting() <= 0):
            pass

        data = self.serial.readline()
        distances = np.array(data)
        #todo: may need to decode the data using utf-8


        return distances
            # distance = float(str(data, "utf-8"))

            # distances = np.roll(distances, 1)
