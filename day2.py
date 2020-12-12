import fileinput
import re

f = open("input_2.txt")
file = f.read()
contents = file.splitlines()

rule = re.compile(r'(\d+)-(\d+) (\w): (\w*)', re.A)
count1 = 0
count2 = 0

for i in range(len(contents)):
    start, end, arg, body = re.match(rule, contents[i]).groups()
    start = int(start)
    end = int(end)
    if body.count(arg) in range(start, end+1):
        count1 += 1
    #1 indexed
    if (body[start-1] == arg) != (body[end-1] == arg):
        count2 += 1
print(count1)
print(count2)
