# Структуры данных.
# Односвязный список.

"""
Linked list

Тестирование:
>>> linked_list = LinkedList()
>>> linked_list.append_elem(1)
>>> linked_list.append_elem(2)
>>> linked_list.append_elem(3)
>>> linked_list.display_list()
[1, 2, 3]

>>> linked_list.pre_pend_elem(0)
>>> linked_list.display_list()
[0, 1, 2, 3]

>>> linked_list.delete_elem(2)
>>> linked_list.display_list()
[0, 1, 3]
"""
import doctest


class NodeList:
    """Элемент односвязного списка."""
    def __init__(self, val_elem=0, next_elem=None):
        self.val_elem = val_elem
        self.next_elem = next_elem


class LinkedList:
    """Односвязный список."""
    def __init__(self):
        self.head_list = None

    def is_empty(self):
        """Проверка: пуст список или нет."""
        return self.head_list is None

    def append_elem(self, val_elem):
        """Добавление элемента к хвосту списка."""
        new_node = NodeList(val_elem)
        if self.head_list is None:
            self.head_list = new_node
        else:
            current = self.head_list
            while current.next_elem:
                current = current.next_elem
            current.next_elem = new_node

    def pre_pend_elem(self, val_elem):
        """Добавление элемента к голове списка."""
        new_node = NodeList(val_elem, self.head_list)
        self.head_list = new_node

    def delete_elem(self, val_elem):
        """Удаление конкретного элемента."""
        if self.head_list is None:
            return
        if self.head_list.val_elem == val_elem:
            self.head_list = self.head_list.next_elem
            return

        current = self.head_list
        while current.next_elem:
            if current.next_elem.val_elem == val_elem:
                current.next_elem = current.next_elem.next_elem
                return
            current = current.next_elem

    def display_list(self):
        """Показать список."""
        tmp_list = []
        current = self.head_list
        while current:
            tmp_list.append(current.val_elem)
            current = current.next_elem
        print(tmp_list)


if __name__ == '__main__':
    doctest.testmod()
    print('Тесты запущены!')
