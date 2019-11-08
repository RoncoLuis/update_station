"""
    Programa en Python para leer codigos QR.
    Muestra sus dimensiones en la pantalla, su mensaje y su rotacion en grados.

    Escrito por Glare,
    www.robologs.net
    fuente: https://robologs.net/2017/07/17/deteccion-de-codigos-qr-en-python-con-opencv-y-zbar/
"""

from pyzbar.pyzbar import decode
import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials, db
import json
import time
from script_main import generar_qr

# credenciales para ingresar a la app tst-update-station de firebase
CREDENTIALS = credentials.Certificate('../ficheros_salidas/tst-update-station-firebase-adminsdk-jq8g5-71c9c42d8b.json')
# inicializar de la app tst-update-station de firebase con permisos de administrador
# retorna un objeto de conexión,para evitar hacer la conexion en cada iteración
OBJ_FIREBASE = firebase_admin.initialize_app(CREDENTIALS, {'databaseURL': 'https://tst-update-station.firebaseio.com/'})
REFERENCE = db.reference('stored_data')

# variables de personalización para la vista de cámara web
cap = cv2.VideoCapture(1)  # inicializa la cámara web 0:webcam externa, 1:webcam integrada
bgr = (255, 255, 255)
text_font = cv2.FONT_HERSHEY_SIMPLEX

def barcodereader(image, bgr):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)
    for decodedObject in barcodes:  # loop dibuja recuadro en imagen QR
        points = decodedObject.polygon  # loc
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (255, 0, 0), 2)
        data = decodedObject.data.decode("utf-8")
        type_source = decodedObject.type
        cv2.putText(image, data + " - " + type_source, (30, 30), text_font, 0.7, bgr, 2)
        return data

def returndata():
    new_reference = db.reference('stored_data/updatestation/').order_by_child('paradero').limit_to_last(10)
    for key in new_reference:
        print(key)

while True:
    val, frame = cap.read()
    if val:
        barcode = barcodereader(frame, bgr)
        cv2.imshow('updatestation QR', frame)
        if type(barcode) is str:
            json_data = json.loads(barcode)
            json_data['fecha'] = time.strftime("%d/%m/%y")
            json_data['hora'] = time.strftime("%H:%M:%S")
            print(json_data)
            #TODO se comento esta linea para no hacer el insert en firebase
           # REFERENCE.child('updatestation').child('paradero').push(json_data)
            #print(type(json.loads(barcode)))
        code = cv2.waitKey(10)
        if code == ord('q'):
            cv2.destroyAllWindows()
            answer = int(input('Desea descargar la información 1.Si 2.No: '))
            if answer == 1:
                returndata()
            else:
                print('Adiós')
            break

