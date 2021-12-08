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


def to_codes(string):
    """Convert the string to ordered list"""
    return sorted(list(string))


def compare_codes(codes, string):
    """Compare the lists"""
    compare_list = sorted(list(string))
    if len(compare_list) != len(codes):
        return False
    if codes != compare_list:
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
    # There's gotta be a better way.
    # Fall through each letter and decoded them by bulding on previous decide
    for i in input_codes:
        if len(i) == 2:
            solutions[1] = to_codes(i)
        elif len(i) == 3:
            solutions[7] = to_codes(i)
        elif len(i) == 4:
            solutions[4] = to_codes(i)
        elif len(i) == 7:
            solutions[8] = to_codes(i)
    # We know 1,7,4,8. Use that to work out a few more
    for i in input_codes:
        if len(i) == 5: # 2,3 or 5
            is_match = True
            for _x in solutions[1]:
                if _x not in list(i):
                    is_match = False
            if is_match:
                solutions[3] = to_codes(i)
                continue

        if len(i) == 6: # 6 or 9 or 0
            is_match = True
            for _x in solutions[4]:
                if _x not in list(i):
                    is_match = False
            if is_match:
                solutions[9] = to_codes(i)
                continue
            is_match = True
            for _x in solutions[1]:
                if _x not in list(i):
                    is_match = False
            if is_match:
                solutions[0] = to_codes(i)
            else:
                solutions[6] = to_codes(i)
    # Only 2 or 5 left. Counmt the overlap with 6 and work out which is which
    for i in input_codes: # 2 or 5
        if len(i) == 5:  # 2 5
            if compare_codes(solutions[3], i):
                continue
            over_lap_with_6 = 0
            for c in solutions[6]:
                if c in list(i):
                    over_lap_with_6 += 1
            if over_lap_with_6 == 5:
                solutions[5] = to_codes(i)
            else:
                solutions[2] = to_codes(i)

    assert len(solutions) == 10, "Should have 10 solutions"

    decoded = []
    for output in output_values:
        for num in solutions:
            if compare_codes(solutions[num], output):
                decoded.append(num)
                continue
    combined = "".join((map(str, decoded)))
    decoded_out.append(combined)

solnpart2 = sum(map(lambda x: int(x), decoded_out))
print(solnpart2)
assert solnpart2 == 1043697, "Wrong p2"