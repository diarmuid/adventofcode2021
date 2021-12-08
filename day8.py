import re


fname = "d8.txt"
f = open(fname)
output_values = []
input_codes = []
for l in f.readlines():
    (pre, pos) = l.split("|")
    for m in re.findall(r"(\w+)", pos):
        output_values.append(m)
    for m in re.findall(r"(\w+)", pre):
        input_codes.append(m)
f.close()

Digits = {1: 0, 4: 0, 7: 0, 8: 0}
LenDigits = {1: 2, 4: 4, 7: 3, 8: 7}
for val in output_values:
    for d in Digits.keys():
        if LenDigits[d] == len(val):
            Digits[d] += 1
solnpart1 = sum(Digits.values())
print(solnpart1)
assert solnpart1 == 416, "wrong p1"


class DigitCode(object):
    def __init__(self, num, string):
        self.num = num
        self.codes = sorted(list(string))

    def match(self, string):
        compare_list = sorted(list(string))
        if len(compare_list) != len(self.codes):
            return False
        if self.codes != compare_list:
            return False
        return True

fname = "d8.txt"
decoded_out = []
f = open(fname)

for l in f.readlines():
    output_values = []
    input_codes = []
    (pre, pos) = l.split("|")
    for m in re.findall(r"(\w+)", pos):
        output_values.append(m)
    for m in re.findall(r"(\w+)", pre):
        input_codes.append(m)

    solutions = {}
    # There's gotta be a better way
    for i in input_codes:
        if len(i) == 2:
            solutions[1] = DigitCode(1, i)
        elif len(i) == 3:
            solutions[7] = DigitCode(7, i)
        elif len(i) == 4:
            solutions[4] = DigitCode(4, i)
        elif len(i) == 7:
            solutions[8] = DigitCode(8, i)
    for i in input_codes:
        if len(i) == 5: # 2,3 or 5
            is_match = True
            for _x in solutions[1].codes:
                if _x not in list(i):
                    is_match = False
            if is_match:
                solutions[3] = DigitCode(3, i)
                continue

        if len(i) == 6: # 6 or 9 or 0
            is_match = True
            for _x in solutions[4].codes:
                if _x not in list(i):
                    is_match = False
            if is_match:
                solutions[9] = DigitCode(9, i)
                continue
            is_match = True
            for _x in solutions[1].codes:
                if _x not in list(i):
                    is_match = False
            if is_match:
                solutions[0] = DigitCode(0, i)
            else:
                solutions[6] = DigitCode(6, i)

    for i in input_codes: # 2 or 5
        if len(i) == 5:  # 2 5
            if solutions[3].match(i):
                continue
            over_lap_with_6 = 0
            for c in solutions[6].codes:
                if c in list(i):
                    over_lap_with_6 += 1
            if over_lap_with_6 == 5:
                solutions[5] = DigitCode(5, i)
            else:
                solutions[2] = DigitCode(2, i)

    assert len(solutions) == 10, "Should have 10 solutions"

    decoded = []
    for output in output_values:
        for v in solutions.values():
            if v.match(output):
                decoded.append(v.num)
                continue
    combined = "".join((map(str, decoded)))
    #print(combined)
    decoded_out.append(combined)
    #assert combined == str(5353)

solnpart2 = sum(map(lambda x: int(x), decoded_out))
print(solnpart2)
assert solnpart2 == 1043697, "Wrong p2"