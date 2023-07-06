# Сортировка Методом Пузырька.
# Сложность O(n^2).

"""Bubble sorting

>>> arr1 = [1, 2, 3, 4, 5]
>>> bubble_sort(arr1)
[1, 2, 3, 4, 5]

>>> arr2 = [5, 4, 3, 2, 1]
>>> bubble_sort(arr2)
[1, 2, 3, 4, 5]

>>> arr3 = [4, 2, 3, 4, 1]
>>> bubble_sort(arr3)
[1, 2, 3, 4, 4]

>>> arr4 = []
>>> bubble_sort(arr4)
[]

>>> arr5 = [9]
>>> bubble_sort(arr5)
[9]

>>> arr6 = [10000, 5000, 100000, 20000, 3000]
>>> bubble_sort(arr6)
[3000, 5000, 10000, 20000, 100000]

>>> arr7 = [-4, -2, -6, -1, -3]
>>> bubble_sort(arr7)
[-6, -4, -3, -2, -1]

"""
import doctest


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
