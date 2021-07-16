import copy
# 0이 꺼진 상태, 1이 켜진 상태
def rangeRight(row, col):
    if row>=0 and row<m and col>=0 and col<n:
        return 1
    return 0

def dfs(right, row, col, standard, other):
    if rangeRight(row, col)==0:
        return
    if right[row][col]==standard: #0이면
        right[row][col]=other
        dfs(right, row, col+1, standard, other)
        dfs(right, row-1, col, standard, other)
        dfs(right, row, col-1, standard, other)
        dfs(right, row+1, col, standard, other)
        return True
    return False
        


m, n = map(int, input().split()) # 세로길이, 가로길이 차례로
# 전구 상태
graph=[]
for _ in range(m):
    graph.append(list(map(int, input().split())))

graph2=copy.deepcopy(graph)
# 먼저 꺼진 상태에서 켜기위한 최소 횟수
result=0
for i in range(m):
    for j in range(n):
        if rangeRight(i, j)==1:
            if dfs(graph, i, j, 0, 1)==True:
                result+=1
result2=0
for i in range(m):
    for j in range(n):
        if rangeRight(i, j)==1:
            if dfs(graph2, i, j, 1, 0)==True:
                result2+=1
print(result, result2)
