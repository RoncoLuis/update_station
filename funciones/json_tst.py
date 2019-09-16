import json
import time
response ={
    "Paradero":[
        {
            "id":"p_001",
            "nombre":"estacion juarez",
            "fecha":time.strftime("%d/%m/%y"),
            "hora":time.strftime("%H:%M:%S")
        }
    ]
}

respuesta = {"Paradero": [{"id": "p_001", "nombre": "estacion juarez", "fecha": "11/09/19", "hora": "23:36:58"}]}

#Codificar JSON
encode = json.dumps(response)
print('Encoded:',encode)

#Decodificar Json
decode = json.loads(encode)
print('decoded:',decode)
