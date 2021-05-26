import sys
MAX = sys.maxsize


def matParentizeOptimum(p, n):

    m = [[0]*(n)]*(n)

    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i+l-1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[1][n-1], s


def print_optimal(s, i, j):

    if i == j:
        print("A"+str(i), end=" ")
    else:
        print("(", end=' ')
        print_optimal(s, i, s[i][j])
        print_optimal(s, s[i][j]+1, j)
        print(")", end=" ")


p = [30, 35, 15, 5, 10, 20, 25]
n = len(p)
m1, s = matParentizeOptimum(p, n)
print()
print()

print("Optimum parenthisize operation = ", m1)

print("The multiplication to be performed is ", end=" ")
print_optimal(s, 1, n-1)
