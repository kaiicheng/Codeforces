t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    f = input()
    # print("n, s, f: ", s, f)

    s_one = s.count("1")
    f_one = f.count("1")
    # print("s_one, t_one: ", s_one, f_one)

    ans = 0
    save = 0
    for i in range(n):
        # print("s_one, f_one: ", s_one, f_one)
        if f[i] == "1":

            if s[i] == "0":
                # if s_one > f_one:
                    # s_one -= 1
                save += 1
                # elif save == 0: 
                ans += 1

                
            elif s[i] == "1":
                pass

        elif f[i] == "0":
            
            if s[i] == "1":
                ans += 1

            elif s[i] == "0":
                pass
    
    # print("ans, save: ", ans, save)

    if s_one == f_one:
        print(save)
    elif s_one > f_one:
        print(ans - save)
    elif s_one < f_one:
        print(save)

    # print("---end---")


    # if s_zero > f_zero:
        
    #     print()
    # elif s_zero < f_zero:
    #     print()
    # else s_zero == f_zero:
    #     print(0)