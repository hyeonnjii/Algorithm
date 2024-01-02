import sys

class Min_heap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return 0
        elif len(self.heap) == 1:
            return self.heap.pop()

        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        min_value = self.heap.pop()
        self.heapify_down(0)

        return min_value

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        while True:
            left_child_idx = index * 2 + 1
            right_child_idx = index * 2 + 2
            smallest = index

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest]:
                smallest = left_child_idx

            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest]:
                smallest = right_child_idx

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

min_heap = Min_heap()
N = int(sys.stdin.readline().strip())
print_values = []

for _ in range(N):
    i = int(sys.stdin.readline().strip())

    if i == 0:
        print_values.append(min_heap.pop())
    else:
        min_heap.push(i)

for value in print_values:
    sys.stdout.write(str(value) + '\n')
