import keyboard as key
from time import sleep
from djitellopy import Tello
import cv2
from cvzone.FaceDetectionModule import FaceDetector

drone = Tello()
drone.connect()
print(drone.get_battery())
drone.streamoff()
drone.streamon()

detector = FaceDetector()


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if key.is_pressed('LEFT'): lr =  -speed
    elif key.is_pressed('RIGHT'): lr = speed

    if key.is_pressed('UP'): fb = -speed
    elif key.is_pressed('DOWN'): ud = speed

    if key.is_pressed('w'): fb = speed
    elif key.is_pressed('s'): fb = -speed

    if key.is_pressed('a'): yv = speed
    elif key.is_pressed('d'): yv = -speed

    if key.is_pressed('a'): drone.move_up(30)
    if key.is_pressed("s"): drone.move_forward(25)
    if key.is_pressed("d"): drone.rotate_clockwise(360)
    if key.is_pressed("f"): drone.rotate_counter_clockwise(90)
    if key.is_pressed("g"): drone.move_back(21)
    if key.is_pressed('h'): drone.takeoff(21)
    if key.is_pressed('j'): drone.move_right(25)
    if key.is_pressed('k'): drone.move_left(25)
    if key.is_pressed('l'): drone.move_down(21)

    if key.is_pressed('z'): 
        drone.land()
        drone.streamoff()  

    if key.is_pressed('x'): 
        drone.take_picture() 

    return [lr, fb, ud, yv]

drone.takeoff()

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    img = drone.get_frame_read().frame
    img = cv2.resize(img, (520,360))
    img, bboxs = detector.findFaces(img, draw=True)
    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()