import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

#picked base colors using color_picker.py

myColors = [[173, 150, 0, 179, 255, 255],
            [59, 129, 0, 109, 255, 255],
            [173, 150, 0, 179, 255, 255]]

myColorValues = [[0,0,255],
                 [230,215,14],
                 [0,0,255]]

myPoints = []

def findColors(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorValues[count],cv2.FILLED)

        if x!=0 and y!=0:
            newPoints.append([x,y,count])

        count+=1

        # cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>70:
            cv2.drawContours(imgResult, cnt, -1, (255,0,0),2)
            peri = cv2.arcLength(cnt, False)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, False)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgResult, (x,y), (x+w, y+h), (0, 255,0), 1)

    return x+w//2,y 

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]),10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColors(img, myColors)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
