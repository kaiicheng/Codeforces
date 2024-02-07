t = int(input())

for i in range(t):

    n = int(input())
    s = input()

    start = 0
    end = 0
    for i in range(n):
        # print("i: ", i)
        if s[i] == "B":
            start = i
            break

    for i in reversed(range(len(s))):
        # print("i: ", i)
        if s[i] == "B":
            end = i
            break

    # print("start, end: ", start, end)
    print(end - start + 1)