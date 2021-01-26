'''
https://codeup.kr/problem.php?id=4040
'''
'''
도착하는날~(출발하는날-1)만큼 방을 쓸 수 있어야 함
'''
n, m = map(int, input().split())

d = []
for i in range(n) : 
  d.append(list(input()))

s, t = map(int, input().split())

str_list = list(map(list, zip(*d)))

mx = [0, 0]

'''
a = 묵은 방의 수
b = 날짜 계산용
'''
a = 0
b = t - s


while b > 0 : 
  cnt = [0 for _ in range(m)]

  #연속되는 방이 제일 많은 거 찾기
  for i in range(m) : 
    day = (t - b) - 1 #날짜를 인덱스로
    if str_list[i][day] == 'O' : 
      cnt[i] = 1
      while str_list[i][day+1] == 'O' :
        cnt[i] = cnt[i] + 1
        day = day + 1

  b = b - max(cnt)
  a = a + 1

print(a-1) #방 갯수를 옮긴 횟수로 환산
