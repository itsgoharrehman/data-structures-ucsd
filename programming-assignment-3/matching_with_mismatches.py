# python3
import sys

class Solver:
    def __init__(self, k: int, text: str, pattern: str):
        self.k = k
        self.text = text
        self.pattern = pattern
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        
        self.ht1, self.ht2, self.pt1, self.pt2 = self._precompute(text)
        self.hp1, self.hp2, self.pp1, self.pp2 = self._precompute(pattern)

    def _precompute(self, s: str):
        n = len(s)
        h1, h2 = [0] * (n + 1), [0] * (n + 1)
        p1, p2 = [1] * (n + 1), [1] * (n + 1)
        for i in range(n):
            h1[i + 1] = (self.x * h1[i] + ord(s[i])) % self.m1
            h2[i + 1] = (self.x * h2[i] + ord(s[i])) % self.m2
            p1[i + 1] = (p1[i] * self.x) % self.m1
            p2[i + 1] = (p2[i] * self.x) % self.m2
        return h1, h2, p1, p2

    def _get_hash_t(self, start: int, length: int):
        hash1 = (self.ht1[start + length] - self.pt1[length] * self.ht1[start]) % self.m1
        hash2 = (self.ht2[start + length] - self.pt2[length] * self.ht2[start]) % self.m2
        return (hash1, hash2)

    def _get_hash_p(self, start: int, length: int):
        hash1 = (self.hp1[start + length] - self.pp1[length] * self.hp1[start]) % self.m1
        hash2 = (self.hp2[start + length] - self.pp2[length] * self.hp2[start]) % self.m2
        return (hash1, hash2)

    def count_mismatches(self, t_start: int) -> int:
        p_len = len(self.pattern)
        mismatches = 0
        off = 0
        
        while off < p_len and mismatches <= self.k:
            # Binary search for the longest matching segment starting at `off`
            low, high = 1, p_len - off
            match_len = 0
            
            while low <= high:
                mid = (low + high) // 2
                if self._get_hash_t(t_start + off, mid) == self._get_hash_p(off, mid):
                    match_len = mid
                    low = mid + 1
                else:
                    high = mid - 1
                    
            off += match_len
            if off < p_len:
                mismatches += 1
                off += 1  # Skip the mismatching character
                
        return mismatches

    def solve(self) -> list[int]:
        matches = []
        t_len = len(self.text)
        p_len = len(self.pattern)
        
        for i in range(t_len - p_len + 1):
            if self.count_mismatches(i) <= self.k:
                matches.append(i)
                
        return matches

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        k = int(parts[0])
        text = parts[1]
        pattern = parts[2]
        
        solver = Solver(k, text, pattern)
        matches = solver.solve()
        print(f"{len(matches)} " + " ".join(map(str, matches)))

if __name__ == '__main__':
    main()