# Сортировка Методом Вставок.
# Сложность O(n^2).

"""
Insertion sorting

>>> arr = [1, 2, 3, 4, 5]
>>> insertion_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [5, 4, 3, 2, 1]
>>> insertion_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [4, 2, 3, 4, 1]
>>> insertion_sort(arr)
[1, 2, 3, 4, 4]

>>> arr = []
>>> insertion_sort(arr)
[]

>>> arr = [9]
>>> insertion_sort(arr)
[9]

>>> arr = [10000, 5000, 100000, 20000, 3000]
>>> insertion_sort(arr)
[3000, 5000, 10000, 20000, 100000]

>>> arr = [-4, -2, -6, -1, -3]
>>> insertion_sort(arr)
[-6, -4, -3, -2, -1]

"""
import doctest


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
