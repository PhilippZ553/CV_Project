import cv2
import mediapipe as mp
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_drawing

#getting the webcam
cap = cv2.VideoCapture(0)

#init mediapipe hand tracking
hands = mp_hands.Hands()

while True:
    #grab current frame from camera
    success, img = cap.read()

    #change from bgr to rgb colors
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    #detect hands
    results = hands.process(imgRGB)

    #check if hands were detected
    if results.multi_hand_landmarks:
        #loop through every hand found in frame
        for handLms in results.multi_hand_landmarks:
            #draw landmarks
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    #show in window
    cv2.imshow("hand tracking", img)

    #break if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release resources 
cap.release()
cv2.destroyAllWindows()
