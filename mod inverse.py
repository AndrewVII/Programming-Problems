def inv(x, y):
    ans = 0
    while (x*ans) % y != 1:
        ans += 1
        if ans > y:
            return "No such integer exists."
    return ans

n = int(input())
m = int(input())

print(inv(n,m))
