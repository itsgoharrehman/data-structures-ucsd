# python3
import sys
import random

def poly_hash(s: str, prime: int, multiplier: int) -> int:
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans

def precompute_hashes(text: str, pattern_len: int, prime: int, multiplier: int) -> list[int]:
    t_len = len(text)
    H = [0] * (t_len - pattern_len + 1)
    
    # Hash of last window
    last_substring = text[t_len - pattern_len:]
    H[t_len - pattern_len] = poly_hash(last_substring, prime, multiplier)
    
    # Calculate multiplier^pattern_len % prime
    y = 1
    for _ in range(pattern_len):
        y = (y * multiplier) % prime
        
    for i in range(t_len - pattern_len - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime
        
    return H

def get_occurrences(pattern: str, text: str) -> list[int]:
    prime = 1000000007
    multiplier = random.randint(1, prime - 1)
    
    p_len = len(pattern)
    t_len = len(text)
    
    p_hash = poly_hash(pattern, prime, multiplier)
    H = precompute_hashes(text, p_len, prime, multiplier)
    
    result = []
    for i in range(t_len - p_len + 1):
        if H[i] != p_hash:
            continue
        if text[i:i + p_len] == pattern:
            result.append(i)
            
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    pattern, text = input_data[0], input_data[1]
    print(*(get_occurrences(pattern, text)))

if __name__ == '__main__':
    main()