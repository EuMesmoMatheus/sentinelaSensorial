from face_recognition_module import capturar_imagem, reconhecer_face
from email_module import enviar_email
from backup_module import backup_imagens
from datetime import datetime
import keyboard
import os

if __name__ == "__main__":

    while True:
        # Captura de imagem ao detectar movimento
        print("Iniciar Reconhecimento?(Y/N)")

        if keyboard.read_key() == "n":
            break
        elif keyboard.read_key() == "y":
            print("Iniciando...")
            imagem_capturada = capturar_imagem()

            alunos = []

            if imagem_capturada:
                aluno = reconhecer_face(imagem_capturada)

                if aluno:
                    alunos.append('captured_images/'+aluno)
                else:
                #     enviar_email("Pessoa não identificada", "A pessoa capturada não foi identificada", imagem_capturada)
                    print("pessoa desconhecida")

                print("Enviar email?(Y/N)")

                if keyboard.read_key() == "y":
                    print("enviou o email")
                elif keyboard.read_key() == "n":
                    os.system("cls")

                

                # if aluno:
                #     # Enviar e-mail com dados do aluno reconhecido
                #     enviar_email("Aluno reconhecido", f"Aluno identificado: {aluno}", imagem_capturada)
                # else:
                #     # Enviar e-mail de alerta para pessoa não identificada
                #     enviar_email("Pessoa não identificada", "A pessoa capturada não foi identificada", imagem_capturada)

                # Fazer backup das imagens ao final do dia
                hora_atual = datetime.now().hour
                if hora_atual >= 23:
                    backup_imagens()
