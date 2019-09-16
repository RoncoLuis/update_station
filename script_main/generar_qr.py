"""
Luis Ronquillo
Date : 06-09-2019
"""

def make_json_data(id,estacion,ruta):
    paradero = {
        "id_paradero": id,
        "estacion": estacion,
        "ruta": ruta
    }
    return paradero


def make_qr(json_data, qr_filename="default.png"):
    import qrcode
    import json
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=5
    )
    encoded = json.dumps(json_data)
    qr.add_data(encoded)
    qr.make_image(fit=True)
    qr_image = qr.make_image(fill='black', back_color='white')
    qr_image.save("../img/"+qr_filename+".png")
    qr.clear()
