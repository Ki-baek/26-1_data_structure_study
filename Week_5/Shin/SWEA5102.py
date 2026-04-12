from collections import deque

T = int(input())


for t in range(T):
    node, E = map(int, input().split())
    arr = [[] for _ in range(node + 1)]

    for e in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())
    visited = set()
    connected = [0]
    cnt = [0]
    if S == G:
        cnt[0] = 1

    def bfs(cur):
        visited.add(cur)
        queue = deque([(cur, 0)])
        while queue:
            nxt, dist = queue.popleft()
            if nxt == G:
                cnt[0] = dist
                break
            for i in arr[nxt]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, dist + 1))

    bfs(S)

    print(f"#{t+1} {cnt[0]}")
