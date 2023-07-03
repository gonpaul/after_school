ans = 0
for x in range(10, 51):
    for y in range(10, 51):
        for k in range(10, 51):
            if x**2 + y**2 == k**2:
                ans += 1
print(ans)
#26
