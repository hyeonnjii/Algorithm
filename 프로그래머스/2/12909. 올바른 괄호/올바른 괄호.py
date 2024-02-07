def solution(s):
    answer = True
    left = 0
    right = 0
    flag = True
    
    for i in s:
        if i == '(':
            left += 1
        else:
            right += 1
        
        if left < right:
            flag = False
    
    if left == right and flag == True:
        return True
    
    return False