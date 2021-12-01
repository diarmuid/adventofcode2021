import gzip

with gzip.open("d1.txt.gz") as f:
    _fin = f.read()
    input = list(map(lambda x: int(x), _fin.splitlines()))
    # Part 1
    increasing_count = 0
    for i in range(len(input)-1):
        increasing_count += int(input[i] - input[i+1] < 0)

    print("Part1=",increasing_count)

    # Part 2
    prev_ave = None
    increasing_count = 0
    for i in range(len(input)):
        ave = sum(input[i:i+3])
        if prev_ave is not None:
            increasing_count += int(ave > prev_ave)
        prev_ave = ave
    print("Part2=", increasing_count)

