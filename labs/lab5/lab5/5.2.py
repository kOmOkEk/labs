ls = list(map(str, input().split()))

for i in range(0, len(ls) - 1):
    if ls[i] == ls[i + 1]:
        k = ls[i]

print(k)