import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *

distances = []
#pressure = []
arduinoData = serial.Serial('COM5',
                            9600)  # Creating our serial object named
# arduinoData
plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0


def makeFig():  # Create a function that makes our desired plot
    plt.ylim(00, 1000)  # Set y min and max values
    plt.title('My Live Streaming Sensor Data')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('Distance CM')  # Set ylabels
    plt.plot(distances, 'ro-', label='Distance CM')  # plot the temperature
    plt.legend(loc='upper left')  # plot the legend
    #plt2 = plt.twinx()  # Create a second y axis
    plt.ylim(0,
             1000)  # Set limits of second y axis- adjust to readings you
    # are getting
#    plt2.plot(pressure, 'b^-', label='Pressure (Pa)')  # plot pressure data
#    plt2.set_ylabel('Pressrue (Pa)')  # label second y axis
    #plt2.ticklabel_format(
    #    useOffset=False)  # Force matplotlib to NOT autoscale y axis
    #plt2.legend(loc='upper right')  # plot the legend


if __name__ == "__main__":

    while True:  # While loop that loops forever
        while (arduinoData.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        arduinoString = str(arduinoData.readline(), 'utf-8')  # read the line of text
        # from
        #  the serial port
        dataArray = arduinoString.split('\n')  # Split it into an array called dataArray
        distance = float(dataArray[0])  # Convert first element to floating number and
        #  put in temp
        #P = float(dataArray[1])  # Convert second element to floating
        # number and
        # put in P
        distances.append(distance)  # Build our tempF array by appending temp readings
        #pressure.append(P)  # Building our pressure array by appending P
        # readings
        drawnow(makeFig)  # Call drawnow to update our live graph
        plt.pause(.000001)  # Pause Briefly. Important to keep drawnow from crashing
        cnt = cnt + 1
        if (cnt > 50):  # If you have 50 or more points, delete the first
            # one from the array
            distances.pop(0)  # This allows us to just see the last 50 data points