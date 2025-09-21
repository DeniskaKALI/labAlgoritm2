# performance_analysis.py
# Сравнительный анализ list, LinkedList и deque с графиками

import timeit
from linked_list import LinkedList
from collections import deque
import matplotlib.pyplot as plt

def measure_time(func, number=1000):
    """Измеряет время выполнения функции в миллисекундах."""
    return timeit.timeit(func, number=number) * 1000 / number

def system_info():
    """Вывод характеристик ПК в заданном формате."""
    pc_info = """ 
Характеристики ПК для тестирования: 
- Процессор: Intel Core i7-10750H @ 2.60GHz
- Оперативная память: 16 GB DDR4
- ОС: Windows 11
- Python: 3.9.7
"""
    print(pc_info)

def compare_list_vs_linkedlist_insert(N=1000):
    """Сравнение вставки в начало и конец: list vs LinkedList с построением графиков."""
    lst_start_times, ll_start_times = [], []
    lst_end_times, ll_end_times = [], []

    lst, ll = [], LinkedList()

    for i in range(N):
        # Вставка в начало
        lst_start_times.append(measure_time(lambda i=i: lst.insert(0, i)))
        ll_start_times.append(measure_time(lambda i=i: ll.insert_at_start(i)))
        # Вставка в конец
        lst_end_times.append(measure_time(lambda i=i: lst.append(i)))
        ll_end_times.append(measure_time(lambda i=i: ll.insert_at_end(i)))

    # Построение графиков вставки
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(lst_start_times, label="list.insert(0, item)")
    plt.plot(ll_start_times, label="LinkedList.insert_at_start")
    plt.title("Вставка в начало")
    plt.xlabel("Итерация")
    plt.ylabel("Время (ms)")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(lst_end_times, label="list.append(item)")
    plt.plot(ll_end_times, label="LinkedList.insert_at_end")
    plt.title("Вставка в конец")
    plt.xlabel("Итерация")
    plt.ylabel("Время (ms)")
    plt.legend()

    plt.tight_layout()
    plt.show()

    print("Анализ вставки:")
    print("list.insert(0, item) растет линейно, так как элементы смещаются (O(n)).")
    print("LinkedList.insert_at_start выполняется за постоянное время O(1).")
    print("list.append(item) амортизированно O(1), LinkedList.insert_at_end O(1) с tail.")
    print("-" * 40)

def compare_list_vs_deque_queue(N=1000):
    """Сравнение операций очереди: list.pop(0) vs deque.popleft() с графиком."""
    lst = [i for i in range(N)]
    dq = deque(range(N))

    lst_times, dq_times = [], []

    for _ in range(100):
        lst_times.append(measure_time(lambda: lst.pop(0)))
        dq_times.append(measure_time(lambda: dq.popleft()))

    plt.figure(figsize=(6, 5))
    plt.plot(lst_times, label="list.pop(0)")
    plt.plot(dq_times, label="deque.popleft()")
    plt.title("Удаление из начала (очередь)")
    plt.xlabel("Итерация")
    plt.ylabel("Время (ms)")
    plt.legend()
    plt.show()

    print("Анализ очереди:")
    print("list.pop(0) растет линейно (O(n)), так как нужно смещать элементы.")
    print("deque.popleft() выполняется за постоянное время O(1).")
    print("-" * 40)

if __name__ == "__main__":
    system_info()
    compare_list_vs_linkedlist_insert()
    compare_list_vs_deque_queue()
