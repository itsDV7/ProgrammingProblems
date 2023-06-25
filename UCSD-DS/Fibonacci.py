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

# Pisano Period - 01
def fibomod(n, mod):
    if mod == 1:
        return 0
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            if mod >= n:
                prev = 0
                curr = 1
                for _ in range(2, n + 1):
                    prev, curr = curr, prev + curr
                return curr%mod
            else:
                pattern = list()
                pattern.append(0)
                pattern.append(1)
                while True:
                    if len(pattern) > 10**4:
                        return -1
                    pattern.append((pattern[-2] + pattern[-1])%mod)
                    if pattern[-2] == 0 and pattern[-1] == 1:
                        pattern.pop()
                        pattern.pop()
                        break
                return pattern[n%len(pattern)]

# Fibo sum using Pisano Period
def fibosum(n):
    if n < 2:
        return n
    else:
        res = 0
        pattern = list()
        pattern.append(0)
        pattern.append(1)
        pattern_sum = 0
        while True:
            curr = (pattern[-2] + pattern[-1])%10
            pattern.append(curr)
            pattern_sum += curr
            if pattern[-2] == 0 and pattern[-1] == 1:
                pattern.pop()
                pattern.pop()
                break
        pattern_len = len(pattern)
        if n < pattern_len:
            res = sum(pattern[:n+1])%10
        else:
            res = ((pattern_sum * (n//pattern_len)) + sum(pattern[:(n%pattern_len)+1]))%10
        return res

# Fibo Part Sum using Pisano Period
def fibopartsum(m, n):
    if n < 2:
        return n
    else:
        res = 0
        pattern = list()
        pattern.append(0)
        pattern.append(1)
        pattern_sum = 0
        while True:
            curr = (pattern[-2] + pattern[-1])%10
            pattern.append(curr)
            pattern_sum += curr
            if pattern[-2] == 0 and pattern[-1] == 1:
                pattern.pop()
                pattern.pop()
                break
        pattern_len = len(pattern)
        if m < pattern_len and n < pattern_len:
            res = sum(pattern[m:n+1])
        elif m < pattern_len and n >= pattern_len:
            res = sum(pattern[m:])
            res += pattern_sum * ((n//pattern_len)-1) + sum(pattern[:(n%pattern_len)+1])
        elif m > pattern_len:
            res = sum(pattern[(m%pattern_len):])
            res += pattern_sum * ((m//pattern_len) - (n//pattern_len) - 1) + sum(pattern[:(n%pattern_len)+1])
        return res%10

# Fibo Sq Sum using Pisano Period
def fibosqsum(n):
    if n < 2:
        return n
    else:
        res = 0
        pattern = list()
        sqs = list()
        pattern.append(0)
        sqs.append(0)
        pattern.append(1)
        sqs.append(1)
        while True:
            pattern.append((pattern[-2] + pattern[-1])%10)
            sqs.append((pattern[-1]**2)%10)
            if pattern[-2] == 0 and pattern[-1] == 1:
                pattern.pop()
                sqs.pop()
                pattern.pop()
                sqs.pop()
                break
        pattern_len = len(pattern)
        sqs_sum = sum(sqs)
        if n < pattern_len:
            res = sum(sqs[:n+1])%10
        else:
            res = sqs_sum * (n//pattern_len) + sum(sqs[:(n%pattern_len)+1])
            res %= 10
    return res
