from djitellopy import tello
from ultralytics import YOLO
from PIL import Image
import cv2

import keyboard as key


# Load a pretrained YOLOv8n model


drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()



model = YOLO('yolov8n.pt')
cam = cv2.VideoCapture(0)

hi, wi, = 480, 640 
# Run inference on 'bus.jpg' with arguments
"""""
xPID = cvzone.PID([0.22, 0, 0.1], wi // 2)
yPID = cvzone.PID([0.27, 0, 0.1], hi // 2, axis=1)
zPID = cvzone.PID([0.00016, 0, 0.000011], 150000, limit=[-20, 15])

myPlotX = cvzone.LivePlot(yLimit=[-100, 100], char='X')
myPlotY = cvzone.LivePlot(yLimit=[-100, 100], char='Y')
myPlotZ = cvzone.LivePlot(yLimit=[-100, 100], char='Z')

while True:
    img = drone.get_frame_read().frame
    results = model.predict(img, imgsz=320)
    im_array = results[0].plot()  # plot a BGR numpy array of predictions
    bboxs = results[0].boxes
    xVal = 0
    yVal = 0
    zVal = 0
    print(bboxs)

    if bboxs:
    
        cx, cy = bboxs.orig_shape[0]/2,bboxs.orig_shape[1]/2
        x, y, w, h = bboxs.xywh[0]
        x,y,w,h = float(x),float(y),float(w),float(h)
        area = w * h

        xVal = int(xPID.update(cx))
        yVal = int(yPID.update(cy))
        zVal = int(zPID.update(area))

    drone.send_rc_control(0, -zVal, -yVal, xVal)
    """
def getKeyboardInput(): 
     lr, fb, ud, yv = 0, 0, 0, 0 
     speed = 50 
 
     if key.is_pressed('LEFT'): lr =  -speed 
     elif key.is_pressed('RIGHT'): lr = speed 
 
     if key.is_pressed('UP'): fb = -speed 
     elif key.is_pressed('DOWN'): ud = speed 
 
     if key.is_pressed('f'): fb = speed 
     elif key.is_pressed('b'): fb = -speed 
 
     if key.is_pressed('s'): yv = speed 
     elif key.is_pressed('u'): yv = -speed 
     if key.is_pressed('t'): drone.takeoff() 
 
     if key.is_pressed("f"):drone.move_forward(21) 
     if key.is_pressed("m"):drone.move_up(40) 
     if key.is_pressed("b"):drone.move_back(21) 
     if key.is_pressed("r"):drone.rotate_counter_clockwise(45) 
 
 
     if key.is_pressed('l'): drone.land() 
 
     return [lr, fb, ud, yv] 
 
while True:
    img = drone.get_frame_read().frame
    results = model.predict(img, imgsz=320)
    im_array = results[0].plot()  # plot a BGR numpy array of predictions

    vals = getKeyboardInput() 
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    cv2.imshow("image",im_array)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cv2.waitKey(5)
