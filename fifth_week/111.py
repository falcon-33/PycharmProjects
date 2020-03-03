f = int(input())
random_list = list(map(int, input().split()))
x = int(input())


def number_near(random_list, target):
    return min(random_list, key=lambda x: abs(x-target))


print(number_near(random_list, x))
