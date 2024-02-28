# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]  # 인접 리스트를 초기화합니다.
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        self.answer = 0
        visited = [False for _ in range(n)]
        visited[0] = True
        self.dfs(0, graph, visited)
        return self.answer

    def dfs(self, index, graph, visited):
        for node, cost in graph[index]:
            if not visited[node]:
                visited[node] = True
                self.answer += cost
                self.dfs(node, graph, visited)
