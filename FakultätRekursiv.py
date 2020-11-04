def fakrek(n):
    if n ==1:
        return 1
    else:
        return fakrek(n - 1) * n

def fakit(n):
    fak = 1
    for i in range(1, n+1):
        fak = fak * i
    return fak

print(fakit(5))




