# python3
import sys

class Solver:
    def __init__(self, s: str):
        self.s = s
        self.n = len(s)
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        
        self.h1 = [0] * (self.n + 1)
        self.h2 = [0] * (self.n + 1)
        self.p1 = [1] * (self.n + 1)
        self.p2 = [1] * (self.n + 1)
        
        for i in range(self.n):
            self.h1[i + 1] = (self.x * self.h1[i] + ord(s[i])) % self.m1
            self.h2[i + 1] = (self.x * self.h2[i] + ord(s[i])) % self.m2
            self.p1[i + 1] = (self.p1[i] * self.x) % self.m1
            self.p2[i + 1] = (self.p2[i] * self.x) % self.m2

    def ask(self, a: int, b: int, l: int) -> bool:
        hash1_a = (self.h1[a + l] - self.p1[l] * self.h1[a]) % self.m1
        hash1_b = (self.h1[b + l] - self.p1[l] * self.h1[b]) % self.m1
        if hash1_a != hash1_b:
            return False
            
        hash2_a = (self.h2[a + l] - self.p2[l] * self.h2[a]) % self.m2
        hash2_b = (self.h2[b + l] - self.p2[l] * self.h2[b]) % self.m2
        return hash2_a == hash2_b

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    
    solver = Solver(s)
    results = []
    idx = 2
    for _ in range(q):
        a, b, l = int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])
        idx += 3
        results.append("Yes" if solver.ask(a, b, l) else "No")
        
    print('\n'.join(results))

if __name__ == '__main__':
    main()