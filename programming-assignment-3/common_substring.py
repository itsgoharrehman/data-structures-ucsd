# python3
import sys

class Solver:
    def __init__(self, s: str, t: str):
        self.s = s
        self.t = t
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        
        self.hs1, self.hs2, self.ps1, self.ps2 = self._precompute(s)
        self.ht1, self.ht2, self.pt1, self.pt2 = self._precompute(t)

    def _precompute(self, string: str):
        n = len(string)
        h1, h2 = [0] * (n + 1), [0] * (n + 1)
        p1, p2 = [1] * (n + 1), [1] * (n + 1)
        for i in range(n):
            h1[i + 1] = (self.x * h1[i] + ord(string[i])) % self.m1
            h2[i + 1] = (self.x * h2[i] + ord(string[i])) % self.m2
            p1[i + 1] = (p1[i] * self.x) % self.m1
            p2[i + 1] = (p2[i] * self.x) % self.m2
        return h1, h2, p1, p2

    def _get_hash(self, h1, h2, p1, p2, start: int, length: int):
        hash1 = (h1[start + length] - p1[length] * h1[start]) % self.m1
        hash2 = (h2[start + length] - p2[length] * h2[start]) % self.m2
        return (hash1, hash2)

    def check(self, k: int):
        if k == 0:
            return 0, 0
        hashes_s = {}
        for i in range(len(self.s) - k + 1):
            h = self._get_hash(self.hs1, self.hs2, self.ps1, self.ps2, i, k)
            hashes_s[h] = i
            
        for j in range(len(self.t) - k + 1):
            h = self._get_hash(self.ht1, self.ht2, self.pt1, self.pt2, j, k)
            if h in hashes_s:
                return hashes_s[h], j
        return None

    def solve(self):
        low, high = 0, min(len(self.s), len(self.t))
        best_i, best_j, best_k = 0, 0, 0
        
        while low <= high:
            mid = (low + high) // 2
            res = self.check(mid)
            if res is not None:
                best_i, best_j, best_k = res[0], res[1], mid
                low = mid + 1
            else:
                high = mid - 1
                
        return best_i, best_j, best_k

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        s, t = parts[0], parts[1]
        solver = Solver(s, t)
        i, j, k = solver.solve()
        print(f"{i} {j} {k}")

if __name__ == '__main__':
    main()