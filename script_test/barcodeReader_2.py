"""
    Programa en Python para leer codigos QR.
    Muestra sus dimensiones en la pantalla, su mensaje y su rotacion en grados.

    Escrito por Glare,
    www.robologs.net
    fuente: https://robologs.net/2017/07/17/deteccion-de-codigos-qr-en-python-con-opencv-y-zbar/
"""

from pyzbar.pyzbar import decode
from threading import Timer
import json
import cv2
import numpy as np

bgr = (255, 255, 255)
cap = cv2.VideoCapture(0)
text_font = cv2.FONT_HERSHEY_SIMPLEX

def barcodeReader(image, bgr):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)

    for decodedObject in barcodes: #loop dibuja recuadro en imagen QR

        points = decodedObject.polygon  # loc
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image,[pts], True, (255,0, 0), 2)
        data = decodedObject.data.decode("utf-8")
        type_source = decodedObject.type
        cv2.putText(image, data + " - " + type_source, (30, 30), text_font, 0.7, bgr, 2)
        #response = ["Barcode: {} - Type: {}".format(decodedObject.data.decode("utf-8"), decodedObject.type)]
        return data


def insertData(json_response):
    encoded = json.dumps(json_response)
    decoded = json.loads(encoded)
    return decoded

while True:
    val, frame = cap.read()
    if val:
        barcode = barcodeReader(frame, bgr)
        print(insertData(barcode))
        #print(barcode) #retraso de tiempo
        #sintaxis del timer = t = Timer(tiempo,funcion) t.start()
        cv2.imshow('Lector QR', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
cv2.destroyAllWindows()
