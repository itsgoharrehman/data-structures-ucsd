# python3
import sys

class DisjointSet:
    def __init__(self, row_counts: list[int]):
        self.parent = list(range(len(row_counts)))
        self.lines = list(row_counts)
        self.max_lines = max(row_counts) if row_counts else 0

    def get_parent(self, i: int) -> int:
        # Path Compression
        if i != self.parent[i]:
            self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]

    def merge(self, destination: int, source: int) -> int:
        real_dest = self.get_parent(destination)
        real_src = self.get_parent(source)

        if real_dest != real_src:
            # Merge source table into destination table
            self.parent[real_src] = real_dest
            self.lines[real_dest] += self.lines[real_src]
            self.lines[real_src] = 0
            self.max_lines = max(self.max_lines, self.lines[real_dest])

        return self.max_lines

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    row_counts = [int(x) for x in input_data[2:n + 2]]
    dsu = DisjointSet(row_counts)

    results = []
    idx = n + 2
    for _ in range(m):
        destination = int(input_data[idx]) - 1
        source = int(input_data[idx + 1]) - 1
        idx += 2
        results.append(str(dsu.merge(destination, source)))

    print('\n'.join(results))

if __name__ == "__main__":
    main()