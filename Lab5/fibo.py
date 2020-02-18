dp = [-1] * 10000
def fibo(n):
    if (dp[n] == -1):
        dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n];

dp[0] = 0
dp[1] = 1

print(fibo(7))


dp2 = [-1] * 10000
def fibo2(n):
    dp2[0] = 0
    dp2[1] = 1
    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + dp2[i - 2]
    print(dp2[n])

fibo2(7)

for (i = 0, i < 5, i += 1)
    print(i)