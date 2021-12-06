

test_input= "3,4,3,1,2"
real_input = "1,4,2,4,5,3,5,2,2,5,2,1,2,4,5,2,3,5,4,3,3,1,2,3,2,1,4,4,2,1,1,4,1,4,4,4,1,4,2,4,3,3,3,3,1,1,5,4,2,5,2,4," \
             "2,2,3,1,2,5,2,4,1,5,3,5,1,4,5,3,1,4,5,2,4,5,3,1,2,5,1,2,2,1,5,5,1,1,1,4,2,5,4,3,3,1,3,4,1,1,2,2,2,5,4,4," \
             "3,2,1,1,1,1,2,5,1,3,2,1,4,4,2,1,4,5,2,5,5,3,3,1,3,2,2,3,4,1,3,1,5,4,2,5,2,4,1,5,1,4,5,1,2,4,4,1,4,1,4,4," \
             "2,2,5,4,1,3,1,3,3,1,5,1,5,5,5,1,3,1,2,1,4,5,4,4,1,3,3,1,4,1,2,1,3,2,1,5,5,3,3,1,3,5,1,5,3,5,3,1,1,1,1,4," \
             "4,3,5,5,1,1,2,2,5,5,3,2,5,2,3,4,4,1,1,2,2,4,3,5,5,1,1,5,4,3,1,3,1,2,4,4,4,4,1,4,3,4,1,3,5,5,5,1,3,5,4,3," \
             "1,3,5,4,4,3,4,2,1,1,3,1,1,2,4,1,4,1,1,1,5,5,1,3,4,1,1,5,4,4,2,2,1,3,4,4,2,2,2,3"


class Fish(object):
    def __init__(self, age):
        self.age = age

    def add_day(self):
        r_fish = None
        if self.age == 0:
            self.age = 6
            r_fish = Fish(8)
        else:
            self.age -= 1
            return None


#set up
all_fish = []
for age in test_input.split(","):
    all_fish.append(Fish(int(age)))

_new_fish = []
for day in range(18):
    for f in all_fish:
        newf = f.add_day()
        if newf is not None:
            _new_fish.append(newf)
    all_fish += _new_fish

print(len(all_fish))
assert len(all_fish) == 26, "Should have 26 fish but got {}".format(len(all_fish))
