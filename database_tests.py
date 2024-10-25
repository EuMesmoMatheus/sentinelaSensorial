import unittest
from unittest.mock import patch, MagicMock
from database_module import inicia_banco, baixa_fotos

class TestDatabaseModule(unittest.TestCase):

    @patch('firebase_admin.initialize_app')
    @patch('firebase_admin.firestore.client')
    def test_inicia_banco(self, mock_firestore_client, mock_initialize_app):
        mock_firestore_client.return_value = MagicMock()

        db = inicia_banco()

        mock_initialize_app.assert_called_once()
        self.assertIsNotNone(db)

    @patch('firebase_admin.firestore.client')
    def test_baixa_fotos(self, mock_firestore_client):
        # Cria um mock para a coleção "alunos"
        mock_db = MagicMock()
        mock_firestore_client.return_value = mock_db

        # Simula a coleção chamada "alunos"
        mock_alunos_collection = MagicMock()
        mock_db.collection.return_value = mock_alunos_collection

        # Simula o retorno de documentos na coleção "alunos"
        mock_alunos_collection.stream.return_value = [
            MagicMock(to_dict=lambda: {'nome': 'Aluno1', 'foto': 'url1'}),
            MagicMock(to_dict=lambda: {'nome': 'Aluno2', 'foto': 'url2'}),
        ]

        # Executa a função com o Firestore simulado
        links = baixa_fotos(mock_db)

        # Verifica o retorno esperado
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0], ['Aluno1', 'url1'])
        self.assertEqual(links[1], ['Aluno2', 'url2'])


if __name__ == "__main__":
    unittest.main()
