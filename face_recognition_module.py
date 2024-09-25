import cv2
import face_recognition
import mediapipe as mp
import os
from datetime import datetime

PASTA_X = 'captured_images/'  # Pasta onde as imagens capturadas serão salvas
PASTA_Y = 'student_images/'   # Pasta onde estão as imagens dos alunos

def capturar_imagem():
    # Inicializando webcam

    cap = cv2.VideoCapture(0)
    mp_solution = mp.solutions.face_detection
    mp_recognition = mp_solution.FaceDetection()
    mp_draw = mp.solutions.drawing_utils
    os.system("cls")
    while True:        
        ret, frame = cap.read()

        rostos = mp_recognition.process(frame)

        if rostos.detections:
            for rosto in rostos.detections:
                mp_draw.draw_detection(frame, rosto)

        cv2.imshow("Rosto",frame)

        if cv2.waitKey(5) == 27:
            break
        elif cv2.waitKey(5) == 13:
            if ret:
                # Salvando imagem na PASTA_X
                filename = PASTA_X + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
                cv2.imwrite(filename, frame)
                cv2.destroyAllWindows()
                return filename
            else:
                print('Erro ao capturar a imagem')
                return None
    cv2.destroyAllWindows()
    cap.release()




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
