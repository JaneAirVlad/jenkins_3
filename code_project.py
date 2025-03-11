import random

digits = '0123456789'                               # подключение строковых констант
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
                                          
def data_collection():                              # функция сбора условий генерации пароля
    global quantity, lenght, symbol, chars
    chars = ''                        
    quantity = int(input('Количестве паролей для генерации? (Целое число)\n'))
    lenght = int(input('Длина одного пароля? (Целое число)\n'))
    if quantity == 0 or lenght== 0:
        print('Неверное количество паролей или их длина!')
        restart()
    c = input('Включать ли цифры? (Да = включать, Нет = не включать)\n')
    if c.lower() == 'да':
        chars += digits
    d = input('Включать ли прописные буквы? (Да = включать, Нет = не включать)\n')
    if d.lower() == 'да':
        chars += lowercase_letters   
    e = input('Включать ли строчные буквы? (Да = включать, Нет = не включать)\n')
    if e.lower() == 'да':
        chars += uppercase_letters    
    f = input('Включать ли символы !#$%&*+-=?@^_? (Да = включать, Нет = не включать)\n')
    if f.lower() == 'да':
        chars += punctuation 
    symbol = input('Исключать ли неоднозначные символы il1Lo0O? (Да = исключать, Нет = не исключать)\n')
    if chars == '':
        print('Вы неправильно сформировали запрос для пароля. Попробуйте еще раз!')
        restart()

def generate_password(lenght, quantity, chars):         # функция генерации пароля
    password = ''
    for i in range(quantity):
        num = lenght
        while num > 0:
            password += random.choice(chars)
            num -= 1
        if symbol.lower() == 'да':                      # проверка на неоднозначные символы
            for c in 'il1Lo0O':
                chars = chars.replace(c, '')
        print(password)
        num = lenght
        password = ''

def restart():                                          # функция запуска кода и повтора
    again = 'да'
    while again.lower() == 'да':
        data_collection()
        generate_password(lenght, quantity, chars)    
        again = input('Вам еще нужны пароли ? (Да = запустить еще раз, Любая клавиша = выйти из программы) \n' )
        
print('Добро пожаловать в генератор паролей. Ответьте на несколько вопросов для создания пароля.')
restart()
print('Всегда рады Вам помочь! Досвидания.')
