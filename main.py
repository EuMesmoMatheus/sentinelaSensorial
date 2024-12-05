from face_recognition_module import capturar_imagem
from email_module import enviar_email
from backup_module import backup_imagens
from database_module import inicia_banco, baixa_fotos
from datetime import datetime
import keyboard # type: ignore
import csv
import os

if __name__ == "__main__":
    imagens_alunos = []
    alunos = []
    desconhecidos = []
    nome_csv = "csv/"+datetime.now().strftime("%d-%m-%Y")+".csv"

    while True:
        
        print("Iniciando...")
        db = inicia_banco()
        
        lista_alunos = baixa_fotos(db)

        alunos_capturados= capturar_imagem(lista_alunos)

        for aluno in alunos_capturados[0]:
            imagens_alunos.append(aluno)
        #    print(imagens_alunos)

        # Lista de alunos para CSV
        alunos = [
            {"alunos": aluno[0], "matricula": aluno[1], "entrada": aluno[2]}
            for aluno in alunos_capturados[1]
        ]

        #    print(alunos)
        # Enviar e-mail de alerta para pessoa não identificada
        for pessoa in alunos_capturados[2]:
            desconhecidos.append(pessoa)

        fieldnames = ["alunos", "matricula", "entrada"]

        # Escrevendo os dados no arquivo CSV
        with open(nome_csv, mode="w", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=fieldnames, delimiter=',')
            
            escritor.writeheader()  # Escreve o cabeçalho (nomes das colunas)
            escritor.writerows(alunos)  # Escreve as linhas de dados
        imagens_alunos.append(nome_csv)

        if len(desconhecidos) > 0:
            enviar_email("Pessoa não identificada", "A pessoa capturada não foi identificada", desconhecidos)

        print("Enviar email?(Y/N)")

        if keyboard.read_key() == "y":
            enviar_email("Alunos reconhecidos", f"Alunos identificados: {alunos}", imagens_alunos)
            
        elif keyboard.read_key() == "n":
            os.system("cls")

        # Fazer backup das imagens 
        print("Fazer Backup(Y/N)")

        if keyboard.read_key() == "y":
            backup_imagens()
            
        elif keyboard.read_key() == "n":
            os.system("cls")

        # Fazer backup das imagens ao final do dia
        hora_atual = datetime.now().hour
        if hora_atual >= 20:
            backup_imagens()

        break
