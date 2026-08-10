# python3
import sys

class StackWithMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value: int):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.stack.pop()
        self.max_stack.pop()

    def max(self) -> int:
        return self.max_stack[-1]

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    num_queries = int(input_data[0])
    stack = StackWithMax()
    results = []

    for i in range(1, num_queries + 1):
        query = input_data[i].split()
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            results.append(str(stack.max()))

    print('\n'.join(results))

if __name__ == "__main__":
    main()