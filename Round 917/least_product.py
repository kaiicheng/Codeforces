t = int(input())

for i in range(t):

    n = int(input())
    # print("n: ", n)

    a = input().split(" ")
    # print("a: ", a)

    # total = 1
    # for j in range(len(a)):
    #     total *= int(a[j])
    # print("total: ", total)

    total = 1
    n_neg = 0
    n_zero = 0
    for j in range(len(a)):
        if int(a[j]) < 0:
            n_neg += 1
        elif int(a[j]) == 0:
            n_zero += 1
        total *= int(a[j])

    # print("total: ", total)
    # print("n_neg: ", n_neg)
    # print("n_zero: ", n_zero)

    # print("---ans below---")
    n_oper = 0
    oper = []
    if n_zero > 0:
        print(int(0))
    else:
        if n_neg == 0:
            n_oper += 1
            oper.append(["1", "0"])
            print(n_oper)
            print(" ".join(oper[0]))
        else:
            if n_neg % 2 == 0:
                # mx = max(a)
                # print("max: ", mx)
                # removed = a.pop(a.index(mx))
                # print("a, removed: ", a, removed)
                n_oper += 1
                oper.append(["1", "0"])
                print(n_oper)
                print(" ".join(oper[0]))
            else:
                # print("total: ", total)
                print(n_oper)
    # print("---end---")
