from collections import deque


n, k = map(int, input().split())


input_queue = deque(range(1, n+1))
output_queue = deque()



while len(input_queue) > 1 :
    input_queue.rotate(-(k - 1))
    i = input_queue.popleft()
    output_queue.append(i)



print('<', end='')

last = input_queue.popleft()
for i in output_queue:
    print(i, end=', ')

print(last, end= '>')