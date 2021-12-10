import RealInput
import re
import logging


#brks = re.compile(r"((?:\[\])|(?:\(\))|(?:{})|(?:<>))")
brks = re.compile(r"(\[\]|\(\)|{}|<>)")
illegal_bkts = re.compile(r"(\[}|\[\)|\[>|"
                          r"{\]|{\)|{>|"
                          r"\(\]|\(}|\(>|"
                          r"<\]|<\)|<})")
COSTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
CORRECTION_COST = {"(": 1, "[": 2, "{": 3, "<": 4}

running_cost = 0
replacement_scores = []

for i, l in enumerate(RealInput.RealInput.DAY10.splitlines()):
    keep_iterating = True
    modified_line = l
    incomplete = True
    while keep_iterating:
        m = illegal_bkts.search(modified_line)
        if m:
            (openb, closeb) = list(m.group(1))
            logging.debug("{}:{}:{}:{}".format(i, m.start(), m.group(), COSTS[closeb] * m.start()))
            running_cost += COSTS[closeb]
            keep_iterating = False
            incomplete = False
        else:
            (modified_line, subsmade) = brks.subn("", modified_line)
            if subsmade == 0:
                keep_iterating = False
    # Part 2
    if len(modified_line) > 0 and incomplete:
        brks_to_add = reversed(list(modified_line))
        fix_score = 0
        for addition in brks_to_add:
            fix_score *= 5
            fix_score += CORRECTION_COST[addition]
        replacement_scores.append(fix_score)

replacement_scores = sorted(replacement_scores)
middle = replacement_scores[len(replacement_scores)//2]

print(middle)
assert running_cost == 388713, "wrong p1"
#assert running_cost == 26397, "wrong p1"
assert middle == 3539961434, "wrongp2"