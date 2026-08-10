# python3
import sys
import heapq

def assign_jobs(n_workers: int, jobs: list[int]):
    result = []
    # Min-Heap stores tuples: (next_free_time, worker_index)
    heap = [(0, i) for i in range(n_workers)]
    heapq.heapify(heap)

    for job_time in jobs:
        free_time, worker_idx = heapq.heappop(heap)
        result.append((worker_idx, free_time))
        heapq.heappush(heap, (free_time + job_time, worker_idx))

    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_workers = int(input_data[0])
    m_jobs = int(input_data[1])
    jobs = [int(x) for x in input_data[2:m_jobs + 2]]

    assigned_jobs = assign_jobs(n_workers, jobs)

    for worker_idx, start_time in assigned_jobs:
        print(f"{worker_idx} {start_time}")

if __name__ == "__main__":
    main()