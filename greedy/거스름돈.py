'''
https://codeup.kr/problem.php?id=3301
'''

n = int(input())

num_50000 = n//50000
n = n%50000
num_10000 = n//10000
n = n%10000
num_5000 = n//5000
n = n%5000
num_1000 = n//1000
n = n%1000
num_500 = n//500
n = n%500
num_100 = n//100
n = n%100
num_50 = n//50
n = n%50
num_10 = n//10
n = n%10

print(num_50000 + num_10000 + num_5000 + num_1000 + num_500 + num_100 + num_50 + num_10)
