import cv2
import mediapipe as mp
import numpy as np
import pyautogui
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import math

x1 = y1 = x2 = y2 = 0

webcam = cv2.VideoCapture(0)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

myHands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
# drawing_utils draws points on the hand

while True:
    _, image = webcam.read()
    image = cv2.flip(image,1)
    frameHeight, frameWidth,_ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = myHands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frameWidth)
                y = int(landmark.y * frameHeight)
                # For drawing green circle on forefinger
                if id ==8:
                    cv2.circle(img = image, center=(x,y), radius=9, color=(0, 255,0), thickness=3)
                    x1 = x
                    y1 = y
                # For drawing red circle on thumb
                if id == 4:
                    cv2.circle(img=image, center=(x,y), radius=9, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2) ** (0.5) //4
        # for drawing yellow line connecting the two circles
        cv2.line(image,(x1,y1), (x2,y2), (0,255,255), 4)

        # Getting current volume level (0.0 to 1.0)
        currentVol = volume.GetMasterVolumeLevelScalar()

        # Map distance to volume level
        vol = np.interp(dist, [6, 60], [0.0, 1.0])
        volume.SetMasterVolumeLevelScalar(vol, None)
        if dist > 30:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

        # This displays text on the video
        cv2.putText(image, f'Vol: {int(vol * 100)}%', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Hand Volume Control", image)

    # This waits for 10 milliseconds before capturing next video frame (going back to while loop)
    key = cv2.waitKey(10)

    # 27 is the esc key, when pressed; the window closes
    if key ==27:
        break

webcam.release()
cv2.destroyAllWindows()
