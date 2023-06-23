# Fibonacci
def Fibonacci(n):
    numlist = list()
    numlist.append(0)
    numlist.append(1)
    if n < 0:
        return 0
    elif n <= 1:
        return numlist[n]
    else:
        for i in range(2, n+1):
            numlist.append(numlist[i-1] + numlist[i-2])
        return numlist[n]
    return -1
