from face_recognition_module import capturar_imagem, reconhecer_face
from email_module import enviar_email
from backup_module import backup_imagens
from datetime import datetime
import keyboard # type: ignore
import os

if __name__ == "__main__":
    alunos = []

    while True:
        
        print("Iniciando...")
        alunos_capturados = capturar_imagem()

        for aluno in alunos_capturados[1]:
            alunos.append(aluno)
            print(alunos)
        # Enviar e-mail de alerta para pessoa não identificada
            #enviar_email("Pessoa não identificada", "A pessoa capturada não foi identificada", imagem_capturada)

        print("Enviar email?(Y/N)")

        if keyboard.read_key() == "y":
            print("enviou o email")
            #enviar_email("Aluno reconhecido", f"Aluno identificado: {aluno}", alunos)
            
        elif keyboard.read_key() == "n":
            os.system("cls")

        # Fazer backup das imagens ao final do dia
        hora_atual = datetime.now().hour
        if hora_atual >= 23:
            backup_imagens()

        break
