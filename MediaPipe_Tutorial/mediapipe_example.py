import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Setting up a web cam
    cap = cv2.VideoCapture(0) # This works for MacOS too.

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()

            # Detection (convert openCV's BGR to RGB so that MediaPipe can process it)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Set flags
            image.flags.writeable = False

            # Make Detection
            returned = hands.process(image)
            image.flags.writeable = True

            # Convert back to BGR for OpenCV
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            print(returned) # Print detection results
            
            cv2.imshow("Hand Tracking", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            
        cap.release()
        cv2.destroyAllWindows()

# standard Python entry point
if __name__ == "__main__":
    main()