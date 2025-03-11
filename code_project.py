import random

# Строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def get_input_from_file():
    with open('input_data.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def data_collection(inputs):                             
    global quantity, lenght, symbol, chars
    chars = ''
    quantity = int(inputs[0)  # Количество паролей
    lenght = int(inputs[1])    # Длина пароля
    if quantity == 0 or lenght == 0:
        print('Неверное количество паролей или их длина!')
        return

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
        print('Вы неправильно сформировали запрос для пароля. Попробуйте еще раз!')
        return

def generate_password(lenght, quantity, chars):
    password = ''
    for i in range(quantity):
        num = lenght
        while num > 0:
            password += random.choice(chars)
            num -= 1
        if symbol.lower() == 'да':
            for c in 'il1Lo0O':
                chars = chars.replace(c, '')
        print(password)
        num = lenght
        password = ''

def restart():
    inputs = get_input_from_file()
    data_collection(inputs)
    if chars:  # Если символы неправильные - не генерировать пароли
        generate_password(lenght, quantity, chars)

print('Добро пожаловать в генератор паролей. Ответьте на несколько вопросов для создания пароля.')
restart()
print('Всегда рады Вам помочь! До свидания.')
