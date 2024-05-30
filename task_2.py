'''Напишите программу, которая принимает две строки вида “a/b” -
дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions'''

import fractions
import math

def get_fraction(user_fraction):
    sep_fraction = user_fraction.split('/')
    numerator = int(sep_fraction[0])
    denominator = int(sep_fraction[1])

    return numerator, denominator

fraction_1 = input('Введите первую дробь вида “a/b”: ')
fraction_2 = input('Введите вторую дробь вида “a/b”: ')

(numerator_1, denominator_1) = get_fraction(fraction_1)
(numerator_2, denominator_2) = get_fraction(fraction_2)

result_sum_denominator = int(math.lcm(denominator_1, denominator_2))
result_sum_numerator = int(numerator_1 * (result_sum_denominator /
                                      denominator_1) + numerator_2 * (result_sum_denominator / denominator_2))
if result_sum_numerator % result_sum_denominator == 0:
    result_sum = str(int(result_sum_numerator / result_sum_denominator))
else:
    result_sum_denominator_corr = int(result_sum_denominator/math.gcd(result_sum_numerator, result_sum_denominator))
    result_sum_numerator_corr = int(result_sum_numerator/math.gcd(result_sum_numerator, result_sum_denominator))
    result_sum = str(result_sum_numerator_corr) + '/' + str(result_sum_denominator_corr)

print(f'Сумма дробей равна {result_sum}')

result_prod_numerator = int((numerator_1 * numerator_2)/
                       math.gcd(numerator_1 * numerator_2, denominator_1 * denominator_2))
result_prod_denominator = int((denominator_1 * denominator_2)/
                         math.gcd(numerator_1 * numerator_2, denominator_1 * denominator_2))
if result_prod_numerator % result_prod_denominator == 0:
    result_prod = str(int(result_prod_numerator / result_prod_denominator))
else:
    result_prod = str(result_prod_numerator) + '/' + str(result_prod_denominator)

print(f'Произведение дробей равно {result_prod}')


f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)

if result_sum == str(f1 + f2) and result_prod == str(f1 * f2):
    print('Все правильно')
else:
    print('Какая-то ошибка')