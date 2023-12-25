t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    # print("s: ", s)
    st = set()
    ans = 0
    dp = set()
    temp_s = ""
    for c in s:
        # print("c: ", c)

        st.add(c)
        ans += len(st)
    #     print("ans: ", ans)
    #     print("st: ", st)
    #     print("---end of iteration---")
    # print("---end---")
    print(ans)


# import copy

# t = int(input())

# for i in range(t):

#     n = int(input())
#     print("n: ", n)

#     a = input()
#     print("a: ", a)
#     a = [i for i in a]
#     print("list(a): ", a)

#     # dp = [0] * len(a) * 2
#     # dp = []
#     # dp.append("".join(a))
#     dp = set()
#     dp.add("".join(a))

#     def erase(s):
#         temp_ls1 = [s[i] for i in range(len(s)) if i != 0]
#         print("temp_ls1: ", temp_ls1)
#         temp1 = "".join(temp_ls1)
#         if temp1 not in dp and temp1 != "":
#             # dp.append(temp1)
#             dp.add(temp1)

#         temp_ls2 = [s[i] for i in range(len(s)) if i != 1]
#         print("temp_ls2: ", temp_ls2)
#         temp2 = "".join(temp_ls2)
#         if temp2 not in dp and temp2 != "":
#             # dp.append(temp2)
#             dp.add(temp2)
#         return temp1, temp2

#     temp1 = copy.deepcopy(a)
#     temp2 = None

#     while len(temp1) > 0:
#         for i in dp:
#             temp1, temp2 = erase(i)
#         # temp1, temp2 = erase(temp1)
#         print("temp1, temp2: ", temp1, temp2)

#     print("dp: ", dp)
#     print("len(dp): ", len(dp))
#     print("---end---")



    # def erase(s):
    #     temp_ls1 = [s[i] for i in range(len(s)) if i != 0]
    #     print("temp_ls1: ", temp_ls1)
    #     temp1 = "".join(temp_ls1)
    #     if temp1 not in dp and temp1 != "":
    #         dp.append(temp1)

    #     temp_ls2 = [s[i] for i in range(len(s)) if i != 1]
    #     print("temp_ls2: ", temp_ls2)
    #     temp2 = "".join(temp_ls2)
    #     if temp2 not in dp and temp2 != "":
    #         dp.append(temp2)
    #     return temp1, temp2

    # # def erase_index_0(s):
    # #     temp_ls1 = [s[i] for i in range(len(s)) if i != 0]
    # #     print("temp_ls1: ", temp_ls1)
    # #     temp1 = "".join(temp_ls1)
    # #     if temp1 not in dp and temp1 != "":
    # #         dp.append(temp1)
    # #     return temp1

    # # def erase_index_1(s):
    # #     temp_ls2 = [s[i] for i in range(len(s)) if i != 1]
    # #     print("temp_ls2: ", temp_ls2)
    # #     temp2 = "".join(temp_ls2)
    # #     if temp2 not in dp and temp2 != "":
    # #         dp.append(temp2)
    # #     return temp2

    # temp1 = copy.deepcopy(a)
    # temp2 = None

    # # temp = copy.deepcopy(a)
    # # temp1 = erase_index_0(temp)
    # # temp2 = erase_index_1(temp)
    # # if temp1 not in dp and temp1 != "":
    # #     dp.append("".join(temp1))
    # # if temp2 not in dp and temp2 != "":
    # #     dp.append("".join(temp2))

    # # temp1 = copy.deepcopy(a)
    # # temp2 = copy.deepcopy(a)

    # while len(temp1) > 1:
    #     if len(temp1) == 1:
    #         break
    #     temp1, temp2 = erase(temp1)
        
    #     # temp1 = erase_index_0(temp1)
    #     # if temp2 is not None:
    #     #     temp2 = erase_index_1(temp2)
    #     # temp1, temp2 = erase(temp1)
    #     print("temp1, temp2: ", temp1, temp2)

    # print("dp: ", dp)
    # print("len(dp): ", len(dp))
    # print("---end---")




    # # dp = [0] * len(a) * 2
    # dp = []

    # # di = {}
    # # di["".join(a)] = ""
    # # print("di: ", di)

    # # temp = ""
    # # dp.append("")

    # for j in range(len(a)):
        
    #     if j == 0:
    #         # temp = dp[0]
    #         temp = a[j]
    #         print("temp: ", temp)
    #         dp.append(temp)
    #     else:
    #         for k in range(len(dp)):
    #             temp = dp[k]
    #             temp += a[j]
    #             if temp not in dp:
    #                 dp.append(temp)

    #     # print("dp: ", dp)
    # print("dp: ", dp)
    # print("---end---")
    # print("len(dp): ", len(dp))




    # di = {}
    # di["".join(a)] = ""
    # print("di: ", di)

    # for j in range(len(a)):
    #     if j == 0:
    #         temp_ls = a[j + 1:]
    #     elif j == len(a) - 1:
    #         temp_ls = a[:j]
    #     else:
    #         temp_ls = a[:j] + a[j + 1:]
    #     print("temp_ls: ", temp_ls)
        
    #     temp_s = "".join(temp_ls)
    #     if temp_s != "" and temp_s not in di:
    #         di[temp_s] = ""
    #     print("di: ", di)
    # print("---end---")

