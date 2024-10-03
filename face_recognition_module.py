import cv2
import face_recognition
import mediapipe as mp
import os
from datetime import datetime

PASTA_X = 'captured_images/'  # Pasta onde as imagens capturadas serão salvas
PASTA_Y = 'student_images/'   # Pasta onde estão as imagens dos alunos


def capturar_imagem():
    # Inicializa webcam
    cap = cv2.VideoCapture(0)
    mp_solution = mp.solutions.face_detection
    mp_recognition = mp_solution.FaceDetection()
    mp_draw = mp.solutions.drawing_utils
    alunos_reconhecidos = []
    faces_reconhecidas = []
    faces_desconhecidas = []

    cap.set(3,640)
    cap.set(4,480)

    frame_count = 0
    

    while True:
        ret, frame = cap.read()
        cv2.imshow("Rosto",frame)
        filename = ""

        if not ret:
            break

        if frame_count % 150 == 0:


            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame,face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                for file in os.listdir(PASTA_Y):
                    student_image_path = os.path.join(PASTA_Y, file)
                    student_image = face_recognition.load_image_file(student_image_path)
                    student_encoding = face_recognition.face_encodings(student_image)[0]

                    results = face_recognition.compare_faces([student_encoding], face_encoding)
                    face_distance = face_recognition.face_distance([student_encoding], face_encoding)

                    if results[0] and file not in alunos_reconhecidos:
                        label = f'{file} (Distancia: {face_distance[0]:.2f})'
                        color = (0,255,0)
                        desenha_retangulo(frame,left,top,right,bottom,label,color)
                        filename = PASTA_X + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
                        cv2.imwrite(filename, frame)
                        alunos_reconhecidos.append(file)
                        faces_reconhecidas.append("./"+filename)
                        break
                    elif results[0] and file in alunos_reconhecidos:
                        label = f'{file} (Distancia: {face_distance[0]:.2f})'
                        color = (0,255,0)
                        desenha_retangulo(frame,left,top,right,bottom,label,color)
                        break
                    else:
                        label = "Desconhecido"
                        color = (0,0,255)
                        desenha_retangulo(frame,left,top,right,bottom,label,color)
                        filename = PASTA_X + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
                        cv2.imwrite(filename, frame)
                        faces_desconhecidas.append("./"+filename)
                        break

                

                
        frame_count += 1

        if cv2.waitKey(5) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    
    return faces_reconhecidas, faces_desconhecidas

def desenha_retangulo(frame,l,t,r,b,nome, cor):
    cv2.rectangle(frame, (l,t), (r, b), cor, 2)
    cv2.putText(frame,nome,(l,t-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)

def reconhecer_face(image_path):
    # Carregando a imagem capturada
    imagem_capturada = face_recognition.load_image_file(image_path)
    face_encodings_capturada = face_recognition.face_encodings(imagem_capturada)

    if len(face_encodings_capturada) > 0:
        face_capturada = face_encodings_capturada[0]
    else:
        print('Nenhuma face reconhecida na imagem capturada')
        return None

    # Comparando com as imagens da PASTA_Y (alunos)
    for file in os.listdir(PASTA_Y):
        student_image_path = os.path.join(PASTA_Y, file)
        student_image = face_recognition.load_image_file(student_image_path)
        student_encoding = face_recognition.face_encodings(student_image)[0]

        results = face_recognition.compare_faces([student_encoding], face_capturada)

        if results[0]:
            print(f'Aluno reconhecido: {file}')
            return file

    print('Pessoa não identificada')
    return None
