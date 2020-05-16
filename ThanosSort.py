#Thanos sort is a supervillain sorting algorithm, which works as follows: if the array is not sorted,
# snap your fingers* to remove the first or the second half of the items, and repeat the process.

#Given an input array, what is the size of the longest sorted array you can obtain from it using Thanos sort?

#*Infinity Gauntlet required.
def ts(l):
    if not l:
        return []
    if sorted(l) == l:
        return l
    part1, part2 = l[:len(l) // 2], l[len(l) // 2:]
    r1 = ts(part1)
    r2 = ts(part2)
    return r1 if len(r1) > len(r2) else r2


n = int(input())
l = list(map(int, input().split()))

print(len(ts(l)))
