# Data Structures

This repository contains solutions to programming assignments for the **Data Structures** course (part of the Coursera Data Structures and Algorithms Specialization).

All implementations are written in **Python 3**.

---

## 📁 Repository Structure

```text
data-structures/
├── programming-assignment-1/
│   ├── check_brackets.py
│   ├── tree_height.py
│   ├── process_packages.py
│   ├── stack_with_max.py
│   └── max_sliding_window.py
├── programming-assignment-2/
│   ├── build_heap.py
│   ├── job_queue.py
│   └── merging_tables.py
├── programming-assignment-3/
│   ├── phone_book.py
│   ├── hash_chains.py
│   ├── hash_substring.py
│   ├── substr.py
│   ├── common_substring.py
│   └── matching_with_mismatches.py
└── programming-assignment-4/
    ├── tree_orders.py
    ├── is_bst.py
    ├── is_bst_hard.py
    ├── set_range_sum.py
    └── rope.py
```

---

## 💡 Assignments Overview

### 🔹 Programming Assignment 1: Basic Data Structures

| File | Description |
| :--- | :--- |
| [`check_brackets.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-1/check_brackets.py) | Validates matching brackets `()`, `[]`, `{}` in code and identifies the 1-based index of unmatched brackets. |
| [`tree_height.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-1/tree_height.py) | Computes the height of an arbitrary tree from parent node representation using BFS. |
| [`process_packages.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-1/process_packages.py) | Simulates a network packet processing buffer queue and outputs start times or dropped status (`-1`). |
| [`stack_with_max.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-1/stack_with_max.py) | Implements an extended Stack supporting $O(1)$ `max()` queries via auxiliary max tracking. |
| [`max_sliding_window.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-1/max_sliding_window.py) | Computes maximum values in sliding windows of size $k$ over an array in $O(N)$ time using a monotonic deque. |

---

### 🔹 Programming Assignment 2: Dynamic Arrays and Disjoint Sets

| File | Description |
| :--- | :--- |
| [`build_heap.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-2/build_heap.py) | Converts an unsorted array into a Min-Heap in $O(N)$ time using in-place bottom-up sifting down. |
| [`job_queue.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-2/job_queue.py) | Simulates parallel job processing across multiple threads using a Priority Queue (Min-Heap). |
| [`merging_tables.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-2/merging_tables.py) | Simulates database table merge queries while tracking maximum table size using Disjoint Set Union (DSU) with Path Compression. |

---

### 🔹 Programming Assignment 3: Hash Tables

| File | Description |
| :--- | :--- |
| [`phone_book.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-3/phone_book.py) | Implements a fast phone book contact search using direct addressing. |
| [`hash_chains.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-3/hash_chains.py) | Implements a hash table with chaining using polynomial hashing for string keys. |
| [`hash_substring.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-3/hash_substring.py) | Implements the Rabin-Karp algorithm for fast pattern searching in text using rolling hashes. |
| [`substr.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-3/substr.py) | Responds to $O(1)$ substring equality queries using double polynomial rolling hashes. |
| [`common_substring.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-3/common_substring.py) | Finds the longest common substring between two strings using binary search and double rolling hashes. |
| [`matching_with_mismatches.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-3/matching_with_mismatches.py) | Finds pattern occurrences allowing up to $k$ mismatches using double rolling hashes and binary search. |

---

### 🔹 Programming Assignment 4: Binary Search Trees & Self-Balancing Trees

| File | Description |
| :--- | :--- |
| [`tree_orders.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-4/tree_orders.py) | Computes In-Order, Pre-Order, and Post-Order traversals of a binary tree. |
| [`is_bst.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-4/is_bst.py) | Verifies if a given binary tree satisfies the Binary Search Tree (BST) property with distinct keys. |
| [`is_bst_hard.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-4/is_bst_hard.py) | Verifies if a binary tree satisfies the BST property allowing equal keys in the right subtrees. |
| [`set_range_sum.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-4/set_range_sum.py) | Implements a dynamic set data structure with range sum queries using Splay Trees. |
| [`rope.py`](file:///c:/Users/Gohar%20Rehman/Desktop/data-structures/programming-assignment-4/rope.py) | Implements a Rope data structure using an implicit Splay Tree to efficiently process string cut-and-paste queries. |

---

## 🚀 Usage

Run any script using Python 3 with input supplied via standard input (`stdin`):

```bash
python programming-assignment-4/tree_orders.py < input.txt
```

---

## 📜 Requirements

- Python `3.x`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
