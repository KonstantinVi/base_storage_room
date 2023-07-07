# Сортировка Методом Выбором.
# Сложность O(n^2).

"""Bubble sorting

>>> arr = [1, 2, 3, 4, 5]
>>> select_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [5, 4, 3, 2, 1]
>>> select_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [4, 2, 3, 4, 1]
>>> select_sort(arr)
[1, 2, 3, 4, 4]

>>> arr = []
>>> select_sort(arr)
[]

>>> arr = [9]
>>> select_sort(arr)
[9]

>>> arr = [10000, 5000, 100000, 20000, 3000]
>>> select_sort(arr)
[3000, 5000, 10000, 20000, 100000]

>>> arr = [-4, -2, -6, -1, -3]
>>> select_sort(arr)
[-6, -4, -3, -2, -1]

"""
import doctest


def select_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
