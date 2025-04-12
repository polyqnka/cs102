"""
test_calculator.py базовые тесты для примитивного калькулятора calculator.py
"""
import unittest
from src.lab1.calculator import add, subtract, multiply, divide

def test_add():
    """Проверяем, что функция сложения возвращает правильный результат"""
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    """Проверяем, что функция вычитания возвращает правильный результат"""
    assert subtract(4, 2) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0

def test_multiply():
    """Проверяем, что функция умножения возвращает правильный результат"""
    assert multiply(3, 3) == 9
    assert multiply(0, 10) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """Проверяем, что функция деления возвращает правильный результат"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(0, 1) == 0

def test_divide_by_zero():
    """Проверяем, что функция деления на ноль возвращает правильное сообщение"""
    assert divide(10, 0) == "Делить на ноль нельзя (пока :)))"


if __name__ == '__main__':
    unittest.main()