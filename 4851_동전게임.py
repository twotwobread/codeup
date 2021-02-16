k = int(input()) # 라운드 수
c = int(input()) # 입력 개수
result = []

for i in range(c):
    m, n = map(int, input().split()) # 영희, 동수
    if m > n:
        if n+(k-(m-1)) >= m-1:
            result.append(1)
        else:
            result.append(0)
    elif n > m:
        if m+(k-(n-1)) > n-1:
            result.append(1)
        else:
            result.append(0)
    else:
        result.append(1)

for i in range(c):
    print(result[i])

            
