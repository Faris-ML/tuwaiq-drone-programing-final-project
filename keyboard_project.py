from djitellopy import tello
from pynput.keyboard import Key, Listener
from time import sleep
import cv2
import cvzone
from cvzone.PoseModule import PoseDetector


detector = PoseDetector()

# kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

def getKeyboardInput(key):
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30
    if key==Key.left :
        lr = -speed
    elif key==Key.right:
        lr = speed
    if key==Key.up:
        fb = speed
    elif key==Key.down:
        fb = -speed
    if str(key)=="'w'":
       ud = speed
    elif str(key)=="'s'":
        ud = -speed
    if str(key)=="'a'":
       yv = -speed
    elif str(key)=="'d' ":
        yv = speed
    if str(key)=="'q'":
        me.land()
        sleep(3)
    if str(key)=="'e'":
        me.takeoff()
    vals = [lr, fb, ud, yv]
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])   


while True:
    
    img = me.get_frame_read().frame
    img = cv2.resize(img, (320, 250))
    img = detector.findPose(img)
    bboxs,_= detector.findPosition(img, draw=True)
  

    
    count = len(bboxs)

    img = cv2.putText(
    img = img,
    text = str(count),
    org = (200, 200),
    fontFace = cv2.FONT_HERSHEY_DUPLEX,
    fontScale = 3.0,
    color = (125, 246, 55),
    thickness = 3
     )    
    
    with Listener(on_press=getKeyboardInput) as listener:
        listener.join()
    cv2.imshow("image", img)
    vals = getKeyboardInput()
    
    # sleep(0.5)









# KeyPressModule

import pygame



def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    print('K_{}'.format(keyName))

    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey("LEFT"):
        print("Left key pressed")

    if getKey("RIGHT"):
        print("Right key Pressed")


if __name__ == "__main__":
    init()
    while True:
        main()