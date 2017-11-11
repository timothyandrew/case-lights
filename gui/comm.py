import serial
import time

#####################################################################################
# Protocol Notes                                                                    #
# --------------                                                                    #
#                                                                                   #
# - All communication happens one byte at a time                                    #
# - The `protocol` on the Python side is the canonical list of what each byte means #
# - Every message sent from Python to Arduino is ACKed                              #
#####################################################################################

def waitForArduinoReady(conn):
    message = conn.read()
    if message != '' and message[0] == getProtocolCode('arduinoReady'):
        pass
    else:
        print("Debug: Didn't get ready signal from Arduino. Already ready?")

protocol = {
    'arduinoReady': chr(1),
    'ACK': chr(2),

    # Lighting styles
    'pulse': chr(10),
    'rgb': chr(11),
    'white': chr(12),

    # Actions
    'pause': chr(30),
    'clear': chr(31)
}

def getProtocolCode(code):
    return protocol[code]

def sendToArduino(conn, operation):
    conn.write(getProtocolCode(operation))
    response = conn.read()
    if not response == getProtocolCode("ACK"):
        raise ValueError("Arduino didn't ACK the request")

def setup():
    conn = serial.Serial('COM1', 9600, timeout=1, write_timeout=1)
    waitForArduinoReady(conn)
    return conn

