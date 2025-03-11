import random

# Строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def get_input_from_file(filename='input_data.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def data_collection(inputs):
    chars = ''
    quantity = int(inputs[0])  # Количество паролей
    length = int(inputs[1])    # Длина пароля
    if quantity == 0 or length == 0:
        return None, None, None

    # Обработка включения различных символов
    if inputs[2].lower() == 'да':
        chars += digits
    if inputs[3].lower() == 'да':
        chars += lowercase_letters   
    if inputs[4].lower() == 'да':
        chars += uppercase_letters    
    if inputs[5].lower() == 'да':
        chars += punctuation 
    symbol = inputs[6]  # Исключать ли неоднозначные символы
  
    if chars == '':
        return None, None, None

    return quantity, length, chars, symbol

def generate_password(length, quantity, chars):
    passwords = []
    for _ in range(quantity):
        password = ''.join(random.choice(chars) for _ in range(length))
        passwords.append(password)
    return passwords

def restart(filename='input_data.txt'):
    inputs = get_input_from_file(filename)
    quantity, length, chars, symbol = data_collection(inputs)
    
    if chars:  # Если символы неправильные - не генерировать пароли
        passwords = generate_password(length, quantity, chars)
        return passwords
    return None

if __name__ == '__main__':
    print('Добро пожаловать в генератор паролей.Сейчас я сгенерирую пароли по параметрам, которые ты задал в файле input_data.txt.')
    passwords = restart()
    for password in passwords:
        print(password)
    print('Всегда рады Вам помочь! До свидания.')
