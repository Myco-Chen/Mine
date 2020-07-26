import os
import cv2 as cv
import requests
from pyzbar.pyzbar import decode
def pyzbarParseQRcode(filepath):
    if os.path.isfile(filepath):
        img = cv.imread(filepath)
    else:
        with open("./qrCodeTEst.png","wb") as f:
            f.write(requests.get(url=filepath).content)
        img = cv.imread("./qrCodeTest.png")
    texts = decode(img)
    for text in texts:
        qrInfo = text.data.decode("utf-8")
        print(qrInfo)

while 1:
    filepath = input()
    if filepath == 'Esc':
        import sys
        sys.exit()
    else:
        pyzbarParseQRcode(filepath)

#test