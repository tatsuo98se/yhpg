def right_func(input_num):
    return input_num // 2 - 10

def left_func(input_num):
    return input_num * 2 // 3

def calc(memo, input_num, target):
    if input_num in memo:
        return memo[input_num]

    if input_num < target:
        return 0

    if input_num == target:
        return 1

    ans = calc(memo, right_func(input_num), target) + calc(memo, left_func(input_num), target)
    memo[input_num] = ans
    return ans

def resolve(data):
    memo = {}
    counter = 0
    splited = data.split(",")

    input_num = int(splited[0])
    target = int(splited[1])

    return str(calc(memo, input_num, target))


## test logic
class Result:
    def __init__(self):
        self.success = 0
        self.fail = 0

RESULT = Result()
RESULT.success = RESULT.fail = 0

def test(data, expect):
    print("actual:" + resolve(data) + " expected:" + expect)
    if resolve(data) == expect:
        RESULT.success += 1
    else:
        RESULT.fail += 1


test( "123,4", "5" )
test( "1,1", "1" )
test( "2,1", "1" )
test( "3,3", "1" )
test( "19,5", "1" )
test( "69,5", "3" )
test( "88,9", "2" )
test( "1,100", "0" )
test( "100,4", "4" )
test( "101,9", "0" )
test( "456,7", "7" )
test( "567,8", "12" )
test( "756,10", "10" )
test( "789,10", "12" )
test( "896,29", "2" )
test( "7764,6", "664" )
test( "1234,56", "3" )
test( "8563,29", "35" )    
test( "12345,67", "10" )    
test( "72927,51", "263" )    
test( "71441,145", "22" )    
test( "123456,78", "397" )    
test( "123456,789", "1" )    
test( "592741,216", "55" )    
test( "913826,584", "81" )    
test( "1234567,89", "2293" )    
test( "10000000,1", "19383507" )    
test( "12345678,9", "3567354" )    
test( "6215879,358", "2907" )    
test( "12345678,90", "79419" )    
test( "5745432,1032", "1287" )

print("Success: {0.success}, Fail: {0.fail}".format(RESULT))
