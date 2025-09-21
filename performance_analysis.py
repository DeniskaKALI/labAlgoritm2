import timeit
import matplotlib.pyplot as plt
from collections import deque
from linked_list import LinkedList


def measure_time(func, number=1000):
    return timeit.timeit(func, number=number) * 1000 / number


def benchmark_insert_start(max_size=5000, step=500):
    sizes = list(range(step, max_size + 1, step))
    list_times, ll_times = [], []

    for n in sizes:
        lst = []
        ll = LinkedList()

        def test_list():
            for i in range(n):
                lst.insert(0, i)

        def test_ll():
            for i in range(n):
                ll.insert_at_start(i)

        list_time = measure_time(test_list, number=1)
        ll_time = measure_time(test_ll, number=1)

        list_times.append(list_time)
        ll_times.append(ll_time)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_times, "r-o", label="list.insert(0, x)")
    plt.plot(sizes, ll_times, "g-o", label="LinkedList.insert_at_start")
    plt.xlabel("Количество вставок (N)")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Сравнение вставки в начало: list vs LinkedList")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("insert_start_comparison.png", dpi=300, bbox_inches="tight")
    plt.show()


