# performance_analysis.py
# Сравнительный анализ list, LinkedList и deque

import timeit
import collections
from linked_list import LinkedList


def measure_time(func, number=1000):
    """Измеряет время выполнения функции в миллисекундах."""
    return timeit.timeit(func, number=number) * 1000 / number


# 1. Сравнение вставки в начало: list vs LinkedList
def compare_list_vs_linkedlist():
    lst = []
    ll = LinkedList()

    list_time = measure_time(lambda: lst.insert(0, 1))
    ll_time = measure_time(lambda: ll.insert_at_start(1))

    print("Вставка в начало:")
    print(f"list.insert(0, item): {list_time:.6f} ms  (O(n))")
    print(f"LinkedList.insert_at_start: {ll_time:.6f} ms  (O(1))")


# 2. Сравнение очередей: list vs deque
def compare_list_vs_deque():
    from collections import deque
    N = 1000
    lst = [i for i in range(N)]
    dq = deque(range(N))

    list_time = measure_time(lambda: lst.pop(0))
    deque_time = measure_time(lambda: dq.popleft())

    print("\nУдаление из начала (очередь):")
    print(f"list.pop(0): {list_time:.6f} ms  (O(n))")
    print(f"deque.popleft(): {deque_time:.6f} ms  (O(1))")


if __name__ == "__main__":
    compare_list_vs_linkedlist()
    compare_list_vs_deque()
