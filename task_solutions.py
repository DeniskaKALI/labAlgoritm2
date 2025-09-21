from collections import deque


def check_brackets(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


def printer_queue(jobs):
    queue = deque(jobs)
    result = []
    while queue:
        job = queue.popleft()
        result.append(job)
    return result


def is_palindrome(s: str) -> bool:
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == "__main__":
    print("Сбалансированные скобки:")
    print(check_brackets("{[()]}"))
    print(check_brackets("{[(])}"))

    print("\nОчередь печати:")
    print(printer_queue(["doc1", "doc2", "doc3"]))

    print("\nПроверка палиндрома:")
    print(is_palindrome("radar"))
    print(is_palindrome("hello"))
