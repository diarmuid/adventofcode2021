import gzip
import logging

logging.basicConfig(level=logging.INFO)

# Fall into old habits. Create a class for the board


class Board(object):
    def __init__(self, lines):
        self._rows = []
        self._cols = [[] for i in range(5)]
        self._parse_input(lines)
        self.count_to_check = None
        self.called_num = None
        self.magic_score = None

    def _parse_input(self, lines):
        """Put the input into rows and cols"""
        for l in lines:
            remove_newline = l.strip()  # remove new line
            l_as_ints = list(map(lambda x: int(x), remove_newline.split()))
            self._rows.append(l_as_ints)
            for col_idx, v in enumerate(l_as_ints):
                self._cols[col_idx].append(v)

    def verify_lines(self, checks):
        """Verify rows and cols for the win by removing items"""
        for count, c in enumerate(checks):
            for r_idx in range(len(self._rows)):
                if c in self._rows[r_idx]:
                    self._rows[r_idx].remove(c)
                if len(self._rows[r_idx]) == 0:
                    logging.debug("Row Win Val={} Count={}".format(c, count+1))
                    self._calc_magic(count + 1, c)
                    return True
            # I didn't read the challenged and missed that bingo worked on rows too
            # So looks a bit verbose
            for c_idx in range(len(self._cols)):
                if c in self._cols[c_idx]:
                    self._cols[c_idx].remove(c)
                if len(self._cols[c_idx]) == 0:
                    logging.debug("Col Win Val={} Count={}".format(c, count + 1))
                    self._calc_magic(count + 1, c)
                    return True

        return False

    def _calc_magic(self, count,  call):
        self.count_to_check = count
        self.called_num = call
        _row_sum = 0
        for r in self._rows:
            for c in r:
                _row_sum += c
        self.magic_score = self.called_num * _row_sum

    def __repr__(self):
        return "Count_to_win={} Called={} Score={}".format(self.count_to_check, self.called_num, self.magic_score)


def get_win_count(obj: Board) :
    return obj.count_to_check


# Read the input
f = gzip.open("d4.txt.gz", 'rt')
all_lines = f.readlines()
f.close()
check_line = all_lines.pop(0)
verify_nums = list(map(lambda x: int(x), check_line.split(",")))
all_lines.pop(0)  # Strip first newine

# Create the boards
boards = []
board_lines =[]
for l in all_lines:
    if l == "\n":
        boards.append(Board(board_lines))
        board_lines = []
    else:
        board_lines.append(l)

# Part 1
for b in boards:
    verify = b.verify_lines(verify_nums)
    if not verify:
        raise Exception("Board did not verify")

win_board = sorted(boards, key=get_win_count)[0]
print(repr(win_board))
if win_board.magic_score != 54275:
    raise Exception("Wrong answer")

# Part 2 just fell out! BOOM
lose_board = sorted(boards, key=get_win_count)[-1]
print(repr(lose_board))
if lose_board.magic_score != 13158:
    raise Exception("Wrong answer")