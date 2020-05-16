#You have a coins of value n and b coins of value 1. You always pay in exact change, so you want to know if there exist such x
# and y that if you take x (0≤x≤a) coins of value n and y (0≤y≤b) coins of value 1, then the total value of taken coins will be S.

#You have to answer q independent test cases.

for i in range(int(input())):
  l=list(map(int,input().split()))
  print("YES" if (l[3] <= l[0]*l[2]+l[1] and l[3]%l[2] <= l[1]) else "NO")