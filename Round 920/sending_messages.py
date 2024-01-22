t = int(input())

for i in range(t):
    n, f, a, b = input().split(" ")
    n, f, a, b = int(n), int(f), int(a), int(b)
    # print("n, f, a, b: ", n, f, a, b)


    m = input().split(" ")
    m = [int(i) for i in m]
    m.insert(0, 0)
    # print("m: ", m)

    # exceed memory!
    # dp = [0 for i in range(int(m[-1]))]
    # dp[0] = f
    # print("dp: ", dp)

    cur_energy = f
    i = 0

    # insert 0 at the beginning!
    # pre = m[0]

    # while cur_energy > 0 and i < len(m):
    ans = True
    for i in range(1, n + 1):
        # print("i, n, cur_energy, a, b: ", i, n, cur_energy, a, b)

        off = b
        awake = (m[i] - m[i - 1]) * a
        # print("off, awake: ", off, awake)

        min_cost = min(off, awake)
        cur_energy -= min_cost
   
        if cur_energy <= 0:
            ans = False
            break
    
    if ans:
        print("YES")
    else:
        print("NO")
