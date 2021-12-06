import logging


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

TIME_LEN = {80 : 349549}

test_num = INPUT_REAL


class Fish(object):
    def __init__(self, age):
        self.age = age

    def add_day(self):
        r_fish = None
        if self.age == 0:
            self.age = 6
            r_fish = Fish(8)
            return r_fish
        else:
            self.age -= 1
            return None


for len_time, exp_ans in TIME_LEN.items():
    all_fish = []
    for age in INPUT[test_num].split(","):
        all_fish.append(Fish(int(age)))
    for day in range(len_time):
        _new_fish = []
        for f in all_fish:
            newf = f.add_day()
            if newf is not None:
                logging.debug("New fish created")
                _new_fish.append(newf)
        all_fish += _new_fish

    print("Length = {} NumFish={}".format(len_time, len(all_fish)))
    assert len(all_fish) == exp_ans, "Should have {} fish but got {}".format(exp_ans, len(all_fish))

# Part 2 needs a maths and shoulld have been part 1
