N,M=map(int,input().split())
INF=int(1e9)
graph=[[INF] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j]==0

for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
X,K=map(int,input().split())
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
distance=graph[1][k]+graph[K][X]
if distance >= INF:
    print("무한")
else:
    print(distance)
