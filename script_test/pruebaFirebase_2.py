import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time

p_001 ={"id":"p_002","nombre":"universidad"}
p_001['fecha'] = time.strftime("%d/%m/%y")
p_001['hora'] = time.strftime("%H:%M:%S")

encoded = json.dumps(p_001)
decoded = json.loads(encoded)
print(decoded)
#Fetch the service account key JSON file contents
#credentials = credentials.Certificate('../ficheros_salidas/tst-update-station-firebase-adminsdk-jq8g5-71c9c42d8b.json')

#initialize the app with a service account, granting admin privileges
#firebase_admin.initialize_app(credentials,{
#    'databaseURL':'https://tst-update-station.firebaseio.com/'
#})

#ref = db.reference('stored_data')
#user_ref = ref.child('updatestation').child('paradero').push(decoded)