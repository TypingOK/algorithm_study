# https://leetcode.com/problems/number-of-provinces/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for _ in range(len(isConnected))]
        answer = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    answer += 1
                    self.dfs(visited, isConnected, i, 0)
        return answer

    def dfs(self, visited, isConnected, index, depth):
        if depth >= len(isConnected):
            return
        for i in range(len(isConnected[index])):
            if isConnected[index][i] == 1 and not visited[i]:
                visited[i] = True
                self.dfs(visited, isConnected,i,depth+1)