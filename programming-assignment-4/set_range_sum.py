# python3
import sys

# Increase recursion depth for deep tree operations
sys.setrecursionlimit(200000)

class Vertex:
    def __init__(self, key, sum, left, right, parent):
        self.key = key
        self.sum = sum
        self.left = left
        self.right = right
        self.parent = parent

def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left else 0) + (v.right.sum if v.right else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v

def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        small_rotation(v.parent)
        small_rotation(v)
    else:
        small_rotation(v)
        small_rotation(v)

def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v

def find(root, key):
    v = root
    last = root
    next_node = None
    while v is not None:
        if v.key >= key and (next_node is None or v.key < next_node.key):
            next_node = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next_node, root)

def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

root = None

def insert(x):
    global root
    (left, right) = split(root, x)
    new_node = None
    if right is None or right.key != x:
        new_node = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_node), right)

def erase(x):
    global root
    (left, right) = split(root, x)
    (middle, right) = split(right, x + 1)
    root = merge(left, right)

def search(x):
    global root
    (node, root) = find(root, x)
    if node is not None and node.key == x:
        return True
    return False

def sum_range(fr, to):
    global root
    if fr > to:
        return 0
    (left, right) = split(root, fr)
    (middle, right) = split(right, to + 1)
    ans = middle.sum if middle is not None else 0
    root = merge(merge(left, middle), right)
    return ans

MODULO = 1000000001

def main():
    global root
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    last_sum_result = 0
    results = []

    for _ in range(n):
        type_ = input_data[idx]
        if type_ == '+':
            x = (int(input_data[idx + 1]) + last_sum_result) % MODULO
            insert(x)
            idx += 2
        elif type_ == '-':
            x = (int(input_data[idx + 1]) + last_sum_result) % MODULO
            erase(x)
            idx += 2
        elif type_ == '?':
            x = (int(input_data[idx + 1]) + last_sum_result) % MODULO
            results.append("Found" if search(x) else "Not found")
            idx += 2
        elif type_ == 's':
            l = (int(input_data[idx + 1]) + last_sum_result) % MODULO
            r = (int(input_data[idx + 2]) + last_sum_result) % MODULO
            res = sum_range(l, r)
            results.append(str(res))
            last_sum_result = res % MODULO
            idx += 3

    print('\n'.join(results))

if __name__ == '__main__':
    main()