def signatures(lines):
    sort_lines = sorted(lines)
    include = [0]*len(lines)
    ans = list()
    for i,k in enumerate(sort_lines):
        v = lines[k]
        if not include[i]:
            currmin = min(v)
            include[i] = 1
            for j,key in enumerate(sort_lines):
                val = lines[key]
                if not include[j]:
                    nextmin = min(val)
                    if key <= currmin <= nextmin:
                        include[j] = 1
                        continue
                    if nextmin > currmin:
                        break
                    currmin = nextmin
                    include[j] = 1
            ans.append(currmin)
    return ans
if __name__ == "__main__":
    n = int(input())
    lines = dict()
    for _ in range(n):
        x, y = map(int, input().split())
        if x in lines:
            lines[x].append(y)
        else:
            lines[x] = [y]
    ans = signatures(lines)
    print(len(ans))
    print(*ans)
