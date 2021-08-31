def com(a,a1,a2):
  l=0
  m=0
  n=0
  while (m <len(a1) and l < len(a) and n<len(a2)):
    if a[l] > a1[m]:
      m=m+1
    elif a1[m] >a[l]:
      l=l+1
    elif a1[m] == a2[n]:
      print(a[l])
      l=l+1
      m=m+1
      n=n+1
    else:
      n=n+1
arr=[1,2,3,5,6,7,8]
arr2=[2,6,7,8,9,10]
arr3=[1,2,6,7,8,9]
com(arr,arr2,arr3)
