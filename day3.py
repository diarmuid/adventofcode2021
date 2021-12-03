import gzip
import logging

logging.basicConfig(level=logging.DEBUG)

with gzip.open("d3.txt.gz", 'rt') as f:
    # Setup
    _fin = f.read()
    all_lines = list(map(lambda x: x.strip(), _fin.splitlines()))
    # Get some key features
    bit_count = len(all_lines[0])
    mask = pow(2, bit_count) - 1
    line_count = len(all_lines)

    # Part 1.
    gama_b = ""
    epsilon_b = ""
    for bposn in range(bit_count):
        _vert_line = map(lambda x: int(x[bposn]), all_lines)  # Extract each vertical line as integers
        tot_count = sum(_vert_line)  # Add them up.
        logging.debug("bitpos={} count={}".format(bposn, tot_count))
        gama_b += str(int(tot_count > (line_count//2)))  # Most common => more than half

    epsilon_b = "{:0{bit_count}b}".format(~int(gama_b, 2) & mask, bit_count=bit_count)  # Invert it
    logging.debug("E={} G={}".format(epsilon_b, gama_b))
    gama = int(gama_b, 2)  # To integers
    epsilon = int(epsilon_b, 2)
    print("G={} E={} Mult={}".format(gama, epsilon, gama * epsilon))