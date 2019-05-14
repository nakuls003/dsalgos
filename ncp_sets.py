n, m, d = map(int, input().split())
breaks = [int(num) for num in input().split()]
sb = set(breaks)
ans = {}
day, next_valid_minute = 1, 1
while len(ans) != n:
    i = next_valid_minute
    while i not in sb and i <= m:
        i += 1
    if i in sb:
        sb.remove(i)
        ans[i] = day
        next_valid_minute = i+d+1
    else:
        next_valid_minute = 1
        day += 1
print(day)
print(' '.join(str(ans[b]) for b in breaks))