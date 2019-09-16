import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time
from script_main import generar_qr

json_data = generar_qr.make_json_data('p_001','Delta-Universidad','alimentadora')
json_data['fecha'] = time.strftime("%d/%m/%y")
json_data['hora'] = time.strftime("%H:%M:%S")
generar_qr.make_qr(json_data,'prueba_1')

encoded = json.dumps(json_data)
decoded = json.loads(encoded)
print(decoded)
#Fetch the service account key JSON file contents
credentials = credentials.Certificate('../ficheros_salidas/tst-update-station-firebase-adminsdk-jq8g5-71c9c42d8b.json')

#initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(credentials,{'databaseURL':'https://tst-update-station.firebaseio.com/'})


ref = db.reference('stored_data')
user_ref = ref.child('updatestation').child('paradero').push(decoded)