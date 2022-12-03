with open('../Data/Day 1/input.txt') as f:
    t = f.readlines()
cals = [i.replace('\n','') for i in t]

cal_carried = 0
cal_max = 0
cal_totals = []
for cal in cals:
    if cal=='':
        cal_totals.append(cal_carried)
        cal=0
    if type(cal) is str:
        cal = int(cal)
    if cal == 0:
        cal_carried = 0
    cal_carried += cal
    if cal_carried > cal_max:
        cal_max = cal_carried

# P1
print(cal_max)
# P2
print(sum(sorted(cal_totals)[-3:]))