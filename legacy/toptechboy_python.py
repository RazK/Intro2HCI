import numpy as np
import serial  # Import Serial Library
from drawnow import *

from legacy.plot_arduino import f_spectrum, show_easy

# arduinoSerialData
SAMPLE_LENGTH = 50
SLICE_SIZE = 7
ZEROS_WIDTH = 3

SAMPLE_SHARP = "sample_sharp50.sig"
SAMPLE_SOFT = "sample_soft50.sig"
SAMPLE_WHITE = "sample_white50.sig"

GEST_SHARP = np.fromfile(SAMPLE_SHARP)
SPEC_SHARP = f_spectrum(GEST_SHARP)
GEST_SOFT = np.fromfile(SAMPLE_SOFT)
SPEC_SOFT = f_spectrum(GEST_SOFT)
GEST_NONE = np.fromfile(SAMPLE_WHITE)
SPEC_NONE = f_spectrum(GEST_NONE)

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

SHARP=OKBLUE+"HORIZONTAL"+ENDC
SOFT=OKGREEN+"VERTICAL"+ENDC
NONE=FAIL+"NONE"+ENDC



def makeFig(distances):  # Create a function that makes our desired plot
    plt.ylim(0, 200)  # Set y min and max values
    plt.title('My Live Streaming Sensor Data')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('Distance CM')  # Set ylabels
    plt.plot(distances, 'ro-', label='Distance CM')  # plot the temperature
    plt.legend(loc='upper left')  # plot the legend
    #plt2 = plt.twinx()  # Create a second y axis
    plt.ylim(0,
             200)  # Set limits of second y axis- adjust to readings you
    # are getting
#    plt2.plot(pressure, 'b^-', label='Pressure (Pa)')  # plot pressure data
#    plt2.set_ylabel('Pressrue (Pa)')  # label second y axis
    #plt2.ticklabel_format(
    #    useOffset=False)  # Force matplotlib to NOT autoscale y axis
    #plt2.legend(loc='upper right')  # plot the legend


def record_cyber(filename):
    distances = np.zeros(SAMPLE_LENGTH)
    samples = 0
    with serial.Serial('COM5',9600) as arduinoSerialData: # Create Serial
        # port object called
        while (1 == 1):
            if (arduinoSerialData.inWaiting() > 0):
                samples += 1
                myData = arduinoSerialData.readline()
                print(myData)
                distances = np.roll(distances, 1)
                distances[0] = myData
                # print(distances[10])
                # spec = f_spectrum(fourier, True)
                # show_dual_plot(np.tile(blurred, (100, 1)), np.tile(spec,
                # (100,
                # 1)))
                if samples > SAMPLE_LENGTH:
                    break
    fourier = np.fft.fft(distances)
    fourier.tofile(filename)
    distances.tofile("{}.im".format(filename))
    return fourier

def display_cyber(file1, file2, file3, shift = False):
    gest1 = np.fromfile(file1)
    spec1 = f_spectrum(gest1, shift)
    gest2 = np.fromfile(file2)
    spec2 = f_spectrum(gest2, shift)
    no_gest = np.fromfile(file3)
    spec3 = f_spectrum(no_gest, shift)
    show_easy(spec1, spec2, spec3)

def SSD(sliceSize, spec, ref):
    return np.sum((spec[:sliceSize]-ref[:sliceSize])**2)

def findGest(spec):
    sharp = 1.1*SSD(SLICE_SIZE, spec, SPEC_SHARP)
    soft = SSD(SLICE_SIZE, spec, SPEC_SOFT)
    none = 0.92*SSD(SLICE_SIZE, spec, SPEC_NONE)
    gest = {sharp:SHARP, soft:SOFT, none:NONE}
    return gest[min(gest)]

# if True:
#     input("white SAMPLE:")
#     white = record_cyber(SAMPLE_WHITE)
#     print(white)
    # input("SOFT SAMPLE:")
    # soft = record_cyber(SAMPLE_SOFT)
    # print(soft)
#display_cyber(SAMPLE_SHARP, SAMPLE_SOFT, SAMPLE_WHITE, True)
#display_cyber(SAMPLE_SHARP+".im", SAMPLE_SOFT+".im", SAMPLE_WHITE+".im")
def demo():
    distances = np.zeros(SAMPLE_LENGTH)
    lastones = np.zeros(15).astype(str)
    samples = 0
    last_gest = GEST_NONE
    with serial.Serial('COM5',9600) as arduinoSerialData: # Create Serial
        # port object called
        while (1 == 1):
            if (arduinoSerialData.inWaiting() > 0):
                myData = arduinoSerialData.readline()
                #print(myData)
                try:
                    distances = np.roll(distances, 1)
                    distances[0] = myData
                except:
                    distances = np.roll(distances, -1)

                    # print(distances[10])
                # spec = f_spectrum(fourier, True)
                # show_dual_plot(np.tile(blurred, (100, 1)), np.tile(spec,
                # (100,
                # 1)))
            #drawnow(makeFig, distances=distances)  # Call drawnow to update
            #plt.pause(.01)  # Pause Briefly. Important to keep drawnow from
            # crashing
            # our live graph
            fourier = np.fft.fft(distances)
            spec = f_spectrum(fourier)
            gest = findGest(spec)
            #if (gest != last_gest):
            lastones = np.roll(lastones, 1)
            lastones[0] = gest
            all_sharp = lastones == SHARP
            all_soft = lastones == SOFT
            all_none = lastones == NONE
            if(all_sharp.all() or all_soft.all() or all_none.all()):
                print("\r"+gest)
            else:
                pass#print("...")

demo()
