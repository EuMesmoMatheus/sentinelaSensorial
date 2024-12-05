import os
import zipfile
from datetime import datetime

PASTA_X = 'captured_images/'  
BACKUP_DIR = 'backup/'       

def backup_imagens():
    # Compacta e faz backup das imagens da PASTA_X
    zip_filename = BACKUP_DIR + f'backup_{datetime.now().strftime("%d-%m-%Y")}.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(PASTA_X):
            for filename in filenames:
                zipf.write(os.path.join(foldername, filename), os.path.relpath(os.path.join(foldername, filename), PASTA_X))
    # Limpando pasta após backup
    for file in os.listdir(PASTA_X):
        os.remove(os.path.join(PASTA_X, file))

    print(f'Backup criado e pasta {PASTA_X} limpa com sucesso.')
