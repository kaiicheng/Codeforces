num = int(input())

a_to_z = "abcdefgh"

for i in range(num):

    start = input()
    char = start[0]
    num = start[1]
    # print("char: ", char)
    # print("num: ", num)

    for i in range(8):
        if i + 1 != int(num):
            temp = str(i + 1)
            ans = char + temp
            print(ans)

    for i in range(len(a_to_z)):
        # print(i, a_to_z[i])
        if a_to_z[i] != char:
            temp = a_to_z[i]
            ans = temp + num
            print(ans)