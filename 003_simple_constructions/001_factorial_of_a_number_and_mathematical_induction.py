# Факториал числа | n! = n * (n - 1)!
# Математическая индукция | (n * (n + 1)) / 2

"""
Tests
>>> factorial_search(0)
1

>>> factorial_search(1)
1

>>> factorial_search(5)
120

>>> factorial_search(10)
3628800

>>> mathematic_induction(0)
0

>>> mathematic_induction(5)
15

>>> mathematic_induction(10)
55

"""
import doctest


def factorial_search(n):
    """Поиск факториала числа."""
    if n <= 1:
        return 1
    return n * factorial_search(n - 1)


def mathematic_induction(n):
    """Математическая индукция."""
    tmp_val = int(n * (n + 1) / 2)
    return tmp_val


if __name__ == '__main__':
    doctest.testmod()
    print('Все тесты запустились!')
