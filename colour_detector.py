import cv2
import numpy as np


def scan_colour():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        hsv = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2HSV)
        lower_bound = np.array([110, 50, 50])
        upper_bound = np.array([130, 255, 255])

        mask = cv2.inRange(src=hsv, lowerb=lower_bound, upperb=upper_bound)
        filtered = cv2.bitwise_and(src1=frame, src2=frame, mask=mask)
        cv2.imshow('Filtered', filtered)
        cv2.imshow('Mask', mask)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    scan_colour()
