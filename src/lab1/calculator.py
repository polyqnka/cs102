"""
calculator.py

Примитивный калькулятор, состоящий из 4х базовых функций: сложение, вычитание, умножение и вычитание
"""

def add(first_arg, second_arg):
    """Функция сложения"""
    return first_arg + second_arg


def subtract(first_arg, second_arg):
    """Функция вычитания"""
    return first_arg - second_arg


def multiply(first_arg, second_arg):
    """Функция умножения"""
    return first_arg * second_arg


def divide(first_arg, second_arg):
    """Функция деления"""
    if second_arg == 0:
        return "Делить на ноль нельзя (пока :)))"
    return first_arg / second_arg


def run_calculator():
    """Функция для выполнения калькулятора с пользовательским вводом"""
    print("Добро пожаловать в калькулятор!")
    print("Выберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4): ")

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
            if next_calculation.lower() != "да":
                print("Спасибо за использование калькулятора! До свидания! <333")
                break
        else:
            print("Неправильный ввод. Пожалуйста, введите номер операции от 1 до 4 </3")

if __name__ == "__main__":
    run_calculator()