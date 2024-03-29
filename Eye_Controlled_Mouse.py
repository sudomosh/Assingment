import cv2
import mediapipe as mp
import pyautogui as pag

faceMesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)
screen_width , screen_height = pag.size()
while True:
    _, frame = cam.read()                                  # Reads the camera
    frame = cv2.flip(frame, 1)                             # flips the frame vertically
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     # changes BGR to RGB for easy processing
    output = faceMesh.process(rgb_frame)                   # Gives the RGB output
    markings = output.multi_face_landmarks                 # Detects landmarks on face
    frame_height, frame_width, _ = frame.shape             # Detects fame width and height


    if markings:
        landmarks = markings[0].landmark
        for id, p in enumerate(landmarks[474:478]):
            x = int(p.x * frame_width)
            y = int(p.y * frame_height)
            cv2.circle(frame, (x,y), 1 , (0, 255, 0))
            if id == 1:
                screen_x = screen_width / frame_width * x
                screen_y = screen_height / frame_height * y
                pag.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for p in left:
            x = int(p.x * frame_width)
            y = int(p.y * frame_height)
            cv2.circle(frame, (x, y), 1, (0, 255, 200))
        if (left[0].y - left[1].y) < 0.008:
            pag.click()
            pag.sleep(1)



    cv2.imshow("Mouse", frame)
    cv2.waitKey(1)
