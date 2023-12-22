from collections import deque

# Input: n, k
n, k = map(int, input().split())


# Initialize the input queue with numbers from 1 to n
input_queue = deque(range(1, n+1))

# Initialize an output queue to store the order of removed elements
output_queue = deque()



while len(input_queue) > 1 :
    # Rotate the input queue to make the (k-1)th element the first one
    input_queue.rotate(-(k - 1))

    # Remove and append the first element (k-1th element after rotation) to the output queue
    i = input_queue.popleft()
    output_queue.append(i)



print('<', end='')

last = input_queue.popleft()
for i in output_queue:
    print(i, end=', ')

print(last, end= '>')
