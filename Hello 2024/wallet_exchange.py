t = int(input())

for i in range(t):
    x = input().split(" ")
    a = int(x[0])
    b = int(x[1])
    
    if (a + b) % 2 == 0:
        print("Bob")
    else:
        print("Alice")