#Let's define the following recurrence:
#an+1=an+minDigit(an)⋅maxDigit(an).
#Here minDigit(x) and maxDigit(x) are the minimal and maximal digits in the decimal representation of x without leading zeroes.
# For examples refer to notes.
#Your task is calculate aK for given a1 and K.

for i in range(int(input())):
    a,b = map(int, input().split())
    while b != 1:
        a += max(list(map(int, str(a))))  * min(list(map(int, str(a))))
        b -= 1
    print(a)