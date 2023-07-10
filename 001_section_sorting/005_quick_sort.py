# Сортировка Быстрая.
# Сложность O(n*log(n)).

"""
Quick Sort

>>> arr = [1, 2, 3, 4, 5]
>>> quick_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [5, 4, 3, 2, 1]
>>> quick_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [4, 2, 3, 4, 1]
>>> quick_sort(arr)
[1, 2, 3, 4, 4]

>>> arr = []
>>> quick_sort(arr)
[]

>>> arr = [9]
>>> quick_sort(arr)
[9]

>>> arr = [10000, 5000, 100000, 20000, 3000]
>>> quick_sort(arr)
[3000, 5000, 10000, 20000, 100000]

>>> arr = [-4, -2, -6, -1, -3]
>>> quick_sort(arr)
[-6, -4, -3, -2, -1]

"""
import doctest


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    central_point = arr[len(arr) // 2]
    left_part = []
    central_part = []
    right_part = []

    for x in arr:
        if x < central_point:
            left_part.append(x)
        elif x == central_point:
            central_part.append(x)
        else:
            right_part.append(x)

    return quick_sort(left_part) + central_part + quick_sort(right_part)


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
