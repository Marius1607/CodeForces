#Vasya claims that he had a paper square. He cut it into two rectangular parts using one vertical or horizontal cut.
# Then Vasya informed you the dimensions of these two rectangular parts. You need to check whether Vasya originally had a square.
# In other words, check if it is possible to make a square using two given rectangles.

for i in range(1, (int(input()) * 2)+1):
    l = list(map(int, input().split()))
    if i%2 != 0:
        a = l[0]
        b = l[1]
    else:
        if (a == l[0] and b + l[1] == a) or (b == l[0] and a + l[1] == b) or \
                (a == l[1] and b + l[0] == a) or (b == l[1] and a + l[0] == b):
            print("YES")
        else:
            print("NO")

