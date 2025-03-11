import unittest
from unittest.mock import patch
from your_password_generator import data_collection, generate_password  # Импортируйте функции из вашего файла

class TestPasswordGenerator(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', '8', 'да', 'да', 'да', 'да', 'да'])
    def test_data_collection_correct_input(self, mock_input):
        data_collection()
        self.assertEqual(quantity, 1)
        self.assertEqual(lenght, 8)
        self.assertIn('0123456789', chars)
        self.assertIn('abcdefghijklmnopqrstuvwxyz', chars)
        self.assertIn('ABCDEFGHIJKLMNOPQRSTUVWXYZ', chars)
        self.assertIn('!#$%&*+-=?@^_', chars)

    def test_generate_password_length(self):
        # Пример корректной генерации пароля длиной 8 символов
        chars = 'abc123!@#'
        generated_password = generate_password(8, 1, chars)
        self.assertEqual(len(generated_password), 8)

if __name__ == '__main__':
    unittest.main()
