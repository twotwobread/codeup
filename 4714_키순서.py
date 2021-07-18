# n 학생들의 수 ( 2<=n<= 500 )
# m  두 학생 키를 비교한 횟수 ( 0<=m<=n(n-1)/2 )
# a, b 두 학생 키를 비교한 결과 a < b

def dfs(info, num):
    if len(info[num])==0:
        return
    visited[num]=True
    for c in info[num]:
        if visited[c]==False:
            visited[c]=True
            dfs(info, c)

n, m = map(int, input().split())
student = [[] for _ in range(n+1)] # 아래 트리(자식) 탐색을 하기 위함
reverse_student=[[] for _ in range(n+1)] # 위 트리(부모) 탐색을 하기 위함
for _ in range(m):
    a, b = map(int, input().split())
    student[a].append(b)
    reverse_student[b].append(a)


result=0
for i in range(1, n+1):
    visited = [False]*(n+1)
    visited[0]=True
    dfs(student, i)
    dfs(reverse_student, i)
    if (False in visited)==False:
        result+=1
    
print(result)
