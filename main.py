from face_recognition_module import capturar_imagem, reconhecer_face
from email_module import enviar_email
from backup_module import backup_imagens
from datetime import datetime

if __name__ == "__main__":
    # Captura de imagem ao detectar movimento
    imagem_capturada = capturar_imagem()

    if imagem_capturada:
        aluno = reconhecer_face(imagem_capturada)

        if aluno:
            # Enviar e-mail com dados do aluno reconhecido
            enviar_email("Aluno reconhecido", f"Aluno identificado: {aluno}", imagem_capturada)
        else:
            # Enviar e-mail de alerta para pessoa não identificada
            enviar_email("Pessoa não identificada", "A pessoa capturada não foi identificada", imagem_capturada)

        # Fazer backup das imagens ao final do dia
        hora_atual = datetime.now().hour
        if hora_atual >= 23:
            backup_imagens()
