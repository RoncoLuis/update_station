"""
Luis Ronquillo
Date : 06-09-2019
"""
import qrcode
import time
import json


def estructura(id, estacion, ruta):
    #función para generar la estructura de los codigos qr
    paradero = {
        "id_paradero": id,
        "estacion": estacion,
        "ruta": ruta
    }
    return paradero


# Aquí va la lista con la información de los paraderos
p_001 = {
    "Paradero": [
        {
            "id": "p_001",
            "nombre": "estacion juarez",
            "fecha": time.strftime("%d/%m/%y"),
            "hora": time.strftime("%H:%M:%S")
        }
    ]
}

p_002 = {
    "Paradero": [
        {
            "id": "p_002",
            "nombre": "centro historico",
            "fecha": time.strftime("%d/%m/%y"),
            "hora": time.strftime("%H:%M:%S")
        }
    ]
}

p_003 = {
    "Paradero": [
        {
            "id": "p_003",
            "nombre": "poliforum",
            "fecha": time.strftime("%d/%m/%y"),
            "hora": time.strftime("%H:%M:%S")
        }
    ]
}

p_004 = {
    "Paradero": [
        {
            "id": "p_004",
            "nombre": "plaza tecnologia",
            "fecha": time.strftime("%d/%m/%y"),
            "hora": time.strftime("%H:%M:%S")
        }
    ]
}

# La funcion dumps nos sirve para formatear el diccionario a json
# info = json.loads(json.dumps(data))

qr = qrcode.QRCode(
    # aqui va la configuracion y personalizacion del codigo qr
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=5
)

qr.add_data(json.dumps(p_001))
qr.make(fit=True)
img_p001 = qr.make_image(fill='black', back_color='white')
img_p001.save('../img/p001_qr-code.png')

qr.clear()
qr.add_data(json.dumps(p_002))
qr.make(fit=True)
img_p002 = qr.make_image(fill='black', back_color='white')
img_p002.save('../img/p002_qr-code.png')

qr.clear()
qr.add_data(json.dumps(p_003))
qr.make(fit=True)
img_p003 = qr.make_image(fill='black', back_color='white')
img_p003.save('../img/p003_qr-code.png')

qr.clear()
qr.add_data(json.dumps(p_004))
qr.make(fit=True)
img_p004 = qr.make_image(fill='black', back_color='white')
img_p004.save('../img/p004_qr-code.png')

print('Códigos QR generados')
print('Ejemplo 1:', json.dumps(p_001))
