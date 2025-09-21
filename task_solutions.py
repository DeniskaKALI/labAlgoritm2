# task_solutions.py
# Решение практических задач с использованием подходящих структур данных

from collections import deque


# 1. Проверка сбалансированности скобок
def check_brackets(s: str) -> bool:
    """
    Использует стек (list). Сложность: O(n).
    """
    stack = []  # O(1)
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:             # O(n)
        if ch in "([{":
            stack.append(ch)  # O(1)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()       # O(1)
    return not stack          # O(1)


# 2. Симуляция очереди печати
def printer_queue(jobs):
    """
    Использует очередь (deque). Сложность: O(n).
    """
    queue = deque(jobs)     # O(n)
    result = []
    while queue:            # O(n)
        job = queue.popleft()  # O(1)
        result.append(job)     # O(1)
    return result


# 3. Проверка палиндрома
def is_palindrome(s: str) -> bool:
    """
    Использует deque. Сложность: O(n).
    """
    dq = deque(s)             # O(n)
    while len(dq) > 1:        # O(n/2) ≈ O(n)
        if dq.popleft() != dq.pop():  # O(1)
            return False
    return True


if __name__ == "__main__":
    print("Сбалансированные скобки:")
    print(check_brackets("{[()]}"))  # True
    print(check_brackets("{[(])}"))  # False

    print("\nОчередь печати:")
    print(printer_queue(["doc1", "doc2", "doc3"]))

    print("\nПроверка палиндрома:")
    print(is_palindrome("radar"))   # True
    print(is_palindrome("hello"))   # False
