# 7x7 격자판
# 빨강=1, 노랑=2, 파랑=3, 초록=4, 보라=5
# 연속 3개 이상인 부분을 터치하면 터진다.
import copy
def rangeRight(row, col):
    if row>=0 and row<7 and col>=0 and col<7:
        return 1
    return 0
def dfs(row, col, standard, temp):
    if rangeRight(row, col)==0:
        return temp
    if graph[row][col]==standard:
        temp+=1
        graph[row][col]=0
        temp=dfs(row, col+1, standard, temp)
        temp=dfs(row-1, col, standard, temp)
        temp=dfs(row, col-1, standard, temp)
        temp=dfs(row+1, col, standard, temp)
        return temp
    return temp
        

graph=[]
for i in range(7):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(7):
    for j in range(7):
        temp=0
        if graph[i][j]!=0:
            if dfs(i, j, graph[i][j], temp)>=3:
                result+=1
print(result)
