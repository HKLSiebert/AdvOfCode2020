content = open("input_6.txt", "r").read().split('\n\n')
print(content)

count1 = count2 = 0
for i in content:
    vals = i.split('\n')
    sets = map(set, vals)
    union = set.union(*sets)
    size = len(union)
    count1 += size

for i in content:
    vals = i.split('\n')
    sets = map(set, vals)
    intersect = set.intersection(*sets)
    size = len(intersect)
    count2 += size
print(count1, count2)
