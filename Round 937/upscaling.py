t = int(input())

for i in range(t):

    n = int(input())
    two_n = 2 * n
    
    # number_sign = True
    # dot = True

    col_change = False
    col_sign = "#"

    ans = []
    for i in range(two_n):
        temp = []

        if i != 0 and i % 2 == 1:
            col_change = True
        if col_change and i % 2 == 0:
            if col_sign == "#":
                col_sign = "."
            elif col_sign == ".":
                col_sign = "#"

        temp.append(col_sign * 2)
        # temp.append(row_sign * 2)

        # print("temp: ", temp)
        ans.append(temp)
    # print("ans: ", ans)

    row_change = False
    row_sign = ans[0][0][0]
    for i in range(len(ans)):

        # print("ans[i]: ", ans[i])
        temp = ans[i]
        row_sign = temp[0][0]
        if row_sign == "#":
            row_sign = "."
        elif row_sign == ".":
            row_sign = "#"
        for j in range(two_n - 2):
            # print("i, j: ", i, j)
            # print("row_sign: ", row_sign)

            if j != 0 and j % 2 == 1:
                row_change = True
            if row_change and j % 2 == 0:
                if row_sign == "#":
                    row_sign = "."
                elif row_sign == ".":
                    row_sign = "#"
            if j % 2 == 1:
                temp.append(row_sign * 2)
                # print("temp: ", temp)
        row_change = False
        ans[i] = temp

    # print("ans: ", ans)

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = "")
        print()
    
    # print("---end---")
