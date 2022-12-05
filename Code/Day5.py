with open('../Data/Day 5/input.txt') as f:
    t = f.readlines()
s = [i.replace('\n','') for i in t]

# cleaning and formatting

split = s.index('')
stacks = s[:split]
stacks = [s + (' '*(35-len(s))) for s in stacks]
instructions = s[split+1:]

idx_start = [[*stacks[-1]].index(str(x))-1 for x in range(1,(len(stacks)+1))]
idx_end = [i-1 for i in idx_start[1:]]
idx_end.append(len([*stacks[-1]]))

lol_stacks = [[stacks[l][idx_start[i]:idx_end[i]] for i in range(len(stacks))] for l in range(len(stacks))]
t_lol_stacks = list(map(list, zip(*lol_stacks)))

stacks_clean = [[v for v in stack if v != '   '] for stack in t_lol_stacks]


# P1

for index in range(len(instructions)):
    containers_moved = int(instructions[index].split(' from ')[0].split(' ')[1])
    frm, to = [(int(i) - 1) for i in instructions[index].split(' from ')[1].split(' to ')]
    for i in range(containers_moved):
        popped_crate = stacks_clean[frm][0]
        stacks_clean[frm].pop(0)
        stacks_clean[to] = [popped_crate] + stacks_clean[to]  
print(''.join([i[1] for i in list(map(list, zip(*stacks_clean)))[0]]))

# P2
stacks_clean = [[v for v in stack if v != '   '] for stack in t_lol_stacks]
for index in range(len(instructions)):
    containers_moved = int(instructions[index].split(' from ')[0].split(' ')[1])
    frm, to = [(int(i) - 1) for i in instructions[index].split(' from ')[1].split(' to ')]
    popped_crates = stacks_clean[frm][:containers_moved]
    del stacks_clean[frm][:containers_moved]
    stacks_clean[to] = popped_crates + stacks_clean[to]
print(''.join([i[1] for i in list(map(list, zip(*stacks_clean)))[0]]))