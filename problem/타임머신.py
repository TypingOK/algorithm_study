import sys
INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
distance = [INF for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))


def bellman_ford(start):
    distance[start] = 0

    # 전체 v-1번을 반복
    for i in range(N):
        # 매 반복마다 모든 경로에 대해서
        for j in range(M):
            start_node = graph[j][0]
            end_node = graph[j][1]
            cost = graph[j][2]

            # 현재 저장된 값보다 cost로 더해준 값이 더 작다면
            if distance[start_node] != INF and distance[end_node] > distance[start_node] + cost:
                distance[end_node] = distance[start_node] + cost

                # N-1번 이후 음수 순환이 있는지 한번 더 돌려본 상태. 만약 여기서도 distance가 갱신된다면 음수 간선이 존재
                if i == N-1:
                    return True

    return False


negative = bellman_ford(1)

if negative:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)
