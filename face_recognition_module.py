import cv2 # type: ignore
import face_recognition # type: ignore
import os
import requests
import numpy as np
from datetime import datetime

PASTA_X = 'captured_images/'  # Pasta onde as imagens capturadas serão salvas
#PASTA_Y = 'student_images/'   # Pasta onde estão as imagens dos alunos

def carregar_imagem(url):
    response = requests.get(url)
    img_array = np.array(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(img_array, -1)
    return image


def capturar_imagem(students_list):
    lista_alunos = []
    for aluno in students_list:
        aluno_nome, aluno_link = aluno
        aluno_foto = carregar_imagem(aluno_link)
        lista_alunos.append([aluno_nome,aluno_foto])

    # Inicializa webcam
    cap = cv2.VideoCapture(1)
    alunos_reconhecidos = []
    faces_reconhecidas = []
    faces_desconhecidas = []

    cap.set(3, 640)
    cap.set(4, 480)

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Detecção de rosto a cada 150 frames
        if frame_count % 150 == 0:  
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                match_found = False
                for aluno in lista_alunos:
                    aluno_nome, aluno_link = aluno
                    student_image = aluno_link
                    student_encoding = face_recognition.face_encodings(student_image)[0]

                    results = face_recognition.compare_faces([student_encoding], face_encoding)
                    face_distance = face_recognition.face_distance([student_encoding], face_encoding)

                    if results[0]:  # Se houver uma correspondência
                        if aluno_nome not in alunos_reconhecidos:
                            label = f'{aluno_nome} (Distancia: {face_distance[0]:.2f})'
                            color = (0, 255, 0)
                            desenha_retangulo(frame, left, top, right, bottom, label, color)
                            filename = PASTA_X +f"{aluno_nome}_"+ datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
                            cv2.imwrite(filename, frame)
                            alunos_reconhecidos.append(aluno_nome)
                            faces_reconhecidas.append("./" + filename)
                        else:
                            label = f'{aluno_nome} (Distancia: {face_distance[0]:.2f})'
                            color = (0, 255, 0)
                            desenha_retangulo(frame, left, top, right, bottom, label, color)

                        match_found = True
                        break

                if not match_found:  # Caso nenhum rosto conhecido seja encontrado
                    label = "Desconhecido"
                    color = (0, 0, 255)
                    desenha_retangulo(frame, left, top, right, bottom, label, color)
                    filename = PASTA_X + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
                    cv2.imwrite(filename, frame)
                    faces_desconhecidas.append("./" + filename)
            cv2.imshow("Webcam ao vivo", frame)
            cv2.waitKey(2000)

        cv2.imshow("Webcam ao vivo", frame)

        frame_count += 1

        # Sai do loop ao pressionar a tecla 'ESC'
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return faces_reconhecidas, alunos_reconhecidos, faces_desconhecidas


def desenha_retangulo(frame,l,t,r,b,nome, cor):
    cv2.rectangle(frame, (l,t), (r, b), cor, 2)
    cv2.putText(frame,nome,(l,t-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)