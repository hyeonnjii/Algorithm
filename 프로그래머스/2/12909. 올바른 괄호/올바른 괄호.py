def solution(s):
    slist = list()
    
    
    # stack 사용
    for i in s:
        if i == '(':
            slist.append(i)

        elif slist and i == ')':
                slist.pop()
        else:
            return False

    return len(slist) == 0
