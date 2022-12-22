# n = 9000
# k = 100

# result = 0
# while True:
#     a = (n//k) * k # when divide result == 0
#     result += n - a 
#     n = a

#     if n < k:
#         break

#     n //= k 
#     result += 1

# result += (n - 1)

######################################

# number = "567"
# result = 0
# for n in number:
#     if int(n) <= 1 or result == 0:
#         result += int(n)
#     else:
#         result *= int(n)
# print(result)

######################################

# adventure = list(map(int, input().split()))
# adventure.sort()
# result = 0
# count = 0
# for a in adventure:
#     count += 1
#     if count >= a:
#         result += 1
#         count = 0

# print(result)

######################################
# n = int(input())
# person = list(map(int, input().split()))
# person.sort()

# result = 0
# for i in range(0,n):
#     result += person[i] * (n-i)
# print(result)

######################################
sugar = int(input()) #4999
result = 0
while True:
    if sugar % 5 == 0:
        result += sugar // 5
        print(result)
        break
    sugar -= 3
    result += 1
    if sugar == 0:
        print(result)
        break
    elif sugar < 3:
        print("-1")
        break
