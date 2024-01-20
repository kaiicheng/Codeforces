# map
t = int(input())

for i in range(t):
    # h, w, a_x, a_y, b_x, b_y = input().split(" ")
    # h, w, a_x, a_y, b_x, b_y = int(h), int(w), int(a_x), int(a_y), int(b_x), int(b_y)
    
    h, w, a_x, a_y, b_x, b_y = map(int, input().split())
    # print("h, w, a_x, a_y, b_x, b_y: ", h, w, a_x, a_y, b_x, b_y)

    if a_x >= b_x:
        print("Draw")
    elif abs(a_x - b_x) % 2 == 1:
        alice = abs(a_x - b_x) // 2 + 1
        bob = abs(a_x - b_x) // 2

        # alice on the left of bob
        if a_y < b_y:
            if b_y + bob <= w:
                b_y += bob
            else:
                b_y = w
            if a_y + alice <= w:
                a_y += alice
            else:
                a_y = w
            if a_y >= b_y:
                print("Alice")
            else:
                print("Draw")

        # bob on the left of alice
        elif a_y > b_y:
            if b_y - bob >= 1:
                b_y -= bob
            else:
                b_y = 1
            if a_y - alice >= 1:
                a_y -= alice
            else:
                a_y = 1
            if a_y <= b_y:
                print("Alice")
            else:
                print("Draw")
        elif a_y == b_y:
            print("Alice")

    elif abs(a_x - b_x) % 2 == 0:
        alice = abs(a_x - b_x) // 2
        bob = abs(a_x - b_x) // 2

        # alice on the left of bob
        if a_y < b_y:
            if b_y - bob >= 1:
                b_y -= bob
            else:
                b_y = 1
            if a_y - alice >= 1:
                a_y -= alice
            else:
                a_y = 1
            if a_y >= b_y:
                print("Bob")
            else:
                print("Draw")

        # bob on the left of alice
        elif a_y > b_y:
            if b_y + bob <= w:
                b_y += bob
            else:
                b_y = w
            if a_y + alice <= w:
                a_y += alice
            else:
                a_y = w
            if a_y <= b_y:
                print("Bob")
            else:
                print("Draw")
        elif a_y == b_y:
            print("Bob")
