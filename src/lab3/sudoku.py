"""
Этот модуль включает функции для чтения, отображения,
решения и генерации судоку.
"""

import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(file_path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """
    Читает судоку из указанного файла и возвращает его в виде двумерного списка.

    :param file_path: Путь к файлу с судоку.
    :return: Двумерный список, представляющий поле судоку.
    """
    path = pathlib.Path(file_path)
    with path.open() as file:
        puzzle_content = file.read()
    return create_grid(puzzle_content)


def create_grid(puzzle_string: str) -> tp.List[tp.List[str]]:
    """
    Преобразует строковое представление пазла в сетку 9x9.

    :param puzzle_string: Строка, представляющая пазл.
    :return: Двумерный список, представляющий сетку судоку.
    """
    digits = [char for char in puzzle_string if char in "123456789."]
    return group(digits, 9)


def display(grid: tp.List[tp.List[str]]) -> None:
    """
    Выводит судоку в читаемом формате 9x9 с разделителями для блоков 3x3.

    :param grid: Двумерный список, представляющий сетку судоку.
    """
    width = 3
    separator_line = "+-------+-------+-------"

    for row in range(9):
        print(" | ".join(
            " ".join(grid[row][col] if grid[row][col] != '.' else '.' for col in range(start, start + 3))
            for start in range(0, 9, 3)
        ))


        if row in [2, 5]:
            print(separator_line)

    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов.

    :param values: Список значений для группировки.
    :param n: Размер группы (количество элементов в каждой подсписке).
    :return: Список списков, где каждый подсписок содержит n элементов.
    """
    return [values[i:i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], position: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения для номера строки, указанной в position.

    :param grid: Двумерный список, представляющий сетку судоку.
    :param position: Кортеж (строка, колонка).
    :return: Список значений в указанной строке.
    """
    row, _ = position
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], position: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения для номера столбца, указанного в position.

    :param grid: Двумерный список, представляющий сетку судоку.
    :param position: Кортеж (строка, колонка).
    :return: Список значений в указанном столбце.
    """
    _, col = position
    return [grid[row][col] for row in range(9)]


def get_block(grid: tp.List[tp.List[str]], position: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения из квадрата 3x3, в который попадает позиция position.

    :param grid: Двумерный список, представляющий сетку судоку.
    :param position: Кортеж (строка, колонка).
    :return: Список значений в указанном 3x3 блоке.
    """
    row, col = position
    block_row_start = (row // 3) * 3
    block_col_start = (col // 3) * 3
    return [grid[r][c] for r in range(block_row_start, block_row_start + 3)
            for c in range(block_col_start, block_col_start + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """
    Находит первую свободную позицию в пазле.

    :param grid: Двумерный список, представляющий сетку судоку.
    :return: Кортеж с координатами пустой позиции (строка, колонка) или None, если пустых позиций нет.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '.':
                return (row, col)
    return None


def find_possible_values(grid: tp.List[tp.List[str]], position: tp.Tuple[int, int]) -> tp.Set[str]:
    """
    Возвращает множество возможных значений для указанной позиции.

    :param grid: Двумерный список, представляющий сетку судоку.
    :param position: Кортеж (строка, колонка).
    :return: Множество возможных значений для указанной позиции.
    """
    possible_values = set('123456789')
    row_values = set(get_row(grid, position))
    col_values = set(get_col(grid, position))
    block_values = set(get_block(grid, position))
    return possible_values - row_values - col_values - block_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """
    Решает пазл, заданный в grid.

    :param grid: Двумерный список, представляющий сетку судоку.
    :return: Решенная сетка судоку или None, если решение невозможно.
    """
    position = find_empty_positions(grid)
    if position is None:
        return grid

    row, col = position
    possible_values = find_possible_values(grid, position)

    for value in possible_values:
        grid[row][col] = value
        solution = solve(grid)

        if solution:
            return solution

        grid[row][col] = '.'

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """
    Проверяет, верно ли решение судоку.

    :param solution: Двумерный список, представляющий решенное поле судоку.
    :return: True, если решение верно, иначе False.
    """
    for row in range(9):
        if set(get_row(solution, (row, 0))) != set('123456789'):
            return False

    for col in range(9):
        if set(get_col(solution, (0, col))) != set('123456789'):
            return False

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            if set(get_block(solution, (block_row, block_col))) != set('123456789'):
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """
    Генерирует судоку, заполненное на N элементов.

    :param N: Количество заполненных элементов.
    :return: Сгенерированная сетка судоку.
    """
    grid = [['.'] * 9 for _ in range(9)]
    solve(grid)
    empty_positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(empty_positions)

    for _ in range(81 - N):
        row, col = empty_positions.pop()
        grid[row][col] = '.'

    return grid


if __name__ == "__main__":
    for filename in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(filename)
        display(grid)
        solution = solve(grid)

        if not solution:
            print(f"Пазл {filename} не может быть решен")
        else:
            display(solution)
