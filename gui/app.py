import serial

arduino = serial.Serial('COM4', 9600)

while true:
    try:
        print(arduino.readline())
        time.sleep(1)
    except arduino.SerialTimeoutException:
        print("ERROR: Data could not be read")
        time.sleep(1)
