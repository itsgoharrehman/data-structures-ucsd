# python3
import sys
from collections import deque

def max_sliding_window(sequence: list[int], m: int) -> list[int]:
    dq = deque()
    maximums = []
    
    for i, val in enumerate(sequence):
        # Remove elements outside current window
        if dq and dq[0] <= i - m:
            dq.popleft()
            
        # Remove smaller elements from back
        while dq and sequence[dq[-1]] <= val:
            dq.pop()
            
        dq.append(i)
        
        # Append max for valid window
        if i >= m - 1:
            maximums.append(sequence[dq[0]])
            
    return maximums

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    sequence = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    
    result = max_sliding_window(sequence, m)
    print(*result)

if __name__ == "__main__":
    main()