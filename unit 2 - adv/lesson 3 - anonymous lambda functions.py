#1 ["Женя", "Вася"]

L1 = [2,4,6,8,10]
print(list(map(lambda x: x**3, L1)))
#2 [8, 64, 216, 512, 1000]

ar1 = [-1, 4, -7, -8, -10, 1, 0]
ar2 = filter(lambda x: x < 0, ar1)
print(list(ar2))
#3 [-1, -7, -8, -10]

from functools import reduce
list1 = [x for x in range(1, int(input())+1)]
ans = reduce(lambda x,y: x*y, list1)
print(ans)
#4 40320

given = [2,4,6,8,0,3,4,2,3,5,1,2]
ans = max(filter(lambda x: x**2 % 9 == 0, given))
print(ans)
#5 6
