def solution(s):
    slist = list()
    
    
    # stack 사용
    for i in s:
        if i == '(':
            slist.append(i)

        if i == ')':
            try:
                slist.pop()
            except IndexError:
                return False

    return len(slist) == 0
