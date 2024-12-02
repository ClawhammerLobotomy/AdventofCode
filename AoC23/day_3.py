import re

INPUT_FILE = 'd3_input.txt'
# INPUT_FILE = 'd3_test_input.txt'
# INPUT_FILE = 'd3_test.txt'
PART_PATTERN = r'[0-9]+'
SYMBOL_PATTERN = r'[^.0-9]'
GEAR_PATTERN = r'\*'
LINE_LENGTH = 140
# LINE_LENGTH = 10

class Line:
    def __init__(self,index,line,**kwargs):
        self.index = index
        self.line = line
        self.valid_parts = []
        self.valid_gears = []
        self.valid_gear_parts = []
        self.__dict__.update(kwargs)
        self.part_check(self.line)
        self.gear_check(self.line)


    def part_check(self, lines):
        prev_symbols = [x.span() for x in re.finditer(SYMBOL_PATTERN,lines[0])]
        prev_start = [x[0] for x in prev_symbols]
        cur_symbols = [x.span() for x in re.finditer(SYMBOL_PATTERN,lines[1])]
        cur_parts = [Part(x) for x in re.finditer(PART_PATTERN,lines[1])]
        cur_start = [x[0] for x in cur_symbols]
        next_symbols = [x.span() for x in re.finditer(SYMBOL_PATTERN,lines[2])]
        next_start = [x[0] for x in next_symbols]
        for part in cur_parts:
              part_start = part.part_pos[0]
              part_end = part.part_pos[1]
              start_check = any(
                    [x for x in prev_start if part_start in range(x-1,x+2)]+
                    [x for x in cur_start if part_start in range(x,x+2)]+
                    [x for x in next_start if part_start in range(x-1,x+2)]
                    )
              end_check = any(
                    [x for x in prev_start if part_end in range(x,x+2)]+
                    [x for x in cur_start if part_end in range(x,x+2)]+
                    [x for x in next_start if part_end in range(x,x+2)]
                    )
              if any([start_check,end_check]):
                    self.valid_parts.append(int(part.part_no))


    def gear_check(self,lines):
        prev_parts = [Part(x) for x in re.finditer(PART_PATTERN,lines[0])] 
        cur_parts = [Part(x) for x in re.finditer(PART_PATTERN,lines[1])]
        cur_gears = [Gear(x) for x in re.finditer(GEAR_PATTERN,lines[1])]
        next_parts = [Part(x) for x in re.finditer(PART_PATTERN,lines[2])]
        for gear in cur_gears:
              gear_start = gear.gear_pos[0]
              gear_parts = \
                    [x.part_no for x in prev_parts if gear_start in range(x.part_pos[0]-1,x.part_pos[1]+1)]+\
                    [x.part_no for x in cur_parts if gear_start in range(x.part_pos[0]-1,x.part_pos[1]+1)]+\
                    [x.part_no for x in next_parts if gear_start in range(x.part_pos[0]-1,x.part_pos[1]+1)]

              if len(gear_parts) == 2:
                    self.valid_gears.append(int(gear_parts[0])*int(gear_parts[1]))
                    self.valid_gear_parts.append([gear_parts[0],gear_parts[1]])


class Part:
    def __init__(self, part):
          self.part_no = part.group(0)
          self.part_pos = part.span()

class Gear:
      def __init__(self, gear):
        self.gear_pos = gear.span()


def previous_current_next(iterable):
    """Make an iterator that yields an (previous, current, next) tuple per element.

    Returns None if the value does not make sense (i.e. previous before
    first and next after last).
    """
    iterable = iter(iterable)
    prv = '.' * LINE_LENGTH
    cur = next(iterable)
    try:
        while True:
            nxt = next(iterable)
            yield (prv, cur, nxt)
            prv = cur
            cur = nxt
    except StopIteration:
        yield (prv, cur, '.' * LINE_LENGTH)


with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
    lines = list(previous_current_next([l.strip() for l in lines]))
    line_classes = [Line(i,l) for i,l in enumerate(lines)]
    valid_parts = [x.valid_parts for x in line_classes]
    part_list = [item for sublist in valid_parts for item in sublist]
    engine_sum = sum(part_list)
    valid_gears = [x.valid_gears for x in line_classes]
    gear_list = [item for sublist in valid_gears for item in sublist]
    gear_sum = sum(gear_list)
    print(engine_sum)
    print(gear_sum)


# engine_sum
# 534618 - too high
# 528799 - Correct

# gear_sum
# 63688764 - too low
# 63433394 - too low
# 69813108 - too low
# 84907174 - Correct