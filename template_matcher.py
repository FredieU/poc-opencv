import cv2
import numpy as np

img = cv2.imread(filename='assets/beach.jpg', flags=0)
wally = cv2.resize(src=cv2.imread('assets/wally.png', 0), dsize=(50, 50))
h, w = wally.shape

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
]


def match_template():
    for method in methods:
        img2 = img.copy()
        result = cv2.matchTemplate(image=img2, templ=wally, method=method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        pt2 = (location[0] + w, location[1] + h)
        cv2.rectangle(img=img2, pt1=location, pt2=pt2, color=(255, 255, 0), thickness=5)
        cv2.imshow('MATCH', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    match_template()
