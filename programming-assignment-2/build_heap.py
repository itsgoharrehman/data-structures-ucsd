# python3
import sys

def build_heap(data: list[int]):
    swaps = []
    n = len(data)

    def sift_down(i: int):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left
        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    # Apply sift_down from the last non-leaf node up to root
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    data = [int(x) for x in input_data[1:n + 1]]

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()