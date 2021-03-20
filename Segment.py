import sys
MAX_INT = sys.maxsize


def getSegArr(src, high):
    seg = [MAX_INT]*((high+1)*2)
    populateSegArr(src, seg, 0, high, 0)
    return seg


def populateSegArr(src, seg, low, high, pos):
    if(low == high):
        seg[pos] = src[low]
        return
    mid = (high-low)//2 + low
    populateSegArr(src, seg, low, mid, 2*pos+1)
    populateSegArr(src, seg, mid+1, high, 2*pos+2)
    seg[pos] = min(seg[2*pos+1], seg[2*pos+2])


src = [4, 3, -1, 6, 2]
seg = getSegArr(src, len(src)-1)

print(seg)
