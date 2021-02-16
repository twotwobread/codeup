N = int(input())
A, B = map(int, input().split())
C = int(input())
D = []
for i in range(N):
    D.append(int(input()))
D.sort(reverse=True)
for t in D:
    C_rate = C/A
    D_rate = t/B
    #print(C_rate, D_rate)
    if  C_rate < D_rate:
        C +=t; A+=B;
        result = C//A
        #print("result = ", result)
    else:
        continue
print(result)
