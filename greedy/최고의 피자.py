'''
https://codeup.kr/problem.php?id=3321
'''

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []
for i in range(n) : 
  d.append(int(input()))

d.sort(reverse=True)

#첫 칼로리는 도우 칼로리로
cal = c

tmp = float(cal / a) #각 순간의 칼로리값
mx = tmp #그 전의 칼로리값

#1달러 당 칼로리가 낮아지기 전까지 계속 내림차순으로 더함
for i in range(n) :
  cal = cal + d[i]
  tmp = float(cal / (a + b * (i + 1)))

  if tmp < mx : 
    break
  else :
    mx = tmp

print(int(mx))

