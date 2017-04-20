polygon_table = {}
polygon_table[0] = ''
polygon_table[1] = '3'
polygon_table[2] = '4'
polygon_table[3] = '5'
polygon_table[4] = '5'
polygon_table[5] = '7'
polygon_table[6] = '8'
polygon_table[7] = '9'

def get_startline(data):
    start = 128
    while True:
        if data >= start:
            return start
        else:
            start /= 2

def detect_poly(data):
    start = get_startline(data)
    triangle_count = []
    count = 0

    while start != 0:
        if data >= start:
            data -= start
            triangle_count.append(count)
            count = 0
        else:
            start /= 2
            count += 1

    polys = []
    for t in triangle_count:
        polys.append(polygon_table[t])

    remaining = 8 - sum(triangle_count)
    if remaining > 0:
        polys.append(polygon_table[remaining])

    polys.sort()
    return ''.join(polys)

## test logic
class Result:
    def __init__(self):
        self.success = 0
        self.fail = 0

RESULT = Result()
RESULT.success = RESULT.fail = 0

def test(data, expect):
#    print("actual:" + detect_poly(int(data)) + " expected:" + expect)
    if detect_poly(int(data)) == expect:
        RESULT.success += 1
    else:
        RESULT.fail += 1

## ---- tests ----

test("165", "3445" )
test("80", "48" )
test("255", "33333333" )
test("68", "55" )
test("200", "355" )
test("82", "455" )
test("164", "455" )
test("73", "455" )
test("146", "455" )
test("37", "455" )
test("74", "455" )
test("148", "455" )
test("41", "455" )
test("38", "355" )
test("76", "355" )
test("152", "355" )
test("49", "355" )
test("98", "355" )
test("196", "355" )
test("137", "355" )
test("19", "355" )
test("20", "48" )
test("9", "57" )
test("209", "3345" )
test("121", "33345" )
test("239", "3333334" )
test("26", "347" )
test("111", "333344" )
test("95", "333344" )
test("85", "4444" )
test("24", "39" )
test("97", "347" )
test("234", "33444" )
test("59", "33345" )
test("187", "333344" )
test("34", "55" )
test("249", "333335" )
test("43", "3445" )
test("143", "33335" )
test("28", "338" )
test("79", "33345" )
test("173", "33444" )
test("55", "33345" )
test("77", "3445" )
test("35", "355" )
test("153", "3355" )
test("30", "3337" )
test("228", "3355" )
test("177", "3345" )
test("162", "445" )
test("184", "3345" )

## --------------

print("Success: {0.success}, Fail: {0.fail}".format(RESULT))
