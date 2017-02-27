import numpy as np

CEL_H = CEL_W = 10

def build(left, top, right, bottom):
    cel = np.zeros((CEL_H, CEL_W))
    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            cel[y, x] = 1

    return cel


def solve(cels):
    result = np.zeros((CEL_H, CEL_W))
    for cel in cels:
        result = result + build(cel[0], cel[1], cel[2], cel[3])

    return np.count_nonzero(result == 2)

def str2array(str):
    edges = str.split('-')
    lefttop = edges[0].split(',')
    rightbottom = edges[1].split(',')
    return([
        int(lefttop[0]),
        int(lefttop[1]),
        int(rightbottom[0]),
        int(rightbottom[1]), ])


def test(result, src, expected):
    str_cels = src.split('/')
    cels = []
    for cel in str_cels:
        cels.append(str2array(cel))

    result[0 if solve(cels) == int(expected) else 1] += 1

result = [0, 0]
test(result, "5,1-7,9/3,2-8,6/0,5-9,5", "15")
test(result, "0,0-9,9/0,0-9,9/0,0-9,9", "0")
test(result, "0,0-9,9/0,0-0,9/1,0-9,9", "100")
test(result, "2,5-7,6/0,5-7,7/2,0-8,6", "0")
test(result, "1,9-4,9/4,9-7,9/0,3-7,4", "1")
test(result, "6,1-6,9/5,0-7,4/5,1-7,2", "6")
test(result, "4,0-9,8/5,1-6,8/0,2-9,7", "28")
test(result, "2,8-8,9/7,9-8,9/8,3-8,9", "2")
test(result, "3,3-9,4/0,1-8,4/1,2-8,9", "12")
test(result, "2,1-8,3/0,1-3,7/8,3-8,4", "7")
test(result, "5,4-6,9/0,0-6,0/5,3-9,8", "10")
test(result, "1,1-9,7/1,1-3,8/3,8-7,9", "22")
test(result, "2,4-6,7/3,2-7,8/1,0-9,4", "24")
test(result, "0,2-1,5/8,1-8,3/1,8-6,8", "0")
test(result, "5,2-9,5/9,1-9,2/8,0-8,6", "5")
test(result, "5,0-6,4/2,1-6,4/3,8-3,9", "8")
test(result, "0,4-6,9/4,1-6,9/7,6-9,7", "18")
test(result, "0,0-5,5/0,1-2,8/5,3-9,4", "17")
test(result, "0,2-5,6/5,6-8,7/0,1-2,6", "16")
test(result, "7,2-8,4/1,0-6,8/1,3-7,6", "26")
test(result, "4,3-9,3/0,0-6,5/0,0-4,8", "31")
test(result, "3,4-4,6/2,2-4,8/2,0-8,4", "11")
test(result, "1,2-6,5/0,5-4,7/2,8-2,9", "4")
test(result, "4,1-7,5/2,1-9,9/1,7-2,9", "23")
test(result, "1,6-5,6/0,3-5,7/0,2-2,6", "13")
test(result, "1,3-3,4/1,4-3,4/9,2-9,9", "3")
test(result, "6,3-7,6/2,2-2,3/1,3-9,8", "9")
test(result, "2,2-9,7/1,8-9,8/2,2-8,9", "49")
test(result, "1,2-6,9/7,6-9,9/4,3-9,9", "33")
test(result, "6,0-7,5/0,4-3,8/1,4-5,8", "15")
test(result, "2,0-9,7/0,5-3,8/5,1-7,7", "27")
test(result, "1,2-8,7/3,1-4,3/2,3-5,8", "20")
test(result, "1,0-7,7/0,1-5,4/0,0-2,3", "19")
test(result, "2,0-3,7/1,1-3,7/5,3-5,9", "14")
test(result, "7,2-9,8/1,0-6,8/0,2-9,9", "63")
test(result, "1,1-5,3/0,3-8,7/2,3-8,7", "32")
test(result, "3,4-6,6/1,0-9,1/4,0-9,9", "21")
test(result, "0,0-4,7/0,5-5,9/0,2-4,5", "25")
test(result, "1,1-9,9/2,2-7,4/2,4-7,7", "30")
test(result, "3,2-9,9/2,0-6,6/0,5-8,9", "36")
test(result, "0,1-8,8/0,5-9,8/2,3-2,4", "38")
test(result, "0,0-8,6/4,3-9,9/7,1-9,9", "29")
test(result, "0,0-8,8/2,4-9,8/0,1-9,2", "53")

print("Success:" + str(result[0]) + ", Fail:" + str(result[1]))
