'''
https://codeup.kr/problem.php?id=2001
'''

pasta1 = float(input())
pasta2 = float(input())
pasta3 = float(input())

juice1 = float(input())
juice2 = float(input())

pasta = min([pasta1, pasta2, pasta3])
juice = min([juice1, juice2])

sum = pasta + juice
result = sum * 1.1

print(round(result,2))
