n = int(input())

for i in range(n):
    s = input().split(" ")
    s = [int(x) for x in s]
    print(max(s))

    # print(int(max(s)))
    # if s[0] == s[1]:
    #     print(s[0])
    # else:
    #     mi = min(s[0], s[1])
    #     mi += int(max(s[0], s[1])) - mi
    #     print(mi)
