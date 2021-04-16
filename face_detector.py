import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


def scan_faces():
    while True:
        ret, frame = cap.read()
        cropped = frame[40:679, 160:1119]
        gray = cv2.cvtColor(src=cropped, code=cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img=cropped, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)
            roi_gray = gray[y:y+h, x:x+w]
            roi_coloured = cropped[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(image=roi_gray, scaleFactor=1.3, minNeighbors=5)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img=roi_coloured, pt1=(ex, ey), pt2=(ex+ew, ey+eh), color=(0, 255, 0), thickness=5)

        cv2.imshow('CAM', cropped)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    scan_faces()
