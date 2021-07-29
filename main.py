import time
from model import model
import cv2
import serial
import cv2 as cv
from datetime import datetime

def readMessageFromArduino(arduino):
    print('Reading from arduino')
    data = arduino.readline()
    arduino.flush()
    int_value = int(data.decode('utf-8'))
    return int_value


def sendMessageToArduino(arduino, message):
    arduino.write(bytes(message, 'utf-8'))
    print(f'Send {message} to arduino')
    time.sleep(8)
    while arduino.in_waiting == 0:
        pass
    msg = arduino.readline()
    arduino.flush()
    msg = int(msg.decode('utf-8'))
    print(f'Received {msg} from arduino')
    if msg == 5:
        print("Done")

if __name__ == '__main__':
    #import model from model.py
    myModel = model()
    print('Model ready')

    #open serial port for connecting with arduino
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
    arduino.close()
    arduino.open()
    print('Connected to arduino')

    #initiate camera via cv2
    cam = cv2.VideoCapture(0)
    print('Camera opened')

    while True:
        while arduino.in_waiting == 0:
            pass
        while arduino.in_waiting:
            int_value = readMessageFromArduino(arduino)
            time.sleep(1)
            if int_value == 1:
                print('Capturing')
                s, img = cam.read()
                print('Captured')
                if s:
                    now = datetime.now()
                    timestamp = now.strftime("%d-%m-%Y-%H:%M:%S")
                    #path you want to save image
                    filename = "C:\\Users\\Pannavich Setawanna\\PycharmProjects\\ArduinoProject2\\img\\image" + timestamp + ".jpg"
                    cv2.imwrite(filename, img)
                    print('Saved')
                    result = myModel.prediction(filename)
                    label = result["class_name"]
                    print("Detect " + str(label))
                    if label == "plastic":
                        sendMessageToArduino(arduino,'2')
                        continue

                    elif label == "paper":
                        sendMessageToArduino(arduino,'3')
                        continue

                    #metal
                    else:
                        sendMessageToArduino(arduino,'4')
                        continue
            else:
                continue



                            
