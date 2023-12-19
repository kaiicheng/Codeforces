
num = int(input())

for i in range(num):
    # print("-----start-----")
    n = int(input())
    x = [int(i) for i in input().split()]
    x.sort()
    # print(x)

    # single element case
    if (len(x)) <= 1:
        print(0)
    else:
        for i in range(n):
            gap = x[-1] - x[0]
        # print(gap)

        ans=[]

        while x[-1] != x[0]:
            if x[-1] % 2 == 1:
                ans.append(0)
                x[-1] = x[-1]//2
                x[0] = x[0]//2
            else:
                ans.append(1)
                x[-1] = (x[-1] + 1)//2
                x[0] = (x[0] + 1)//2

        if len(ans) > n:
            print(len(ans))
        else:
            print(len(ans))
            print(" ".join(str(val) for val in ans))

            # print(ans[i] for i in range(len(ans)))

        # print(ans)


        # else:
        #     print(gap)

        #     ans=[]
        #     for i in range(gap):
        #         ans.append(1)
        #         print(1, end=" ")
        #     print()