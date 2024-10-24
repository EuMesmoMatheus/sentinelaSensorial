import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase-sdk-adm.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = db.collection('alunos').document("Lucas").get()

if doc.exists:
    print(doc.to_dict())
else:
    print('Documento não encontrado!')