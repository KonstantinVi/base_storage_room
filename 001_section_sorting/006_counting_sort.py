# Сортировка Методом Подсчёта.
# Сложность O(n).

"""
Bubble sorting

>>> arr = [1, 2, 3, 4, 5]
>>> counting_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [5, 4, 3, 2, 1]
>>> counting_sort(arr)
[1, 2, 3, 4, 5]

>>> arr = [4, 2, 3, 4, 1]
>>> counting_sort(arr)
[1, 2, 3, 4, 4]

>>> arr = []
>>> counting_sort(arr)
[]

>>> arr = [9]
>>> counting_sort(arr)
[9]

>>> arr = [10000, 5000, 100000, 20000, 3000]
>>> counting_sort(arr)
[3000, 5000, 10000, 20000, 100000]

>>> arr = [-4, -2, -6, -1, -3]
>>> counting_sort(arr)
[-6, -4, -3, -2, -1]

"""
import doctest



def counting_sort(arr):
    """Сортировка подсчётом."""
    if len(arr) <= 1:
        return arr
    maximum_val = max(arr)
    minimal_value = min(arr)

    dict_count_element = {i: 0 for i in range(minimal_value, maximum_val + 1)}

    for num in arr:
        dict_count_element[num] += 1

    sorted_arr = []
    for key, val in dict_count_element.items():
        sorted_arr.extend([key] * val)

    return sorted_arr


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
