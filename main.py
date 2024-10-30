from face_recognition_module import capturar_imagem
from email_module import enviar_email
from backup_module import backup_imagens
from database_module import inicia_banco, baixa_fotos
from datetime import datetime
import keyboard # type: ignore
import os

if __name__ == "__main__":
    alunos = []
    desconhecidos = []

    while True:
        
        print("Iniciando...")
        db = inicia_banco()
        
        lista_alunos = baixa_fotos(db)

        alunos_capturados= capturar_imagem(lista_alunos)

        for aluno in alunos_capturados[0]:
            alunos.append(aluno)
            print(alunos)
        # Enviar e-mail de alerta para pessoa não identificada
        for pessoa in alunos_capturados[2]:
            desconhecidos.append(pessoa)

        if len(desconhecidos) > 0:
            enviar_email("Pessoa não identificada", "A pessoa capturada não foi identificada", desconhecidos)

        print("Enviar email?(Y/N)")

        if keyboard.read_key() == "y":
            enviar_email("Aluno reconhecido", f"Aluno identificado: {alunos}", alunos)
            
        elif keyboard.read_key() == "n":
            os.system("cls")

        # Fazer backup das imagens ao final do dia
        hora_atual = datetime.now().hour
        if hora_atual >= 23:
            backup_imagens()

        break
