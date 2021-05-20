
import sys

INT_MIN = -1*sys.maxsize

# 1)Dynamic programming appproch
# Initialize the array of all minimum value


def memoized_cut_rod(p, n):
    r = []
    for i in range(n+1):
        r.append(INT_MIN)
    print(r)
    return _memoized_cut_rod(p, n, r)

# helper function to populate the list with optimum revenue for segment length equal to index


def _memoized_cut_rod(p, n, r):
    # if already know the optimum rev.
    if r[n] >= 0:
        return r[n]
    # for 0 length
    if n == 0:
        q = 0
    else:
        q = INT_MIN
        for i in range(1, n+1):
            q = max(q, p[i-1] + _memoized_cut_rod(p, n-i, r))
    r[n] = q
    return q


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
#print(memoized_cut_rod(p, 4))
# print(r)


# recursive Solution
def CUT_ROD(p, n):
    if n == 0:
        return 0
    q = INT_MIN
    for i in range(1, n+1):
        q = max(q, p[i-1]+CUT_ROD(p, n-i))
    return q


print(CUT_ROD(p, 4))


# bottom up approch to print optimum revenue as well as first cut from left
def bottom_up_cut_rod(p, n):
    r = []
    s = []
    for i in range(n+1):
        r.append(0)
    for i in range(n+1):
        s.append(0)

    r[0] = 0
    for j in range(1, n+1):
        q = INT_MIN
        for i in range(1, j+1):
            if q < p[i-1]+r[j-i]:
                q = p[i-1]+r[j-i]
                s[j] = i
        r[j] = q
    return (r, s)


r, s = bottom_up_cut_rod(p, len(p))
print(f'r[i] = {r}')
print(f's[i] = {s}')
