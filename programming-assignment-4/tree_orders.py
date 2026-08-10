# python3
import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

class TreeOrders:
    def read(self):
        input_data = sys.stdin.read().split()
        if not input_data:
            self.n = 0
            return
        self.n = int(input_data[0])
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n
        
        idx = 1
        for i in range(self.n):
            self.key[i] = int(input_data[idx])
            self.left[i] = int(input_data[idx + 1])
            self.right[i] = int(input_data[idx + 2])
            idx += 3

    def in_order(self):
        if self.n == 0:
            return []
        result = []
        stack = []
        curr = 0
        while curr != -1 or stack:
            while curr != -1:
                stack.append(curr)
                curr = self.left[curr]
            curr = stack.pop()
            result.append(self.key[curr])
            curr = self.right[curr]
        return result

    def pre_order(self):
        if self.n == 0:
            return []
        result = []
        stack = [0]
        while stack:
            node = stack.pop()
            if node == -1:
                continue
            result.append(self.key[node])
            if self.right[node] != -1:
                stack.append(self.right[node])
            if self.left[node] != -1:
                stack.append(self.left[node])
        return result

    def post_order(self):
        if self.n == 0:
            return []
        result = []
        stack1 = [0]
        stack2 = []
        while stack1:
            node = stack1.pop()
            if node == -1:
                continue
            stack2.append(node)
            if self.left[node] != -1:
                stack1.append(self.left[node])
            if self.right[node] != -1:
                stack1.append(self.right[node])
        while stack2:
            result.append(self.key[stack2.pop()])
        return result

def main():
    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
        return
    print(" ".join(map(str, tree.in_order())))
    print(" ".join(map(str, tree.pre_order())))
    print(" ".join(map(str, tree.post_order())))

if __name__ == '__main__':
    threading.Thread(target=main).start()