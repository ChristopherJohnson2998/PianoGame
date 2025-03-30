import serial
from pynput.keyboard import Controller

# Initialize serial port
ser = serial.Serial('COM6', 9600, timeout=1)

# Initialize keyboard controller
keyboard = Controller()

try:
    while True:
        data = ser.readline().decode('utf-8').strip()  # Read serial data, decode, and remove whitespace
        if data == "1":  # If "1" is received
            keyboard.press('k')
            keyboard.release('k')  # Simulate pressing and releasing 'K'
            print("Pressed K")  # Debug message
except KeyboardInterrupt:
    print("\nExiting...")
    ser.close()  # Close the serial port on exit
