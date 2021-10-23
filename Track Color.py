import cv2

redLower = (0, 0, 200)
redUpper = (0, 0, 255)

cam = cv2.VideoCapture(0)

while True:
    # Reading, resizing, blurring, converting image to HSV format.
    (grabbed, img) = cam.read()
    img = cv2.resize(img, None, fx= 1, fy= 1)
    gaussianBlur = cv2.GaussianBlur(img, (11,11), 0)
    hsvImg = cv2.cvtColor(gaussianBlur, cv2.COLOR_BGR2HSV)

    # Masking out the selected color only and processing it.
    grab_color = cv2.inRange(hsvImg, redLower, redUpper)
    mask = cv2.erode(grab_color, None, iterations=2)
    cv2.imshow('Erode Mask', mask)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('Dilate Mask', mask)

    # Retriving only the extreme outer contours
    # and storing only the corner points
    mask_cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    # If that color is not on the list we will keep it normal
    # however if that color is detected this 'if' statement will run
    center = None
    if len(mask_cnts)> 0:
        c = max(mask_cnts, key= cv2.contourArea)
        print(c)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Based on minimum enclosing circle's radius 
        # we are making code more practical for real life application
        # circle is only printed if radius > 10 and till critical value of radius which is 250
        # Left : when { x coordinate < 150 }
        # Right : when { x coordinate > 450 }
        # Front : when { radius < 250 } and x coordinate is between 150 to 450

        if radius > 10:
            # minimum enclosing circle
            cv2.circle(img, (int(x), int(y)), int(radius), (0,255,255), 2)
            # center point-cirlce
            cv2.circle(img, center, 5, (0, 0, 255), -1)
            print(center, radius)
        if radius > 250:
            print("stop")
        else:
            if (center[0]<150):
                print('Left')
            elif (center[0]>450):
                print('Right')
            elif (radius<250):
                print('Front')
            else:
                print('Stop')


    cv2.imshow('Colored Object Tracking', img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()