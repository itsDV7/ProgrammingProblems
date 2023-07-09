def knapsack(values, weights, W):
    rate = list()
    for i, (vi, wi) in enumerate(zip(values, weights)):
        rate.append((vi/wi, i))
    rate.sort(reverse=True)
    loot = float(0)
    for r,i in rate:
        loot += r * min(weights[i], W)
        W -= min(weights[i], W)
        if not W:
            break
    return round(loot, 4)
if __name__ == "__main__":
    n, W = map(int, input().split())
    values = list()
    weights = list()
    for _ in range(n):
        vi, wi = map(int, input().split())
        values.append(vi)
        weights.append(wi)
    print(knapsack(values, weights, W))
