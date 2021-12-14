import re
import RealInput
from collections import namedtuple, Counter

Rule = namedtuple("Rule", ["pair", "ins"])


class Polymer(object):
    def __init__(self, as_string):
        self._as_string = as_string
        self._pairs = []
        self._to_pairs(as_string)
        self._intermediate = None

    def _to_pairs(self, _string):
        for i in range(0, len(_string)-1):
            self._pairs.append(_string[i:i+2])

    def add_rule(self, rule: Rule):
        for i,p in enumerate(self._pairs):
            if len(p) !=2:
                continue
            if p == rule.pair:
                _split = list(rule.pair)
                self._pairs[i] = _split[0]+rule.ins+_split[1]

    def apply_step(self):
        self._as_string = ""
        for i, p in enumerate(self._pairs):
            self._as_string += p
            if i != len(self._pairs)-1:
                self._as_string = self._as_string[:-1]
        self._pairs = []
        self._to_pairs(self._as_string)

    def __repr__(self):
        return self._as_string


data_in = RealInput.RealInput.DAY14
poly = Polymer(data_in.splitlines(keepends=False)[0])
rules = []
for l in data_in.splitlines(keepends=False)[2:]:
    (_pair, _ins) = l.split(" -> ")
    rules.append(Rule(_pair, _ins))

steps = 10
for s in range(steps):
    for rule in rules:
        poly.add_rule(rule)
    poly.apply_step()
    to_count = Counter(list(repr(poly)))
    sort_count = sorted(to_count.values(), reverse=True)
    print("{},{}".format(s, sort_count[0] - sort_count[-1]))

    #print(poly)

#assert len(repr(poly))==3073, "wrong"
#to_count = Counter(list(repr(poly)))
#sort_count = sorted(to_count.values(), reverse=True)
#print(sort_count[0] - sort_count[-1])

#y = 2425216000 + (40.2906 - 2425216000)/(1 + (x/81.7808)^6.39633)
steps = 40
predict = 2425216000 + (40.2906 - 2425216000)/(1 + pow(steps/81.7808, 6.39633))
print(predict)
#24754299
