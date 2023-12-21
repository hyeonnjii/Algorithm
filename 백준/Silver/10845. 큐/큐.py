from collections import deque
import sys

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if not queue:
        sys.stdout.write('-1\n')
    else:
        que_int = queue.popleft()
        sys.stdout.write('{}\n'.format(que_int))

def size():
    sys.stdout.write('{}\n'.format(len(queue)))

def empty():
    sys.stdout.write('{}\n'.format(1 if not queue else 0))

def front():
    sys.stdout.write('{}\n'.format(-1 if not queue else queue[0]))

def back():
    sys.stdout.write('{}\n'.format(-1 if not queue else queue[-1]))

functions = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

cnt = int(sys.stdin.readline().rstrip())
commands = [input().split() for _ in range(cnt)]

for command in commands:
    func = command[0]
    if func == 'push':
        i = command[1]
        functions[func](int(i))
    else:
        functions[func]()
