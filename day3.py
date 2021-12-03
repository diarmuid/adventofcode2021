import gzip
import logging

logging.basicConfig(level=logging.INFO)

CO2 = 0
O2 = 1


def filter_list(all_lines, gen_sel):
    """
    Take all the lines and the which gas to detect
    :param all_lines:
    :param gen_sel: 0 | 1
    :return:
    """
    bposn = 0
    filtered_list = all_lines
    iterate = True

    while iterate:
        # Same as port 1
        _vert_line = map(lambda x: int(x[bposn]), filtered_list)
        tot_count = sum(_vert_line)
        tot_count_n = len(filtered_list) - tot_count
        # Create my filters. One is the inverse of the other
        filters = {O2: str(int(tot_count >= tot_count_n)), CO2: str(int(tot_count < tot_count_n))}
        filter_bit = filters[gen_sel] # Which filter do we want
        # Now reduce my list by filtering on the position and the bit selected
        filtered_list = list(filter(lambda x: x[bposn] == filter_bit, filtered_list))
        logging.debug("ListLen={} Bposn={} Filterb={}".format(len(filtered_list), bposn, filter_bit))
        if len(filtered_list) == 1 or bposn == bit_count - 1:
            iterate = False
        else:
            bposn += 1
    return filtered_list


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

    # part 2
    o2_list = filter_list(all_lines, O2)#
    co2_list = filter_list(all_lines, CO2)
    res = int(o2_list[0], 2) * int(co2_list[0], 2)
    print("mult={}".format(res))
    if res != 3832770:
        raise Exception("Wrong answer")