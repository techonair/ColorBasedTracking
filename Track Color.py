import cv2

redUpper = ( , , )
redLower =  ( , , )

cam = cv2.VideoCapture(0)

while True:
    grabbed, img = cam.read()
    img = cv2.resize(img, None, fx= 1, fy= 1)
    gaussianBlur = cv2.GaussianBlur(img, (21,21), 0)
    hsvImg = cv2.cvtColor(gaussianBlur, cv2.COLOR_BGR2HSV)

    hsvImg = cv2.erode(hsvImg, None)[2]
    hsvImg = cv2.dilate(hsvImg, None, iterations=2)
    

    cv2.imshow('Colored Object Tracking', img)

    key = cv2.waitKey(0) & 0xFF
    if key == cv2.waitkey('q'):
        break

cam.release()
cv2.destroyAllWindows()