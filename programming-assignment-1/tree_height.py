# python3
import sys
from collections import deque

def compute_height(n: int, parents: list[int]) -> int:
    children = [[] for _ in range(n)]
    root = -1
    
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            children[parent].append(child)
            
    # BFS to measure max tree depth
    queue = deque([(root, 1)])
    max_height = 0
    
    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)
        for child in children[node]:
            queue.append((child, height + 1))
            
    return max_height

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    parents = list(map(int, input_data[1:]))
    print(compute_height(n, parents))

if __name__ == "__main__":
    main()