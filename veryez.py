import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    N = next(it); M = next(it); Q = next(it); K = next(it)
    c = [[next(it) for _ in range(M)] for _ in range(N)]
    a = [[next(it) for _ in range(M)] for _ in range(M)]
    adj = [[v for v in range(M) if a[u][v] == 1] for u in range(M)]


    full_masks = 1 << M
    popc = [i.bit_count() for i in range(full_masks)]

    INF = 10**30
    dp_prev = [dict() for _ in range(M)]
    for j in range(M):
        dp_prev[j][1 << j] = c[0][j]

    for i in range(1, N):
        dp_next = [dict() for _ in range(M)]
        row = c[i]
        for u in range(M):
            dpu = dp_prev[u]
            if not dpu:
                continue
            cost_add_base = None
            for mask, cost in dpu.items():
            
                for v in adj[u]:
                    newmask = mask | (1 << v)
                    newcost = cost + row[v] + K * abs(u - v)
                    prev = dp_next[v].get(newmask)
                    if prev is None or newcost < prev:
                        dp_next[v][newmask] = newcost
        dp_prev = dp_next

    ans = INF
    for u in range(M):
        for mask, cost in dp_prev[u].items():
            if popc[mask] >= Q and cost < ans:
                ans = cost
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()
