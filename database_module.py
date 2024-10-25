import firebase_admin  # type: ignore
from firebase_admin import credentials, firestore  # type: ignore

def inicia_banco():
    cred = credentials.Certificate("firebase-sdk-adm.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'gs://sentinela-sensorial.appspot.com'
    })
    # Conectando ao Firestore
    db = firestore.client()
    return db

def baixa_fotos(db):
    col_ref = db.collection('alunos')
    docs = col_ref.stream()
    
    lista_links = []

    for doc in docs:
        dados = doc.to_dict()
        nome = dados.get('nome')
        foto_ref = dados.get('foto')

        if nome and foto_ref:
            lista_links.append([nome, foto_ref])

    return lista_links
