def solution(n, computers):
    visited = [False] * n
    network_count = 0

    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터가 있으면 새로운 네트워크
            dfs(i)
            network_count += 1  # 새로운 네트워크 카운트 증가

    return network_count