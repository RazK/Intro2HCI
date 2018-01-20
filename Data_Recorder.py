"""
Module saves data to file
"""
import os
import numpy as np
import time

from Reader import *

from time import gmtime, strftime






DATA_DIR = "recorded_data"

DATA_SHAPE = (SENSORS, FRAME_WIDTH) # data shape for 12 sensors,
# into 32
# reading
# segments
# in time

GESTURE_DIRS = ["approaching", "full_circle", "noise", "running",
                "uncatagorized"]

class Data_Recorder:

    def __init__(self):
        self.reader = Reader()

    def record_data(self, dest_dir, frames):
        """
        Record arduino data and save to file
        :param dir:
        :param frames: duration of recording time in frames
        :return:
        """
        path = os.path.join(DATA_DIR, dest_dir, strftime("%Y-%m-%d %H:%M:%S", gmtime()))


        data = np.zeros(shape=DATA_SHAPE + (frames,))

        self.reader.open_seriel()



        self.reader.close_seriel()





