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
running_cost = 0


for i, l in enumerate(RealInput.RealInput.DAY10.splitlines()):
    keep_iterating = True
    modified_line = l
    while keep_iterating:
        m = illegal_bkts.search(modified_line)
        if m:
            (openb, closeb) = list(m.group(1))
            logging.debug("{}:{}:{}:{}".format(i, m.start(), m.group(), COSTS[closeb] * m.start()))
            running_cost += COSTS[closeb]
            keep_iterating = False
        else:
            (modified_line, subsmade) = brks.subn("", modified_line)
            if subsmade == 0:
                keep_iterating = False
print(running_cost)
assert running_cost == 388713, "wrong p1"