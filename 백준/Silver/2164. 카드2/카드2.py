from collections import deque

def drop_card(queue):
    queue.popleft()

def move_card(queue):
    queue.append(queue.popleft())

N = int(input())

queue = deque(range(1, N+1))

i = 1
while len(queue) > 1:
    if (i) % 2 != 0:
        drop_card(queue)
    else:
        move_card(queue)

    i += 1

print(queue[0])   