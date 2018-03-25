coins = input().split(" ")
for j in range(len(coins)):
    coins[j] = int(coins[j])
n = int(input())

num = []
num.append(0)
k = len(coins)

for p in range(1, n + 1):
    minimum = 1787
    for i in range(1, k):
        if coins[i] <= p:
            if (1 + num[p - coins[i]]) < minimum:
                minimum = 1 + num[p - coins[i]]
    num.append(minimum)

if num[n] == 1787:
    print(-1)
else:
    print(num[n])
