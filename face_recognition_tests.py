import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import cv2
from face_recognition_module import capturar_imagem, carregar_imagem, desenha_retangulo

class TestFaceRecognitionModule(unittest.TestCase):

    @patch('face_recognition_module.requests.get')
    @patch('cv2.imdecode')
    def test_carregar_imagem(self, mock_imdecode, mock_get):
        # Simula a resposta do request
        mock_get.return_value.content = b'test_image_data'
        mock_imdecode.return_value = np.zeros((480, 640, 3), dtype=np.uint8)

        result = carregar_imagem("http://test.url/image.jpg")
        
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (480, 640, 3))

    @patch('cv2.rectangle')
    @patch('cv2.putText')
    
    def test_desenha_retangulo(self, mock_putText, mock_rectangle):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        desenha_retangulo(frame, 10, 20, 30, 40, "Test", (255, 0, 0))

        # Verifica se o retângulo e o texto foram desenhados
        mock_rectangle.assert_called_once_with(frame, (10, 20), (30, 40), (255, 0, 0), 2)
        mock_putText.assert_called_once_with(frame, "Test", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)


if __name__ == "__main__":
    unittest.main()
