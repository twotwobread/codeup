# n 열, 행의 개수 ( 2<=n<=100 )
# graph 높이 정보
import copy
def rangeRight(row, col):
    if row>=0 and row<n and col>=0 and col<n:
        return 1
    return 0

def dfs(row, col, standard):
    if rangeRight(row, col)==0:
        return
    if graph2[row][col]>standard:
        graph2[row][col]=0
        dfs(row, col+1, standard)
        dfs(row+1, col, standard)
        dfs(row, col-1, standard)
        dfs(row-1, col, standard)
        return True
    return False

n = int(input())
graph=[]
max_height=[]
for _ in range(n): # 높이 정보
    height=list(map(int, input().split()))
    graph.append(height)
    max_height.append(max(height))

result=[]
s = max(max_height)
for st in range(s+1):
    temp=0
    graph2 = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if dfs(i, j, st)==True:
                temp+=1
    result.append(temp) 
print(max(result))
