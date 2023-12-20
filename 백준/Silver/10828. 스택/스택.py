import sys

def push(x):
    stack_list.append(x)

def pop():
    if len(stack_list) == 0:
        sys.stdout.write("-1\n")
    else:
        pop_int = stack_list.pop()
        sys.stdout.write(f"{pop_int}\n")

def size():
    print(len(stack_list))

def empty():
    if len(stack_list) == 0:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")

def top():
    if len(stack_list) == 0:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(f"{stack_list[-1]}\n")
        

stack_commands = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'top': top
}

stack_list = []
cnt = int(sys.stdin.readline().rstrip())
while cnt > 0:
    user_input = sys.stdin.readline().rstrip()
    command_parts = user_input.split(' ')
    command_name = command_parts[0]

    if command_name == 'push':
        x = int(command_parts[1])
        stack_commands[command_name](x)
    else:
        stack_commands[command_name]()
    cnt -= 1