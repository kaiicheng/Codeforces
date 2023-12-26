from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    c = Counter(s)
    # print("c: ", c)

    di = dict(c)
    if "0" in di:
        zeros = di["0"]
    else:
        zeros = 0
    if "1" in di:
        ones = di["1"]
    else:
        ones = 0
    # print("zeros, ones: ", zeros, ones)

    if zeros > 0:
        print("YES")
    else:
        print("NO")



    # wrong

    # n_diff = 0
    # # n_same = 0
    # for i in range(len(s) - 1):
    #     if s[i] != s[i + 1]:
    #         n_diff += 1
    #     # if s[i] == s[i + 1]:
    #     #     n_same += 1
    # # print("n_diff: ", n_diff)
    # # print("n_same: ", n_same)

    # # TypeError: 'Counter' object is not callable
    # # zeros = c("0")
    # # ones = c("1")
    # di = dict(c)
    # # print("di: ", di)
    # if "0" in di:
    #     zeros = di["0"]
    # else:
    #     zeros = 0
    # if "1" in di:
    #     ones = di["1"]
    # else:
    #     ones = 0
    # # print("zeros, ones: ", zeros, ones)

    # if zeros + n_diff > ones:
    #     print("YES")
    # else:
    #     print("NO")