# A magic number is a number formed by concatenation of numbers 1, 14 and 144. We can use each of these numbers any number of times. Therefore 14144, 141414 and 1411 are magic numbers but 1444, 514 and 414 are not.
#
# You're given a number. Determine if it is a magic number or not.
#
# Input
# The first line of input contains an integer n, (1 ≤ n ≤ 109). This number doesn't contain leading zeros.
#
# Output
# Print "YES" if n is a magic number or print "NO" if it's not.

def magic_numbers(number, l):
    while number > 0:
        if number % 10 == 1 or number % 10 == 4:
            l.append(number % 10)
        else:
            return "NO"
        number = number // 10

    l = list(reversed(l))
    if l[0] == 4: return "NO"
    i = 0
    while i < (len(l)):
        if l[i] == 1:
            i+=1
        elif l[i] == 4:
            try:
                if l[i - 1] == 1 and l[i + 1] == 4:
                    i += 2
                    continue
            except:
                if l[i-1] == 1:
                    i += 1
                    continue
            if l[i - 1] == 1:
                i += 1
            else:
                return "NO"
    return "YES"

number = int(input())
l = list()
print(magic_numbers(number, l))