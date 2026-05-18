mylist = [1, 2, 3,4,5,6,7,8,9,10]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)
