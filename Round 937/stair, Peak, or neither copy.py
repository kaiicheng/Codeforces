t = int(input())

for i in range(t):

    n = input().split()
    a = [int(i) for i in n]
    # print("a: ", a)

    if a[0] < a[1] and a[1] < a[2]:
        print("STAIR")
    elif a[0] < a[1] and a[1] > a[2]:
        print("PEAK")
    else:
        print("NONE")
