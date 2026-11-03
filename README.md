<div align="center">
  <h1>data-structures-ucsd</h1>
  <p>Algorithmic implementations and coursework assignments for the Data Structures specialization by the University of California San Diego.</p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"></a>
    <img src="https://img.shields.io/badge/Institution-UC_San_Diego-182B49?style=flat-square&logo=coursera&logoColor=white" alt="UC San Diego">
    <img src="https://img.shields.io/badge/Language-Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Focus-Data_Structures_&_Algorithms-E34F26?style=flat-square&logo=thealgorithms&logoColor=white" alt="DSA">
    <a href="https://github.com/itsgoharrehman/data-structures-ucsd/stargazers"><img src="https://img.shields.io/github/stars/itsgoharrehman/data-structures-ucsd?style=flat-square&logo=github&logoColor=white" alt="Stars"></a>
    <a href="https://github.com/itsgoharrehman/data-structures-ucsd/issues"><img src="https://img.shields.io/github/issues/itsgoharrehman/data-structures-ucsd?style=flat-square&logo=github&logoColor=white" alt="Issues"></a>
  </p>
</div>

---

> [!IMPORTANT]
> **Academic Honesty and Institutional Integrity**:
> This repository contains completed algorithmic coursework for the University of California San Diego's **Data Structures** course (part of the Computer Science Data Structures & Algorithms Specialization). In accordance with UCSD's Policy on Integrity of Scholarship and the Coursera Honor Code, students currently enrolled in the course are strictly prohibited from copying, plagiarizing, or submitting any part of these solutions. This repository exists solely for code review, pedagogical reference, and portfolio demonstration.

---

## Core Data Structures & Asymptotic Complexity Matrix

The repository contains rigorous, benchmarked implementations satisfying strict time and memory execution limits:

| Module | Data Structure / Problem | Algorithm & Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Assignment 1** | Bracket Matching (`check_brackets.py`) | Stack-based syntax parsing | `O(n)` | `O(n)` |
| **Assignment 1** | Tree Height (`tree_height.py`) | Memoized depth traversal | `O(n)` | `O(n)` |
| **Assignment 1** | Network Packet Simulator (`process_packages.py`) | FIFO buffer queue | `O(n)` | `O(B)` |
| **Assignment 1** | Stack with Maximum (`stack_with_max.py`) | Auxiliary maximum tracker stack | `O(1)` per op | `O(n)` |
| **Assignment 1** | Max Sliding Window (`max_sliding_window.py`) | Monotonic double-ended queue | `O(n)` | `O(w)` |
| **Assignment 2** | Build Min-Heap (`build_heap.py`) | Bottom-up linear heap construction | `O(n)` | `O(1)` |
| **Assignment 2** | Parallel Job Queue (`job_queue.py`) | Binary min-heap priority scheduler | `O(m log n)` | `O(n)` |
| **Assignment 2** | Table Merging (`merging_tables.py`) | Disjoint-set union with rank & path compression | `O(m * alpha(n))` | `O(n)` |
| **Assignment 3** | Phone Book Direct Addressing (`phone_book.py`) | Hash map lookup | `O(1)` average | `O(n)` |
| **Assignment 3** | Chaining Hash Table (`hash_chains.py`) | Polynomial hashing with linked chains | `O(c + n/m)` | `O(m + n)` |
| **Assignment 3** | Rabin-Karp Substring Search (`hash_substring.py`) | Rolling polynomial hash matching | `O(|T| + |P|)` | `O(|T|)` |
| **Assignment 3** | Substring Equality & Common (`common_substring.py`) | Double rolling hash with binary search | `O((n + m) log(min(n, m)))` | `O(n + m)` |
| **Assignment 4** | Binary Tree Traversals (`tree_orders.py`) | In-order, pre-order, and post-order iterators | `O(n)` | `O(n)` |
| **Assignment 4** | BST Validation (`is_bst.py`, `is_bst_hard.py`) | In-order monotonicity and range bounds | `O(n)` | `O(h)` |
| **Assignment 4** | Range Sum Queries (`set_range_sum.py`) | Self-balancing Splay Tree with subtree sums | `O(log n)` amortized | `O(n)` |
| **Assignment 4** | Rope Data Structure (`rope.py`) | Tree-based string concatenation & substring cuts | `O(log n)` | `O(n)` |

---

## Directory Structure

```
data-structures-ucsd/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml              # Defect reporting form
│   │   └── question.yml                # Conceptual algorithm question form
│   ├── PULL_REQUEST_TEMPLATE.md        # Academic integrity verification checklist
│   └── dependabot.yml                  # Weekly automated pip dependency scanner
├── programming-assignment-1/           # Basic data structures (stacks, queues, trees)
├── programming-assignment-2/           # Priority queues and disjoint sets (heaps, DSU)
├── programming-assignment-3/           # Hash tables and polynomial rolling hashing
├── programming-assignment-4/           # Binary search trees and balanced Splay trees
├── requirements.txt                    # Testing and evaluation dependencies
├── LICENSE                             # MIT License
├── SECURITY.md                         # Security policy and academic disclosure protocol
├── CONTRIBUTING.md                     # Academic archive contribution guidelines
└── CODE_OF_CONDUCT.md                 # Contributor Covenant v2.1
```

---

## Running and Testing Locally

### Prerequisites

* Python 3.10 or higher
* `pytest` for running unit tests

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/itsgoharrehman/data-structures-ucsd.git
   cd data-structures-ucsd
   ```

2. Install test dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run an assignment solution against standard inputs:
   ```bash
   python programming-assignment-1/check_brackets.py
   python programming-assignment-2/build_heap.py
   python programming-assignment-4/tree_orders.py
   ```

---

## Academic Governance and Licensing

* **License**: Licensed under the terms of the [MIT License](LICENSE).
* **Security & Vulnerabilities**: Please review [SECURITY.md](SECURITY.md) for vulnerability reporting.
* **Academic Integrity**: See [CONTRIBUTING.md](CONTRIBUTING.md) regarding policy for completed coursework archives.
