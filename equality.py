n, k = map(int, input().split())
s = input()

d = {chr(65+i):0 for i in range(k)}

for ch in s:
    d[ch] += 1

m = min(d.values())
print(k*m)