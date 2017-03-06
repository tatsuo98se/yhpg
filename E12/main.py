
import re
import numpy as np

class Result:
    def __init__(self):
        self.success = 0
        self.fail = 0

class Block:
    def __init__(self, left, bottom_lines, heights):
        self.left = int(left)
        self.bottom_lines = bottom_lines
        self.heights = heights
        self.height = np.max(self.heights)
        self.width = np.size(self.heights)

class IBlock(Block):
    def __init__(self, left):
        super().__init__(left, [0], [4])

class LBlock(Block):
    def __init__(self, left):
        super().__init__(left, [0, 0], [3,1])

class OBlock(Block):
    def __init__(self, left):
        super().__init__(left, [0,0],[2,2])

class SBlock(Block):
    def __init__(self, left):
        super().__init__(left, [0,0,-1],[1,2,2])

class TBlock(Block):
    def __init__(self, left):
        super().__init__(left, [-1,0,-1],[2,2,2])

class Space:
    def __init__(self):
        self.lines = np.zeros(10)

    def stack(self, block):
        if np.size(self.lines) < (block.left + block.width):
            self.lines.resize((block.left + block.width), refcheck=False)
        
        self.lines[block.left : block.left + block.width] += block.bottom_lines
        self.lines[block.left : block.left + block.width] = np.max(self.lines[block.left : block.left + block.width] )
        self.lines[block.left : block.left + block.width] += block.heights

    def get_height(self):
        return np.max(self.lines)

def build_block(left, type):
    if type == 'I':
        return  IBlock(left) 
    elif type == 'L':
        return LBlock(left)    
    elif type == 'O':
        return OBlock(left)    
    elif type == 'S':
        return SBlock(left)    
    elif type == 'T':
        return TBlock(left)    

def solve(input):
    space = Space()
    blockTypes = np.array([re.findall("[0-9]+", input), re.findall("[A-Z]+", input)])
    blockTypes = blockTypes.transpose()

    for blockType in blockTypes:
        space.stack(build_block(blockType[0], blockType[1]))

    return space.get_height()

result = Result()
result.success = result.fail = 0

def test(src, expected):
    if solve(src) == int(expected):
        result.success += 1
    else:
        result.fail += 1

test("1O3L0I0T", "5")
test("0I", "4")
test("0I0I", "8")
test("0I1I2I3I4I", "4")
test("0S0I", "5")
test("0I0S", "6")
test("2S0T2O3I", "8")
test("4O4T1T0S4L1L3L", "10")
test("0S2S4S6S8S10S12S14S", "16")
test("14S12S10S8S6S4S2S0S", "2")
test("5I2O10I0O4L10T9T11L8I2I10I12O7L12T12T12S11T9O10O13I12O10O7I9I7O0S1O2S0L1L", "23")
test("9T14L10L8T4I1T3S5I8T12O3S7L9O7L14T2I7O3S6S2L0L13T10O4I9T7L8S0I12O9S11L11T14T", "27")
test("9S9S7O11O16I2T9O12L10T9O0O13I9O1I2T14S7O9S11T5L7I14T13O0T12I3S10L10O7I15I6S2L12S8I16I3L", "23")
test("11T13I16S15T7O10L12S1I5I8S5I13I15O8S9I1T12I1S5S0L14I12L16T2S2S8L2S14L16O4I13L15L13S11S9T13S9S3L6O", "22")
test("12L10S7I5L14T12S9L1T14I0I5L1T2O18T9L0I15I16L10S1O15I0L17O5L18T4I18L7L7I13I3I12I2S3T5T3S16L14S14O11O15T14S", "17")
test("0S18S2S19I14T7L14L2L6I9I0L4I5L13L15I8S8T2I5I7O18T3S1T7I2L8O0S20T9I14T5L5I1T4L9O8T19T5S12O16T19L4O10O10T14L", "24")
test("7T5L6S4S8T6S10I19O20L14I18L21S7I11S11O1L13T20O9I7L2T8L2S20L3O14L9T17I8L8S14I6T2O11T21O18O6T15T1S3L6O19S18O20S19O16T6S14T", "26")
test("18S2I4S16L13S17I21O8I17T8I14O12T20I20S19S16S13T12T20I22I15O2I2I8I2S18I9I9T6O13O13L17I2L20L2L4I9I19O11T3S10O2S18T12I5O11S19O21S6I17T17S", "26")
test("11L5S0T22S18O13T2O22S15I12I21T16I3I1I22L11L11L22O13S24S15L13T15S19L10O15T7S24T19L0T13O11I12T13S4I24L15O3S19O10L19O0S20L7O11L21I22S18T19T23O8I22S24L0S", "21")
test("7L7I11T7S18O17L8S15L9I3O24S3O1O5O14L9T13S2O25S22T10T8L24S18S13T1O1L6I10I4S13O3S7L10T1T4L17S20I18O15S25S23S21I19T6O24S9L2O2O15L12L8L8O18I18L0T5O", "31")
test("999I999I999I999I999I999I999I999I999I999I999I", "44")

print("Success: {0.success}, Fail: {0.fail}".format(result))