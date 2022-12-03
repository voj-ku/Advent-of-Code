with open('../Data/Day 2/input.txt') as f:
    t = f.readlines()
games = [i.replace('\n','') for i in t]


# P1

def outcome_points(input):

    val1, val2 = input.split()
    r1 = ord(val1) % 64
    r2 = ord(val2) % 87
    if r1==r2: 
        return 3 + r2, 'draw'
    if (r2-r1) in (1,-2): 
        return 6 + r2, 'win'
    else: 
        return 0 + r2, 'lose'

r = sum([outcome_points(g)[0] for g in games])
print(r)


# P2

def played_choice(input):

    val1, val2 = input.split()
    r1 = ord(val1) % 64
    
    if val2=='Y': # draw
        r2 = r1
    if val2=='X': # lose
        if r1>1:
            r2 = r1-1
        else:
            r2 = r1+2
    if val2=='Z': # win
        if r1<3:
            r2 = r1+1
        else:
            r2 = r1-2
    outcome_score = ((ord(val2) % 88) * 3)
    return r2 + outcome_score

r = sum([played_choice(g) for g in games])
print(r)

r = sum([played_choice(g) for g in games])
print(r)