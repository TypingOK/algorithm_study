def dfs(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered=dfs(w,discovered)
    return discovered
def dfs_stack(start_v):
    discovered=[]
    stack = [start_v]
    while stack:
        v=stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}

print(dfs(1))
print(dfs_stack(1))