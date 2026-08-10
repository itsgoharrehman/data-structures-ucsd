# python3
import sys

class QueryProcessor:
    _prime = 1000000007
    _multiplier = 263

    def __init__(self, bucket_count: int):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s: str) -> int:
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def process_query(self, query: list[str]):
        cmd = query[0]
        
        if cmd == "check":
            i = int(query[1])
            return " ".join(self.buckets[i])
            
        string = query[1]
        bucket_idx = self._hash_func(string)
        chain = self.buckets[bucket_idx]

        if cmd == "add":
            if string not in chain:
                chain.insert(0, string)
        elif cmd == "del":
            if string in chain:
                chain.remove(string)
        elif cmd == "find":
            return "yes" if string in chain else "no"

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    bucket_count = int(input_data[0])
    n_queries = int(input_data[1])
    
    processor = QueryProcessor(bucket_count)
    results = []
    
    for i in range(2, n_queries + 2):
        res = processor.process_query(input_data[i].split())
        if res is not None:
            results.append(res)
            
    print('\n'.join(results))

if __name__ == '__main__':
    main()