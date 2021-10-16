import cv2

redUpper = ( , , )
redLower =  ( , , )

cam = cv2.VideoCapture(0)

while True:
    # Reading, resizing, blurring, converting image to HSV format.
    grabbed, img = cam.read()
    img = cv2.resize(img, None, fx= 1, fy= 1)
    gaussianBlur = cv2.GaussianBlur(img, (21,21), 0)
    hsvImg = cv2.cvtColor(gaussianBlur, cv2.COLOR_BGR2HSV)

    # Masking out the selected color only and processing it.
    grab_color = cv2.inRange(hsvImg, redLower, redUpper)
    hsvImg = cv2.erode(grab_color, None, iterations=2)
    hsvImg = cv2.dilate(grab_color, None, iterations=2)

    # Retriving only the extreme outer contours
    # and storing only the corner points
    mask_cnts = cv2.findContours(hsvImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    # If that color is not on the list we will keep it normal
    # however if that color is detected this 'if' statement will run

    if len(mask_cnts)> 0:
        c = max(mask_cnts, key= )
        

    cv2.imshow('Colored Object Tracking', img)

    key = cv2.waitKey(0) & 0xFF
    if key == cv2.waitkey('q'):
        break

cam.release()
cv2.destroyAllWindows()