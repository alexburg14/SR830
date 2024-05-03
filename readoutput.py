import serial

# define a function that sends an ASCII Command using RS232
def send_command(port,command):
    # open the serial port
    ser = serial.Serial(port, 9600)
    # send the command
    ser.write(b"OUTX 0")
    ser.write(command)
    ser.read(1000)
    # close the serial port
    ser.close()
# define a function that reads the output of the device
send_command("COM2","OUTP ? 1")
