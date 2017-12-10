import serial
device = "/dev/tty.wchusbserial1420"
ser = serial.Serial(device, 9600)
while True:
    print(str(ser.readline()))
