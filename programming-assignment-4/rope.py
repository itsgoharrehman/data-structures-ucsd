# python3
import sys

sys.setrecursionlimit(400000)

class RopeNode:
    def __init__(self, char):
        self.char = char
        self.size = 1
        self.left = None
        self.right = None
        self.parent = None

def update(v):
    if v is None:
        return
    v.size = 1 + (v.left.size if v.left else 0) + (v.right.size if v.right else 0)
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

def find_by_index(node, index):
    """Finds the 0-based index element in implicit splay tree."""
    left_size = node.left.size if node.left else 0
    if index == left_size:
        return node
    elif index < left_size:
        return find_by_index(node.left, index)
    else:
        return find_by_index(node.right, index - left_size - 1)

def split(root, index):
    if root is None:
        return None, None
    if index <= 0:
        return None, root
    if index >= root.size:
        return root, None

    node = find_by_index(root, index)
    root = splay(node)
    
    left = root.left
    if left:
        left.parent = None
    root.left = None
    update(left)
    update(root)
    return left, root

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    node = find_by_index(left, left.size - 1)
    left = splay(node)
    left.right = right
    update(left)
    return left

def build_rope(s, l, r):
    if l > r:
        return None
    mid = (l + r) // 2
    node = RopeNode(s[mid])
    node.left = build_rope(s, l, mid - 1)
    node.right = build_rope(s, mid + 1, r)
    update(node)
    return node

class Rope:
    def __init__(self, s: str):
        self.root = build_rope(s, 0, len(s) - 1)

    def result(self) -> str:
        chars = []
        stack = []
        curr = self.root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            chars.append(curr.char)
            curr = curr.right
        return "".join(chars)

    def process(self, i: int, j: int, k: int):
        # Cut substring S[i...j]
        left, right = split(self.root, i)
        mid, right = split(right, j - i + 1)
        rest = merge(left, right)
        
        # Paste into position k of the remaining string
        rest1, rest2 = split(rest, k)
        self.root = merge(merge(rest1, mid), rest2)

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    
    rope = Rope(s)
    for line in input_data[2:2 + q]:
        i, j, k = map(int, line.split())
        rope.process(i, j, k)
        
    print(rope.result())

if __name__ == '__main__':
    main()