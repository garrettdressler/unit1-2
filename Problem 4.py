year = int(input())
if year % 100 == 0:
  print(year // 100)
if year % 100 != 0:
  print(year // 100 + 1)