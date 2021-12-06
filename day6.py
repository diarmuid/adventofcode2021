from collections import defaultdict

INPUT_TEST = 0
INPUT_REAL = 1
INPUT = ["3,4,3,1,2",
         "1,4,2,4,5,3,5,2,2,5,2,1,2,4,5,2,3,5,4,3,3,1,2,3,2,1,4,4,2,1,1,4,1,4,4,4,1,4,2,4,3,3,3,3,1,1,5,4,2,5,2,4," \
        "2,2,3,1,2,5,2,4,1,5,3,5,1,4,5,3,1,4,5,2,4,5,3,1,2,5,1,2,2,1,5,5,1,1,1,4,2,5,4,3,3,1,3,4,1,1,2,2,2,5,4,4," \
        "3,2,1,1,1,1,2,5,1,3,2,1,4,4,2,1,4,5,2,5,5,3,3,1,3,2,2,3,4,1,3,1,5,4,2,5,2,4,1,5,1,4,5,1,2,4,4,1,4,1,4,4," \
        "2,2,5,4,1,3,1,3,3,1,5,1,5,5,5,1,3,1,2,1,4,5,4,4,1,3,3,1,4,1,2,1,3,2,1,5,5,3,3,1,3,5,1,5,3,5,3,1,1,1,1,4," \
        "4,3,5,5,1,1,2,2,5,5,3,2,5,2,3,4,4,1,1,2,2,4,3,5,5,1,1,5,4,3,1,3,1,2,4,4,4,4,1,4,3,4,1,3,5,5,5,1,3,5,4,3," \
        "1,3,5,4,4,3,4,2,1,1,3,1,1,2,4,1,4,1,1,1,5,5,1,3,4,1,1,5,4,4,2,2,1,3,4,4,2,2,2,3"]

# AFter 18 and 80 days
TEST_ANS = [26, 5934]


test_num = INPUT_REAL


class Population(object):
    def __init__(self, instring: str):
        self._population_by_age = [0] * 9  # Just keep a count of the number of fish of that age
        for age in instring.split(","):
            self._population_by_age[int(age)] += 1

    def add_day(self, count: int=1):
        # There's probably a more compact way of writing this
        for d in range(count):
            new_population = [0] * 9
            new_population[8] = self._population_by_age[0]
            for i in range(8, 0, -1):
                new_population[(i - 1)] = self._population_by_age[i]
            new_population[6] += self._population_by_age[0]
            self._population_by_age = new_population

    def tot_population(self):
        return sum(self._population_by_age)


population = Population(INPUT[test_num])

population.add_day(80)
print(population.tot_population())
assert population.tot_population() == 349549, "Wrong"

# P2
population.add_day(256-80)
print(population.tot_population())
assert population.tot_population() == 1589590444365, "Wrong"