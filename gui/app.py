import serial

arduino = serial.Serial('COM4', 9600)
arduino.write(b'nextColor')
