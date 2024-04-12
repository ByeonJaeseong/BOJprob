def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    lst = list(s)
    if lst[0] == ')' : return False
    count1 = 1
    for i in range(1,len(lst)):
        if lst[i] == ')':
            count1-=1
        else : count1+=1
        if count1<0:return False
    if count1 == 0: return True
    else: return False
    
    

    return True

