import re

count = count2 = 0
req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opts = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

content = [row.strip() for row in open('input_4.txt').readlines()]

passport = {}
passports = []
for line in content:
    if not line:
        passports.append(passport)
        passport = {}
        continue
    pairs = line.split(' ')
    for piece in pairs:
        key, val = piece.split(':')
        passport[key] = val
if passport:
    passports.append(passport)

for i in range(len(passports)):
    valid = True
    for j in range(len(req)):
        if not req[j] in passports[i]:
            valid = False
    if valid:
        count += 1
        valid2 = True
        byr = passports[i]['byr']
        if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
            valid2 = False
        iyr = passports[i]['iyr']
        if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
            valid2 = False
        eyr = passports[i]['eyr']
        if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
            valid2 = False
        hgt = passports[i]['hgt']
        if hgt.endswith('cm'):
            hgt = hgt.strip('cm')
            if not 150 <= int(hgt) <= 193:
                valid2 = False
        elif hgt.endswith('in'):
            hgt = hgt.strip('in')
            if not 59 <= int(hgt) <= 76:
                valid2 = False
        else:
            valid2 = False
        hcl = passports[i]['hcl']
        if not re.match('#[0-9a-f]{6}', hcl):
            valid2 = False
        ecl = passports[i]['ecl']
        if ecl not in opts:
            valid2 = False
        pid = passports[i]['pid']
        if not re.match('^[0-9]{9}$', pid):
            valid2 = False
        if valid2:
            count2 +=1
print(count)
print(count2)
