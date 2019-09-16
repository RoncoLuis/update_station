import firebase_admin
from firebase_admin import credentials,firestore
import time
import json

CREDENTIALS = credentials.Certificate('../ficheros_salidas/tst-update-station-firebase-adminsdk-jq8g5-71c9c42d8b.json')
default_app = firebase_admin.initialize_app(CREDENTIALS)

db = firestore.client()


p_001 ={"id":"p_002","nombre":"universidad","fecha":time.strftime("%d/%m/%y"),"hora":time.strftime("%H:%M:%S")}
encoded = json.dumps(p_001)
decoded = json.loads(encoded)

print(decoded)
doc_ref = db.collection(u'updatestation').document(u'paradero_2')
doc_ref.set(decoded)
print('se han insertado los datos correctamente')


