def move_max( a ):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

a = [6,9,6,8,54,4,5,6,9]
print(move_max(a))
