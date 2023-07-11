# Структуры данных.
# Односвязный список.

"""
Linked list

Тестирование:
Двусвязный список
>>> doubl_linked_list = DoublLinkedList()
>>> doubl_linked_list.append_elem(1)
>>> doubl_linked_list.append_elem(2)
>>> doubl_linked_list.append_elem(3)
>>> doubl_linked_list.display_forward()
[1, 2, 3]

>>> doubl_linked_list.display_backward()
[3, 2, 1]

>>> doubl_linked_list.pre_pend_list(0)
>>> doubl_linked_list.display_forward()
[0, 1, 2, 3]

>>> doubl_linked_list.display_backward()
[3, 2, 1, 0]

>>> doubl_linked_list.delete(2)
>>> doubl_linked_list.display_forward()
[0, 1, 3]

>>> doubl_linked_list.display_backward()
[3, 1, 0]
"""
import doctest


class NodeList:
    def __init__(self, val_elem=0, prev_elem=None, next_elem=None):
        """Класс создание узла двусвязного списка.
        :arg val_elem: значение узла
        :arg prev_elem: указатель на предыдущий узел
        :arg next_elem: указатель на следующий узел
        """
        self.val_elem = val_elem
        self.prev_elem = prev_elem
        self.next_elem = next_elem


class DoublLinkedList:
    """Двусвязный список."""
    def __init__(self):
        self.head_list = None
        self.tail_list = None

    def is_empty(self):
        """Проверка: пуст список или нет."""
        return self.head_list is None

    def append_elem(self, val_elem):
        """Добавить элемент к хвосту списка."""
        new_node = NodeList(val_elem)
        if self.head_list is None:
            self.head_list = self.tail_list = new_node
        else:
            new_node.prev_elem = self.tail_list
            self.tail_list.next_elem = new_node
            self.tail_list = new_node

    def pre_pend_list(self, val_elem):
        """Добавить элемент к голове списка."""
        new_node = NodeList(val_elem, None, self.head_list)
        if self.head_list is None:
            self.head_list = self.tail_list = new_node
        else:
            self.head_list.prev_elem = new_node
            self.head_list = new_node

    def delete(self, val):
        """Удаление конкретного элемента."""
        if self.head_list is None:
            return
        current = self.head_list
        while current:
            if current.val_elem == val:
                if current.prev_elem:
                    current.prev_elem.next_elem = current.next_elem
                else:
                    self.head_list = current.next_elem

                if current.next_elem:
                    current.next_elem.prev_elem = current.prev_elem
                else:
                    self.tail_list = current.prev_elem
                return
            current = current.next_elem

    def display_forward(self):
        """Вывести связный список в прямом порядке."""
        elements = []
        current = self.head_list
        while current:
            elements.append(current.val_elem)
            current = current.next_elem
        print(elements)

    def display_backward(self):
        """Вывести связный список в обратном порядке."""
        elements = []
        current = self.tail_list
        while current:
            elements.append(current.val_elem)
            current = current.prev_elem
        print(elements)


if __name__ == '__main__':
    doctest.testmod()
    print('Тесты запущены!')
