import cv2
import numpy as np
import screen_brightness_control as sbc
import keyboard

def calculate_brightness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)



# Open the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,0)

adj = 140

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if keyboard.is_pressed("f5") and brightness-adj <=100:
        print("+",brightness-adj)

        adj-=2

    if keyboard.is_pressed("f4") and brightness-adj >= 0:
        adj+=2
        print('-',brightness-adj)
    
    brightness = calculate_brightness(frame)
    sbc.set_brightness(brightness-adj)

cap.release()
cv2.destroyAllWindows()
