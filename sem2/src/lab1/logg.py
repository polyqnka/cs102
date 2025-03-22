import time

def logger(func):
    def wrap(*arg, **kwargs):
        start_time = time.time()
        result = func(*arg, **kwargs)
        end_time = time.time()

        print(f'Функция: {func.__name__}')
        print(f'Результат: {result}')
        print(f'Аргументы: {arg}')
        print(f'Время выполнения: {end_time - start_time:.6f} сек.')
        return result
    return wrap

@logger
def bubble_sort(arr):
    """Пузырьковая сортировка."""
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

bubble_sort([64, 34, 25, 12, 22, 11, 90])


