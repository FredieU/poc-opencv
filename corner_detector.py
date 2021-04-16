import cv2
import numpy as np


def scan_corners():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cropped = frame[40:679, 160:1119]
        # 160-1119, 40-679
        width = int(cap.get(3))
        height = int(cap.get(4))

        gray = cv2.cvtColor(cropped, cv2.COLOR_BGRA2GRAY)
        corners = cv2.goodFeaturesToTrack(image=gray, maxCorners=50, qualityLevel=0.1, minDistance=10)
        corners = np.int0(corners)

        for corner in corners:
            x, y = corner.ravel()
            # print(x, y)
            cv2.circle(img=gray, center=(x, y), radius=10, color=(255, 0, 0))

        cv2.imshow('CAM', gray)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    scan_corners()
