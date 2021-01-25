'''
https://codeup.kr/problem.php?id=3120
'''

a, b = map(int, input().split())

dif = abs(b-a)
cnt = 0

cnt_10 = dif // 10
dif = dif % 10

if dif > 7 : 
  cnt_10 = cnt_10 + 1
  dif = abs(dif - 10)

cnt_5 = dif // 5
dif = dif % 5

if dif > 3 : 
  cnt_5 = cnt_5 + 1
  dif = abs(dif - 5)

cnt_1 = dif

cnt = cnt_10 + cnt_5 + cnt_1

print(cnt)
