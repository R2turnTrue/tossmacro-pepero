import math
import cv2
import pyautogui
import numpy as np
import time

#(36, 299)
#(460, 902)

template = cv2.imread('pepero.png')
h,w = template.shape[:2]

last_pos = (99999, 99999)
pyautogui.PAUSE = 0.0


while cv2.waitKey(1) < 0 :
    img_frame = np.array(pyautogui.screenshot(region=(36, 299, 460 - 36, 902 - 299)))
    img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)

    #cv2.imshow('img', img_frame)
    #print(cv2.waitKey(5))
    img_match = cv2.matchTemplate(template, img_frame, cv2.TM_CCOEFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_match)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    ##cv2.imwrite('xx.png', img_frame)
    print(max_val, top_left)

    center = (top_left[0] + int(w / 2), top_left[1] + int(h / 2))

    if math.dist(last_pos, center) > 10:
        if max_val < 62000000:
            print('Ignoring because of threshold...')
        else:
            print('click succeed: {}'.format(max_val))
            print('Last Pos Distance: {}'.format(math.dist(last_pos, center)))
            cv2.rectangle(img_frame, top_left, bottom_right, (255, 0, 0), 2)
            last_pos = (center[0], center[1])
            pyautogui.moveTo(36 + center[0], 299 + center[1], _pause=False)
            time.sleep(0.04)
            pyautogui.click(36 + center[0], 299 + center[1], _pause=False)
            #pyautogui.click(36 + center[0], 299 + center[1], _pause=False)
            time.sleep(0.3)

    ##cv2.imwrite('aa.png', img_match)
    cv2.imshow('Img', img_frame)

    #coords = cv2.findNonZero(img_frame) # x,y

    #img = cv2.circle(img, (coords[0][0][0], coords[0][0][1]), 3, (255, 0, 0), 3)

    #print(coordinates.size)

    #cv2.imshow('Img', img)
    #print(cv2.waitKey(33))

cv2.destroyAllWindows()