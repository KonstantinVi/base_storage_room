# Сортировка Слиянием.
# Сложность O(n*log(n)).

"""
Merge sort

>>> arr = [1, 2, 3, 4, 5]
>>> merge_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [5, 4, 3, 2, 1]
>>> merge_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [4, 2, 3, 4, 1]
>>> merge_sort(arr)
[1, 2, 3, 4, 4]

>>> arr = []
>>> merge_sort(arr)
[]

>>> arr = [9]
>>> merge_sort(arr)
[9]

>>> arr = [10000, 5000, 100000, 20000, 3000]
>>> merge_sort(arr)
[3000, 5000, 10000, 20000, 100000]

>>> arr = [-4, -2, -6, -1, -3]
>>> merge_sort(arr)
[-6, -4, -3, -2, -1]

"""
import doctest


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge(left_part, right_part)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
