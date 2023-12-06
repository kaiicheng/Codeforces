# Counter has same function as dict

from collections import Counter

if __name__ == '__main__':

    num = int(input())

    for i in range(num):
        n = int(input())
        s = input()
        c = Counter(s)
        print("counter: ", c)
        
        maximus = max(c.values())
        print("maximus: ", maximus)
        print("n: ", n)

        ans = max(n % 2, maximus - (n - maximus))
        # ans = maximus - (n - maximus)
        print(ans)

# num = int(input())

# for i in range(num):
#     length = int(input())
#     word = input()
    
#     ls = []
#     for i in range(length):
#         # print("ls: ", ls)
#         # print("word[i]: ", word[i])
#         if i == 0:
#             ls.append(word[i])
#         else:
#             if len(ls) != 0:
#                 if ls[-1] != word[i]:
#                     del ls[-1]
#                     # ls.remove(-1)
#                 else:
#                     ls.append(word[i])
#             else:
#                 ls.append(word[i])

#     print("ls: ", ls)
#     # print("-----end-----")



# num = int(input())

# def reconstruct(str, x, y):
#     ans = []
#     for i in range(len(str)):
#         if i == x or i == y:
#             pass
#         else:
#             ans.append(str[i])
#     print("ans: ", ans)
#     return ans

# for i in range(num):
#     length = input()
#     word = input()
    
#     # for j in range(1, len(word) - 2):
#     one = 0
#     two = 1
#     three = 2
#     four = 3
#     while four < len(word):
#         if word[one] != word[two] and word[three] != word[four]:
#             word = reconstruct(word, one, two)
#             word = reconstruct(word, three - 2, four - 2)
#         else:
#             if word[one] == word[four]:
#                 if word[two] != word[three]:
#                     word = reconstruct(word, two, three)
#                 else:
#                     one += 1
#                     two += 1
#                     three += 1
#                     four += 1
#             else:
#                 if word[two] != word[three]:
#                     word = reconstruct(word, two, three)
#                 else:
#                     one += 1
#                     two += 1
#                     three += 1
#                     four += 1

    # if len(word)

    # elif len(word) > 3:
    #     if word[0] != word[1]:
    #         word = reconstruct(word, 0, 1)
    #     if word[-1] != word[-2]:
    #         word = reconstruct(word, -1, -2)
    # else:
    #     if word[0] != word[1]:
    #         word = reconstruct(word, 0, 1)
    #     else:
    #         if  word[-1] != word[-2]:
    #             word = reconstruct(word, -1, -2)

    # print("word: ", word)



