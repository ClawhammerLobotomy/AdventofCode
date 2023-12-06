INPUT_FILE = 'd2_input.txt'
# INPUT_FILE = 'd2_test_input.txt'

with open(INPUT_FILE) as f:
    LINE_LIST = f.readlines()
p1_lookup = {
    "A":1, #Rock
    "B":2, #Paper
    "C":3, #Scissors
    "X":1, #Rock / Lose
    "Y":2, #Paper / Draw
    "Z":3  #Scissors / Win
}
p2_lookup = {
    "A":1, #Rock
    "B":2, #Paper
    "C":3, #Scissors
    "X":1, #Rock / Lose
    "Y":2, #Paper / Draw
    "Z":3  #Scissors / Win
}



score = 0
p2_score = 0
for l in LINE_LIST:
    opp, play = l.split()
    opp = p1_lookup[opp]
    play = p1_lookup[play]

    if opp==play: # Draw
        score += play + 3
    elif opp == 1:
        if play == 2:
            score += play + 6
        else:
            score += play
    elif opp == 2:
        if play == 3:
            score += play + 6
        else:
            score += play
    elif opp == 3:
        if play == 1:
            score += play + 6
        else:
            score += play


    if play == 2: # Draw
        p2_score += opp + 3
    elif play == 1: # Lose
        if opp == 1:
            play = 3
        elif opp == 2:
            play = 1
        else:
            play = 2
        p2_score += play
    elif play == 3: # Win
        if opp == 1:
            play = 2
        elif opp == 2:
            play = 3
        else:
            play = 1
        p2_score += play + 6

print(score)
# 12364 - too low
# 13924 - Correct

print(p2_score)
# 13448 - Correct
score = 0
p2_score = 0
for l in LINE_LIST:
    opp, play = l.split()
    opp, play = p1_lookup[opp], p1_lookup[play]
    #Modular math for part 1
    if opp == play: # Draw
        score += play + 3
    elif (opp % 3) == (play % 3 + 1) % 3: # Lose
        score += play 
    else: # Win
        score += play + 6
    
    # Part 2 doesn't work. Unsure the solution
    # Calculate player 2 score
    if play == 2:
        p2_score += opp + 3
    else:
        p2_score += (play % 3 + 2) % 3
print(score)
# 12364 - too low
# 13924 - Correct

print(p2_score)