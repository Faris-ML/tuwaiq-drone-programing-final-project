from djitellopy import tello
import cvzone
import cv2
import keyboard as key
from time import sleep
   

myColorFinder = cvzone.ColorFinder()

drone = tello.Tello()


drone.connect()
print(drone.get_battery())
drone.streamon()




hsvVals = {'hmin': 107, 'smin': 145, 'vmin': 99, 'hmax': 129, 'smax': 255, 'vmax': 255}


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
     if key.is_pressed('t'): drone.takeoff()

     if key.is_pressed("a"):drone.move_forward(21)
     if key.is_pressed("w"):drone.move_up(40)
     if key.is_pressed("d"):drone.move_back(21)
     if key.is_pressed("s"):drone.rotate_counter_clockwise(45)


     if key.is_pressed('q'): drone.land()

     return [lr, fb, ud, yv]

drone.takeoff()

s = 0


while True:
 
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(256,256))
    imgOrange, mask = myColorFinder.update(img, hsvVals)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgOrange = cv2.cvtColor(imgOrange,cv2.COLOR_BGR2RGB)

    imgStack = cvzone.stackImages([img, imgOrange, mask], 3, 1)

    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    
    
    cv2.imshow("Image Stack", imgStack)
   
    cv2.waitKey(5)
