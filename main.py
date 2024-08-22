# -*- coding: utf8 -*-
'''
Автор: cryptocoding
Дата создания: 22.08.2024
Описание: Данный модуль создан для рассчета индекса массы тела
'''


def calculate_bmi(weight: float, height: float) -> float:
    '''
    Функция для расчета индекса массыл тела.
    Args:
        weight (float): Вес тела
        height (float): Рост

    Returns:
        float: Индекс массы тела
    '''

    return weight / (height ** 2)


def main():
    '''
    Основная функция для расчета индекса массы тела.
    '''

    weight = float(input('Введите ваш вес (в килограммах): '))
    height = float(input('Введите ваш рост (в метрах): '))

    bmi = calculate_bmi(weight, height)

    print(f'Ваш индекс массы тела (BMI): {bmi:.2f}')

    if bmi < 18.5:
        print('Недостаточный вес')
    elif 18.5 <= bmi < 24.9:
        print('Нормальный вес')
    elif 25 <= bmi < 29.9:
        print('Избыточный вес')
    else:
        print('Ожирение')


if __name__ == '__main__':
    main()
