# This is a sample Python script.
import time
from model import model
import cv2
import serial

#
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data
import cv2 as cv

'''
def testDevice(source):
    cap = cv.VideoCapture(source,cv2.CAP_DSHOW)
    print('Initializing cam')
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
    else:
        print('Yeah')
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    testDevice(0)  # no printout
    testDevice(1)  # prints message
'''

if __name__ == '__main__':
    myProject = model()
    print('Model ready')

    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
    arduino.close()
    arduino.open()
    print('Connected to arduino')
    k = 1

    cam = cv2.VideoCapture(0)
    print('Camera opened')
    while True:
        while arduino.in_waiting == 0:
            pass
        while arduino.in_waiting:
            print('Reading from arduino')
            data = arduino.readline()
            arduino.flush()
            int_value = int(data.decode('utf-8'))
            print(int_value)
            time.sleep(1)
            if int_value == 1:
                print('Capturing')
                s, img = cam.read()
                print('Captured')
                if s:
                    filename = "C:\\Users\\Pannavich Setawanna\\PycharmProjects\\ArduinoProject2\\img\\image" + str(
                        k) + ".jpg"
                    print('Saved')
                    k += 1
                    cv2.imwrite(filename, img)
                    result = myProject.prediction(filename)
                    label = result["class_name"]
                    print("Detect " + str(label))
                    if label == "plastic":
                        arduino.write(bytes('2', 'utf-8'))
                        print('Send 2 to arduino')
                        time.sleep(8)
                        while arduino.in_waiting == 0:
                            pass
                        msg = arduino.readline()
                        arduino.flush()
                        msg = int(msg.decode('utf-8'))
                        print('Received ' + str(msg) + ' from arduino')
                        if msg == 5:
                            print("Done")
                            continue

                    elif label == "paper":
                        arduino.write(bytes('3', 'utf-8'))
                        print('Send 3 to arduino')
                        time.sleep(8)
                        while arduino.in_waiting == 0:
                            pass
                        msg = arduino.readline()
                        arduino.flush()
                        msg = int(msg.decode('utf-8'))
                        print('Received ' + str(msg) + ' from arduino')
                        if msg == 5:
                            print("Done")
                            continue

                    else:
                        arduino.write(bytes('4', 'utf-8'))
                        print('Send 4 to arduino')
                        time.sleep(8)
                        while arduino.in_waiting == 0:
                            pass
                        msg = arduino.readline()
                        arduino.flush()
                        msg = int(msg.decode('utf-8'))
                        print('Received ' + str(msg) + ' from arduino')
                        if msg == 5:
                            print("Done")
                            continue
            else:

                continue


