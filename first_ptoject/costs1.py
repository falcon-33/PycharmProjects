a = int(input())
b = int(input())
n = int(input())
a1 = a * 100
costCoins = (a1 + b) * n
print(costCoins // 100, costCoins % 100)
