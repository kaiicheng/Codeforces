t = int(input())

for i in range(t):

    n = int(input())
    a = input().split()
    a = [int(i) for i in a]
    a.sort()

    ans = 0

    # gap = a[1] - a[0]
    for i in range(1, len(a)):
        # if a[i] - a[i - 1] == gap:
        ans += a[i] - a[i - 1]
    
    print(ans)