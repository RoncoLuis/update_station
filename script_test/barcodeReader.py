"""
    Programa en Python para leer codigos QR.
    fuente: https://cvisiondemy.com/barcode-reader-with-python-opencv-and-pyzbar/
"""
from pyzbar.pyzbar import decode
import cv2
import numpy as np

def barcodeReader(image, bgr):
    #recibe como parametro la imagen QrR
    #bgr = tupla de informacion
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convertir la imagen a gris
    barcodes = decode(gray_img) #decode funcion de pyzbar para decodificar la información del QR
    #print(barcodes)

    for decodedObject in barcodes: #loop dibuja recuadro en imagen QR
        points = decodedObject.polygon
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

    for bc in barcodes: #se muestra el texo en la ventana
        cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    bgr, 2)

        return "Barcode: {} - Type: {}".format(bc.data.decode("utf-8"), bc.type)

bgr = (0, 0, 255)
cap = cv2.VideoCapture(1)

while (True):
    ret, frame = cap.read()
    barcode = barcodeReader(frame, bgr)
    print(barcode)
    cv2.imshow('Lector QR', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break