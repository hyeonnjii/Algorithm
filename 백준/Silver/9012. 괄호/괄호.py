T =int(input())


for _ in range(T):
    vps_test = input()
    
    open_str = 0
    close_str = 0
    flag = 0
    
    vps_test = list(vps_test)
    
    for i in vps_test:
        if i == '(':
            open_str += 1
        else: 
            close_str += 1
        if open_str < close_str:
            flag = 1
    
    if (open_str == close_str) and flag == 0:
        print('YES')
    else:
        print('NO')