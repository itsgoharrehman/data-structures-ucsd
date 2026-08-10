# python3
import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

def is_bst_hard(keys, left, right):
    n = len(keys)
    if n == 0:
        return True

    stack = [(0, -float('inf'), float('inf'))]
    while stack:
        node, min_key, max_key = stack.pop()
        if node == -1:
            continue
        key = keys[node]
        if key < min_key or key >= max_key:
            return False
        if right[node] != -1:
            stack.append((right[node], key, max_key))
        if left[node] != -1:
            stack.append((left[node], min_key, key))

    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        print("CORRECT")
        return

    n = int(input_data[0])
    if n == 0:
        print("CORRECT")
        return

    keys = [0] * n
    left = [0] * n
    right = [0] * n

    idx = 1
    for i in range(n):
        keys[i] = int(input_data[idx])
        left[i] = int(input_data[idx + 1])
        right[i] = int(input_data[idx + 2])
        idx += 3

    if is_bst_hard(keys, left, right):
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == '__main__':
    threading.Thread(target=main).start()