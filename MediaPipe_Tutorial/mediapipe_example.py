import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Setting up a web cam
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# standard Python entry point
if __name__ == "__main__":
    main()