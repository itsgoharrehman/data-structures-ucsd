# python3
import sys
from collections import deque

class Buffer:
    def __init__(self, size: int):
        self.size = size
        self.finish_times = deque()

    def process(self, arrival_time: int, process_time: int) -> int:
        # Remove packets that finish before or at current packet arrival
        while self.finish_times and self.finish_times[0] <= arrival_time:
            self.finish_times.popleft()

        # Drop packet if buffer is full
        if len(self.finish_times) >= self.size:
            return -1

        # Calculate start time
        if not self.finish_times:
            start_time = arrival_time
        else:
            start_time = self.finish_times[-1]

        finish_time = start_time + process_time
        self.finish_times.append(finish_time)
        return start_time

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    size, n = int(input_data[0]), int(input_data[1])
    buffer = Buffer(size)
    
    idx = 2
    responses = []
    for _ in range(n):
        arrival_time = int(input_data[idx])
        process_time = int(input_data[idx + 1])
        idx += 2
        responses.append(buffer.process(arrival_time, process_time))

    print('\n'.join(map(str, responses)))

if __name__ == "__main__":
    main()