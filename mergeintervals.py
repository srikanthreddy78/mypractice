def mi(arr):
    arr.sort(key=lambda x: x[0])
    m = []
    s = 0
    max = 0
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]
    if max != 0 and [s, max] not in m:
        m.append([s, max])
    for i in range(len(m)):
        print(m[i], end=" ")
arr = [[1,3],[2,6],[8,10],[15,18]]
mi(arr)
