import unittest
import xmlrunner
from code_project import data_collection, generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_data_collection_valid_input(self):
        inputs = ['3', '8', 'да', 'да', 'да', 'да', 'нет']
        quantity, length, chars, symbol = data_collection(inputs)
        self.assertEqual(quantity, 3)
        self.assertEqual(length, 8)
        self.assertIn('0123456789', chars)
        self.assertIn('abcdefghijklmnopqrstuvwxyz', chars)
        self.assertIn('ABCDEFGHIJKLMNOPQRSTUVWXYZ', chars)
        self.assertIn('!#$%&*+-=?@^_', chars)

    def test_data_collection_no_characters(self):
        inputs = ['1', '8', 'нет', 'нет', 'нет', 'нет', 'нет']
        result = data_collection(inputs)
        self.assertEqual(result, (None, None, None))  # Проверяем, что результат None, т.к. нет символов

    def test_generate_password_length(self):
        chars = 'abc123!@#'
        generated_password = generate_password(8, 1, chars)
        self.assertEqual(len(generated_password[0]), 8)  # Проверяем длину пароля
        self.assertIsInstance(generated_password, list)   # Проверка, что возвращается список

    def test_generate_password_no_characters(self):
        generated_password = generate_password(8, 0, '')
        self.assertEqual(generated_password, [])  # Проверяем, что ничего не сгенерировано

if __name__ == '__main__':
    with open('test_results.xml', 'wb') as output:  # Создаем XML файл для отчетов
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), buffer=True, failfast=True)
