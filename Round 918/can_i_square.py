import math

t = int(input())

for i in range(t):

    n = input().split(" ")
    n = [int(i) for i in n]
    a = input().split(" ")
    a = [int(i) for i in a]
    # print("n: ", n)
    # print("a: ", a)

    total = sum(a)
    # print("total: ", total)

    ans = math.sqrt(total)
    # print("ans: ", ans)
    # print("total / ans: ", total / ans)
    if total // ans == total / ans:
        print("YES")
    else:
        print("NO")

    # ans = 1
    # while total < 0:
        