def naivepolymulti(A, B):
    ans = [0]*(2*len(A)-1)
    for i in range(len(A)):
        for j in range(len(A)):
            ans[i + j] = ans[i + j] + (A[i] * B[j])
    return ans

# A = [0,5,3,0,0,4,0,1]
# B = [0,0,6,0,0,0,0,5]
# naivepolymulti(A, B)
# [0, 0, 0, 30, 18, 0, 0, 24, 25, 21, 0, 0, 20, 0, 5]
