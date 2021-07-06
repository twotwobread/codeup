"""
memory test 3
"""

# n개의 숫자를 먼저 말해준다.
# m개의 질문을 하면서 그 숫자를 몇 번째로 불렀는지 테스트
# n개의 데이터를 부를 때 오름차순으로 부른다.

# 1<=n<=1,000,000 , 1<=m<=100,000
# 질문은 오름차순 x, 없으면 -1 출력

def find_num(standard, num, start, end): # standard 0-9, num = 찾으려는 값, end, start 0-9
    #print(standard, num, start, end)
    if start > end:
        print(-1)
        return
    if n_num[standard] == num:
        print(standard+1)
        return
    elif n_num[standard] < num:
        find_num((standard+1+end)//2,num,standard+1, end)
    else:
        find_num((standard-1+start)//2,num,start, standard-1)

n = int(input())
n_num = list(map(int, input().split())) # 무조건 오름차순
m = int(input())
m_num = list(map(int, input().split())) # 얘는 오르차순 x

s=0; e=n-1
for i in range(m):
    #print("시작 : ", m_num[i])
    find_num((e+s)//2, m_num[i], s, e)
    
"""    
if start <= end:
        if n_num[standard] == num:
            print(standard + 1)
            return
        elif n_num[standard] > num:
            print("> in")
            print(standard, num, start, end)
            find_num((standard+start)//2, num, start, standard-1)
            return
        else:
            print("< in")
            print(standard, num, start, end)
            find_num((standard+end)//2, num, standard+1, end)
            return
    else:
        print(-1)
        return
"""
