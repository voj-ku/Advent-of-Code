with open('../Data/Day 3/input.txt') as f:
    t = f.readlines()
s = [i.replace('\n','') for i in t]

def get_priority(val):
    if val.isupper():
        priority = ord(v) - 38
    else:
        priority = ord(v) - 96
    return priority

# P1

priorities = []
for st in s:
    comp1 = st[:int(len(st)/2)]
    comp2 = st[int(len(st)/2):]
    v = list(set([*comp2]).intersection(set([*comp1])))[0]
    priorities.append(get_priority(v))
sum(priorities)

# P2

s2 = [s[i: i+3] for i in range(0, len(s), 3)]
priorities = []
for st in s2:
    comp1 = st[:int(len(st)/2)]
    comp2 = st[int(len(st)/2):]
    v = list(set(st[0]) & set(st[1]) & set(st[2]))[0]
    priorities.append(get_priority(v))
sum(priorities)