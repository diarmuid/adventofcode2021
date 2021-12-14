import re
import RealInput
from collections import namedtuple, Counter, defaultdict

Rule = namedtuple("Rule", ["matchpair", "incpair", "incpair2"])


def string_to_dict(str):
    pair_counts =  defaultdict(int)
    for i in range(len(str) - 1):
        if str[i:i + 2] not in pair_counts:
            pair_counts[str[i:i + 2]] = 0
        pair_counts[str[i:i + 2]] += 1
    return  pair_counts


def pair_count_to_counter(pair_counts):
    counter = defaultdict(int)
    for p,v in pair_counts.items():
        if v > 0:
            letters = list(p)
            for l in letters:
                counter[l] += v
    return counter


data_in = RealInput.RealInput.DAY14TST
tst_results =["NCNBCHB", "NBCCNBBBCBHCB", "NBBBCNCCNBBNBNBBCHBHHBCHB", "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"]
pair_counts = string_to_dict(data_in.splitlines(keepends=False)[0])

rules = []
for l in data_in.splitlines(keepends=False)[2:]:
    (_pair, _ins) = l.split(" -> ")
    rules.append(Rule(_pair, _pair[0]+_ins, _ins+_pair[1]))

steps = 4
for s in range(steps):
    _delta = defaultdict(int)
    for p in pair_counts:
        for r in rules:
            if p == r.matchpair:
                _delta[r.incpair] += 1
                _delta[r.incpair2] += 1
                _delta[r.matchpair] -= 1
    for _p, change in _delta.items():
        if pair_counts[_p] + change >= 0:
            pair_counts[_p] += change
        else:
            pair_counts[_p] = 0

    print(pair_counts)
    print(string_to_dict(tst_results[s]))
    print(sum(pair_counts.values())+1)

print(sum(pair_counts.values()) + 1)
print(pair_count_to_counter(pair_counts))
pass
