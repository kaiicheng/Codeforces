# dictionary has order

from collections import Counter

n = int(input())

for i in range(n):
    n = int(input())
    s = input()
    c = Counter(s)
    # print("n, c: ", n, c)

    # print(ord("a"))  # 97
    # print(ord("A"))  # 65
    # print(ord("B"))  # 66
    # print(ord("Z"))  # 90

    ans = 0
    for i in c:
        # print("i, c[i]: ", i, c[i])
        if ord(i) - 64 <= c[i]:
            ans += 1
    print(ans)
    