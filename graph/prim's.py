import heapq

N = int(input())
adj_matrix = [list(map(int, input().split())) for i in range(N)]
adj_list = {i:[] for i in range(N)}
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] != 0:
            adj_list[i].append([adj_matrix[i][j], j])

print(adj_list)
minH = [[0, 0]]
visited = set()
result = 0
while len(visited) < N:
    cost, i = heapq.heappop(minH)
    if i not in visited:
        print(cost)
        result += cost
        visited.add(i)
        for neiCost, nei in adj_list[i]:
            if nei not in visited:
                heapq.heappush(minH, [neiCost, nei])

print(result)