import RealInput
from collections import namedtuple, defaultdict

Rule = namedtuple("Rule", ["matchpair", "incpair", "incpair2"])

# The data can be represented as very limited number of pairs
# when splitting a protein, you remove the original and replace
# it with two others


def string_to_dict(str):
    pair_counts = defaultdict(int)
    for i in range(len(str) - 1):
        pair_counts[str[i:i + 2]] += 1
    return pair_counts


def print_dict_pairs(pairs: dict):
    for c, v in sorted(pairs.items()):
        if v > 0:
            print("{}:{} ".format(c, v), end="")
    print("")


def pair_count_to_counter(pair_counts):
    counter = defaultdict(int)
    for p, v in pair_counts.items():
        if v > 0:
            letters = list(p)
            counter[letters[0]] += v
    return counter


data_in = RealInput.RealInput.DAY14
pair_counts = string_to_dict(data_in.splitlines(keepends=False)[0])
last_letter = list(data_in.splitlines(keepends=False)[0])[-1]

rules = []
for l in data_in.splitlines(keepends=False)[2:]:
    (_pair, _ins) = l.split(" -> ")
    rules.append(Rule(_pair, _pair[0]+_ins, _ins+_pair[1]))

steps = 40
for s in range(steps):
    _delta = defaultdict(int)
    for p in pair_counts:
        for r in rules:
            if p == r.matchpair and pair_counts[p] > 0:
                _delta[r.incpair] += pair_counts[p]
                _delta[r.incpair2] += pair_counts[p]
                _delta[r.matchpair] -= pair_counts[p]
    for _p, change in _delta.items():
        pair_counts[_p] = max(0, pair_counts[_p] + change)

#work out answer
pairs_counted = pair_count_to_counter(pair_counts)
pairs_counted[last_letter] += 1
counts = sorted(pairs_counted.items(), key=lambda item: item[1])
p2_ans = abs(counts[-1][1] - counts[0][1])
print(p2_ans)
assert p2_ans == 3906445077999, "wrong p2"
