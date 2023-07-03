def sum_of_digits(n):
    ans = 0
    for j in range(len(n)):
        ans += n[j]
    return ans

#print(sum_of_digits([1,7,42,12,10,1,4,0]))
# problem1 77

def inside(n):
    n = str(n)
    if n in '123456789':
        return True

#print(inside(7))
#problem2 True

def find_divs(n):
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            if i != n//i:
                a.append(n//i)
    return a

def sum_of_divs(n):
    return sum(find_divs(n)) - n + 1

def is_perfect_digit(n):
    if sum_of_divs(n) == n:
        return True
    return False

#print(is_perfect_digit(8128))
#problem3 True

def is_pallindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

#print(is_pallindrome(1234567899876554321))
#problem4 False

def is_prime(n):
    if len(find_divs(n)) == 0:
        return True
    return False

#print(is_prime(123321))
#problem5 False

def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(10))
#4)2 5)3 6)5 7)8 8)13 9)21 10)34
#problem6 34
