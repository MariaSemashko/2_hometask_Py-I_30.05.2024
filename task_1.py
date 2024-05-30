'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.'''

DIV_HEX = 16

original_num: int = int(input('Введите число: '))

result: str = ''
num = original_num
while num:
    if num % DIV_HEX == 10:
        result = 'a' + result
    elif num % DIV_HEX == 11:
        result = 'b' + result
    elif num % DIV_HEX == 12:
        result = 'c' + result
    elif num % DIV_HEX == 13:
        result = 'd' + result
    elif num % DIV_HEX == 14:
        result = 'e' + result
    elif num % DIV_HEX == 15:
        result = 'f' + result
    else:
        result = str(num % DIV_HEX) + result
    num //= DIV_HEX
print(f'В шестнадцатериччной системе число {original_num} представлено как {result} ')

if '0x' + result == hex(original_num):
    print('Все правильно')
else:
    print('Какая-то ошибка')