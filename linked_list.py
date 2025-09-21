# linked_list.py
# Реализация односвязного списка с комментариями по асимптотике

class Node:
    """Узел связного списка."""
    def __init__(self, data):
        self.data = data    # O(1) - присвоение значения
        self.next = None    # O(1) - инициализация ссылки


class LinkedList:
    """Простейший односвязный список."""
    def __init__(self):
        self.head = None    # O(1) - инициализация головы списка
        self.tail = None    # O(1) - инициализация хвоста (для оптимизации вставки в конец)

    def insert_at_start(self, data):
        """Вставка элемента в начало списка. Сложность: O(1)."""
        new_node = Node(data)       # O(1)
        new_node.next = self.head   # O(1)
        self.head = new_node        # O(1)
        if self.tail is None:       # O(1)
            self.tail = new_node    # O(1)

    def insert_at_end(self, data):
        """Вставка элемента в конец списка. Сложность: O(1) при наличии tail, иначе O(n)."""
        new_node = Node(data)       # O(1)
        if self.tail:               # O(1)
            self.tail.next = new_node  # O(1)
            self.tail = new_node       # O(1)
        else:
            self.head = new_node    # O(1)
            self.tail = new_node    # O(1)

    def delete_from_start(self):
        """Удаление элемента с начала списка. Сложность: O(1)."""
        if self.head:                  # O(1)
            self.head = self.head.next # O(1)
            if self.head is None:      # O(1)
                self.tail = None       # O(1)

    def traversal(self):
        """Обход списка. Сложность: O(n)."""
        elements = []             # O(1)
        current = self.head       # O(1)
        while current:            # O(n) - обход всех узлов
            elements.append(current.data)  # O(1)
            current = current.next         # O(1)
        return elements           # O(1)

# Общая сложность операций:
# insert_at_start – O(1)
# insert_at_end – O(1) с хвостом, иначе O(n)
# delete_from_start – O(1)
# traversal – O(n)
