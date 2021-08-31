def maxpr(arr):
  mina=10000000
  pro=0
  for i in range(len(arr)):
    mina=min(mina,arr[i])
    pro = max(pro,arr[i]-mina)
  print(pro)
arr=[7,1,5,3,6,4]
maxpr(arr)