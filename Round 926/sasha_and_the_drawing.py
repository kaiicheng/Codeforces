t = int(input())

for i in range(t):

    l = input().split()
    n = int(l[0])
    k = int(l[1])

    # print("n, k: ", n, k)

    diag = 4 * n - 2

    if k % 2 == 0:
        x = k // 2
        rest = 0
    
    elif k % 2 == 1:
        x = (k - 1) // 2
        rest = 1
    if k == diag:
        ans = n * 2
    else:
        ans = x + rest
    print(ans)