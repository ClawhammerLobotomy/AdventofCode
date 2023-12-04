import re

in_f = 'd1_input.txt'
in_f = 'Ryan_d1_input.txt'


def part_1():
    with open(in_f, 'r') as f:
        lines = f.readlines()
        calibration_no = sum([int(f'{nums[0]}{nums[-1]}') for nums in [re.findall(r'\d',l) for l in lines]])
        print(calibration_no)


"""
Examples from the site
two1nine            29
eightwothree        83
abcone2threexyz     13
xtwone3four         24
4nineeightseven2    42
zoneight234         14
7pqrstsixteen       76
"""
def part_2():
    """
    This did not work due to how regex pattern matching handles overlaps. 
    eightwothree becomes 8wo3 but we should end with 823
    """
    rep = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    pattern = re.compile("|".join(rep.keys()))
    
    with open(in_f,'r') as f:
        lines = f.readlines()
        # lines = [
        #     'two1nine',
        #     'eightwothree',
        #     'abcone2threexyz',
        #     'xtwone3four',
        #     '4nineeightseven2',
        #     'zoneight234',
        #     '7pqrstsixteen'
        # ]
        numlines = [pattern.sub(lambda m: rep[m.group(0)], line) for line in lines]
        numbers = [re.findall(r'\d',l) for l in numlines]
        calibration_no_list = [int(f'{nums[0]}{nums[-1]}') for nums in numbers]
        calibration_no = sum(calibration_no_list)
        print(calibration_no)
part_1()
part_2()

def part_2_1():
    """
    This method uses a regex capturing group inside a lookahead to match overlaps.
    With the capturing group, the match is technically the zero width string before the pattern, so they do not overlap.
    This allows eightwothree to match eight, two, and three separately.
    Then these can be added to a list or string which can be substituted like the previous attempt.
    """
    with open(in_f,'r') as f:
        lines = f.readlines()
        # lines = [
        #     'two1nine',
        #     'eightwothree',
        #     'abcone2threexyz',
        #     'xtwone3four',
        #     '4nineeightseven2',
        #     'zoneight234',
        #     '7pqrstsixteen'
        # ]
        repl = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
        }
        repl_pat = re.compile("|".join(repl.keys()))
        find_pat =r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))"
        matches = [''.join(re.findall(find_pat,l)) for l in lines]
        numlines = [repl_pat.sub(lambda m: repl[m.group(0)], mat) for mat in matches]
        numbers = [re.findall(r'\d',l) for l in numlines]
        calibration_no_list = [int(f'{nums[0]}{nums[-1]}') for nums in numbers]
        calibration_no = sum(calibration_no_list)
        print(calibration_no)
part_2_1()