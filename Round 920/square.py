t = int(input())

for i in range(t):
    a = input().split(" ")
    b = input().split(" ")
    c = input().split(" ")
    d = input().split(" ")
    # print("a, b, c, d: ", a, b, c, d)
    
    if a[0] == b[0]:
        print(abs(int(a[1])  - int(b[1])) * abs(int(c[1]) - int(d[1])))
    elif a[0] == c[0]:
        print(abs(int(a[1])  - int(c[1])) * abs(int(b[1]) - int(d[1])))
    elif a[0] == d[0]:
        print(abs(int(a[1])  - int(d[1])) * abs(int(b[1]) - int(c[1])))