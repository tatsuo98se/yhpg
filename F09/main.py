## 1:05

import numpy as np

operations = {
    # operation : axis, index, direction
    'a' : (1, 0, -1),
    'b' : (1, 1, -1),
    'c' : (1, 2, -1),
    'd' : (0, 0, 1),
    'e' : (0, 1, 1),
    'f' : (0, 2, 1),
    'g' : (1, 2, 1),
    'h' : (1, 1, 1),
    'i' : (1, 0, 1),
    'j' : (0, 2, -1),
    'k' : (0, 1, -1),
    'l' : (0, 0, -1)
}

def roll(data, row, axis, shift):
    if axis == 1:
        data[row, :] = np.roll(data[row, :], shift)
    else:
        data[:, row] = np.roll(data[:, row], shift)


def init_box():
    return np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

def make_ans(s):
    anser = ''
    for i in range(9):
        anser += str(s[i])
        if (i+1)%3 == 0 and i != 8:
            anser += '/'
    return anser

def resolve(data):
    box = init_box()

    for c in data:
        axis, row, shift = operations[c]
        roll(box, row, axis, shift)

    return make_ans(np.reshape(box, 9).ravel())


################
## test logic ##
################
class RESULT:
    success = 0
    fail = 0

RESULT.success = RESULT.fail = 0

def test(data, expect):
    print "actual:" + resolve(data) + " expected:" + expect
    if resolve(data) == expect:
        RESULT.success += 1
    else:
        RESULT.fail += 1

#################
test( "aegj", "286/435/971" )
test( "a", "231/456/789" )
test( "e", "183/426/759" )
test( "g", "123/456/978" )
test( "j", "126/459/783" )
test( "bb", "123/645/789" )
test( "jjj", "123/456/789" )
test( "bd", "723/164/589" )
test( "ah", "231/645/789" )
test( "bj", "124/569/783" )
test( "db", "723/561/489" )
test( "dh", "723/615/489" )
test( "dl", "123/456/789" )
test( "hc", "123/645/897" )
test( "gf", "128/453/976" )
test( "hl", "623/745/189" )
test( "ja", "261/459/783" )
test( "ld", "123/456/789" )
test( "ki", "315/486/729" )
test( "lfa", "294/753/186" )
test( "kga", "531/486/972" )
test( "dbi", "372/561/489" )
test( "che", "193/625/847" )
test( "iea", "823/416/759" )
test( "gbl", "523/964/178" )
test( "egj", "186/425/973" )
test( "jcf", "127/456/839" )
test( "djh", "726/915/483" )
test( "hld", "123/645/789" )
test( "leeh", "453/678/129" )
test( "heja", "851/629/743" )
test( "cakh", "251/649/837" )
test( "bhjik", "652/489/713" )
test( "eabji", "483/269/751" )
test( "cdbch", "823/156/974" )
test( "ckgajc", "536/492/817" )
test( "ggchha", "231/564/978" )
test( "gfbkeg", "128/534/697" )
test( "agfbcbf", "239/148/765" )
test( "ekahijf", "123/645/789" )
test( "hajdjbe", "789/432/615" )
test( "elgililj", "976/325/814" )
test( "chffefif", "317/629/845" )
test( "ilbbihak", "462/587/319" )
test( "abcdefghijkl", "123/456/789" )
test( "hkijbglfaced", "768/125/493" )
test( "dfkbjiechlga", "256/387/419" )
test( "hgfkbidlajce", "186/745/239" )
test( "baciefjhgkdl", "153/482/796" )

print "Success: {0.success}, Fail: {0.fail}".format(RESULT)
