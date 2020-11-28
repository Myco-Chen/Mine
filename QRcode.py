import os
import cv2 as cv
import requests
from pyzbar.pyzbar import decode


def py_parse_code(fp):
    if os.path.isfile(fp):
        img = cv.imread(fp)
    else:
        with open("./qrCodeTEst.png","wb") as f:
            f.write(requests.get(url=filepath).content)
        img = cv.imread("./qrCodeTest.png")
    texts = decode(img)
    for text in texts:
        qr_info = text.data.decode("utf-8")
        print(qr_info)


while 1:
    filepath = input()
    if filepath == 'Esc':
        import sys
        sys.exit()
    else:
        py_parse_code(filepath)