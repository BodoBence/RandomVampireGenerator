#for small stuff

shit_1 = {'A': 'A1', 'B': 'B1', 'C': {'na': 1}}
shit_2 = {'A': 'A1', 'B': 'B1'}
hist_table = [shit_1, shit_2]

for test in hist_table:
    test['C']['my_shit'] = 3

print(hist_table)
