# 0:48
import time

SIZE = 100

def make_square():
    arr = [[0 for i in range(SIZE+2)] for j in range(SIZE+2)]
    
    c = 1
    size = 1
    for i in range(SIZE-1):
        is_odd = size%2 == 1
        for j in range(size):
            if is_odd:
                arr[size][j+1] = c
            else:
                arr[j+1][size] = c
            c+=1

        for j in reversed(range(size-1)):
            if is_odd:
                arr[j+1][size] = c
            else:
                arr[size][j+1] = c
            c+=1
        size+=1

    return arr

def find_pos(arr,num):
    for i in range(SIZE):
        for j in range(SIZE):
            if arr[i][j] == num:
                return (i,j)

    raise RuntimeError
                

def get_number(arr, pos):
    num = arr[pos[0]][pos[1]]
    if num == 0:
        return '-'
    else:
        return str(num)


def solve(arr, data):
    p = find_pos(arr, int(data))

    result = []
    for i in [[0,-1],[0,1],[-1,0],[1,0]]:
        result.append(get_number(arr, (p[0]+i[0], p[1]+i[1])))
    return ','.join(result)

GUNEGUNE = make_square()

################
## test logic ##
################
class RESULT:
    success = 0
    fail = 0

RESULT.success = RESULT.fail = 0


def test(data, expect):
    r = solve(GUNEGUNE, data)
    print 'actual:' + r + ' expected:' + expect
    if r == expect:
        RESULT.success += 1
    else:
        RESULT.fail += 1

#################
starttime = time.time()

test( "10", "9,25,-,11" )
test( "1", "-,2,-,4" )
test( "2", "1,9,-,3" )
test( "4", "-,3,1,5" )
test( "26", "25,49,-,27" )
test( "72", "71,73,57,93" )
test( "82", "81,121,-,83" )
test( "100", "-,99,65,101" )
test( "122", "121,169,-,123" )
test( "141", "142,140,104,148" )
test( "145", "-,146,144,196" )
test( "320", "321,319,261,329" )
test( "504", "503,505,465,557" )
test( "563", "564,562,498,590" )
test( "906", "905,907,895,1019" )
test( "1047", "1046,1048,1002,1134" )
test( "1111", "1068,1204,1110,1112" )
test( "1338", "1257,1401,1339,1337" )
test( "1613", "1612,1614,1588,1752" )
test( "1845", "1686,1854,1846,1844" )
test( "1921", "1922,1920,1780,1952" )
test( "2517", "2516,2518,2484,2688" )
test( "2670", "2671,2669,2535,2739" )
test( "2798", "2613,2821,2799,2797" )
test( "2841", "2778,2994,2840,2842" )
test( "2896", "2897,2895,2725,2937" )
test( "3050", "3001,3225,3049,3051" )
test( "3354", "3355,3353,3147,3375" )
test( "3563", "3564,3562,3402,3638" )
test( "4454", "4261,4525,4455,4453" )
test( "5397", "5262,5558,5396,5398" )
test( "5592", "5363,5659,5593,5591" )
test( "6122", "6121,6123,6047,6363" )
test( "6772", "6771,6773,6677,7009" )

endtime = time.time()
interval = endtime - starttime

print "Success: {0.success}, Fail: {0.fail} ({1}sec)".format(RESULT, interval)
