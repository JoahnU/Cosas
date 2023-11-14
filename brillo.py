import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc

cap = cv2.VideoCapture(0)  # Checks for camera

mpHands = mp.solutions.hands  # detects hand/finger
hands = mpHands.Hands()  # complete the initialization configuration of hands
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()  # If camera works capture an image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to rgb

    # Collection of gesture information
    results = hands.process(imgRGB)  # completes the image processing.

    lmList = []  # empty list
    if results.multi_hand_landmarks:  # list of all hands detected.
        # By accessing the list, we can get the information of each hand's corresponding flag bit
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):  # adding counter and returning it
                # Get finger joint points
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])  # adding to the empty list 'lmList'
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

    if lmList != []:
        # getting the value at a point
        # x      #y
        x1, y1 = lmList[4][1], lmList[4][2]  # thumb
        x2, y2 = lmList[8][1], lmList[8][2]  # index finger
        # creating circle at the tips of thumb and index finger
        cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)  # image #fingers #radius #rgb
        cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)  # image #fingers #radius #rgb
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)  # create a line b/w tips of index finger and thumb

        length = hypot(x2 - x1, y2 - y1)  # distance b/w tips using hypotenuse

        # Get the current brightness level
        current_brightness = sbc.get_brightness()

        current_brightness = int(current_brightness[0])

        # Luego realiza la multiplicación

        new_brightness = int(current_brightness * length / 400)

        sbc.set_brightness(new_brightness)

    cv2.imshow('Image', img)  # Show the video
    if cv2.waitKey(1) & 0xff == ord(' '):  # By using spacebar delay will stop
        break

cap.release()  # stop cam
cv2.destroyAllWindows()  # close window
