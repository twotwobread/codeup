"""
memory test
"""

# n : 숫자, m : 질문
# a, b : a번째와 b번째 사이에 불렀던 수들의 합


    

result = []
n, m = map(int, input().split())
num = list(map(int, input().split()))
flag = [0] * n

count = 0
for n in num:
    flag[count] = n
    if count != 0:
        flag[count] += flag[count - 1]
    count+=1

count = 0
while count < m:
    m1, m2 = map(int, input().split())
    if m1 == m2:
        print(num[m1-1])
        count += 1
        continue
    elif m1 < m2:
        if m1 == 1:
            print(flag[m2-1])
            count+=1
            continue
        elif m1 > 1:
            print(flag[m2-1]-flag[m1-2])
            count+=1
            continue
        else:
            continue
    else:
        continue
        
