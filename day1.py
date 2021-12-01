#Day1 1
with open("d1.txt") as f:
    _fin = f.read()
    input = list(map(lambda x: int(x), _fin.splitlines()))
    increasing_count = 0
    rolling_count = 0
    for i in range(len(input)-1):
        if input[i] - input[i+1] < 0:
            increasing_count += 1

    print("Part1=",increasing_count)
    prev = None
    increasing_count = 0
    for i in range(len(input)):
        val = sum(input[i:i+3])
        if prev is not None:
            increasing_count += int(val>prev)
        prev = val
    print("Part2=", increasing_count)

