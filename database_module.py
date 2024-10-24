import firebase_admin #type: ignore
from firebase_admin import credentials, firestore, storage #type: ignore



def inicia_banco():
    cred = credentials.Certificate("firebase-sdk-adm.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'gs://sentinela-sensorial.appspot.com'  # Substitua pelo nome do seu bucket de storage
    })
    # Conectando ao Firestore
    db = firestore.client()

    return db

def baixa_fotos(db):
    # Referenciando a coleção no Firestore
    col_ref = db.collection('alunos')

    # Recuperando todos os documentos da coleção
    docs = col_ref.stream()

    # Criando uma lista para armazenar os links de download
    lista_links = []

   # Iterando sobre os documentos
    for doc in docs:
        dados = doc.to_dict()
        
        # Acessando o nome da pessoa e a referência da foto
        nome = dados.get('nome')
        foto_ref = dados.get('foto')  # O campo que contém a referência no Storage

        if nome and foto_ref:
            
            # Adicionando o nome e o link da foto à matriz
            lista_links.append([nome, foto_ref])

    # Exibindo a matriz com os nomes e links para as fotos
    return lista_links