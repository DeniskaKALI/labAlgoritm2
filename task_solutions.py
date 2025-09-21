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

