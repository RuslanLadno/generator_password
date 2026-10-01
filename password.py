# Генератор безопасных паролей

# вводные данные
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'
chars = ''

# функция для генерации пароля
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

# вопросики
k_password = int(input('Сколько ты хочешь сделать паролей? (только целые числа)\n'))
password_len = int(input('Какая будет длина одного пароля? (только целые числа)\n'))
dig = input('Включать ли цифры 0123456789? (да/нет)\n')
upp_let = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет)\n')
low_let = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет)\n')
symbol = input('Включать ли символы !#$%&*+-=?@^_? (да/нет)\n')
iskl = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет)\n')

# куча проверок
if dig.lower() == 'да':
    chars += digits
if upp_let.lower() == 'да':
    chars += uppercase_letters
if low_let.lower() == 'да':
    chars += lowercase_letters
if symbol.lower() == 'да':
    chars += punctuation

if iskl.lower() == 'да':
    for i in ambiguous:
        chars = chars.replace(i, '')

if chars == '':
    print('Бро, так ты не сгенерируешь пароль, давай сначала')
else:
    for _ in range(k_password):
        print(generate_password(password_len, chars))


