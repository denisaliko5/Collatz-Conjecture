num = int(input("Enter an integer: "))
cnt = 0
while True:
  cnt += 1
  if num%2 == 0:
    num /= 2
    print(format(num, '.0f'))
  else:
    num = (num*3)+1
    print(format(num, '.0f'))
  if num == 1:
    break
print(cnt, "times iritated.")