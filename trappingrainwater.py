def tr(a,n):
  result=0
  l=0
  r=n-1
  lmax=0
  rmax=0
  while (l<=r):
    if a[l] <= a[r]:
      if a[l] > lmax:
        lmax=a[l]
      else:
        result=result+(lmax-a[l])
        l=l+1
    else:
     if a[r] > rmax:
       rmax= a[r]
     else:
      result=result+(rmax-a[r])
      r=r-1
  print(result)
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
tr(arr,n)