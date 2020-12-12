f = open("input_1.txt")
file = f.read()
contents = file.splitlines()
for i in range(len(contents)):
    contents[i] = int(contents[i])

for i in range(len(contents)):
    j = i
    for j in range(j, len(contents)):
        #print(contents[i]+contents[j])
        k=j
        for k in range(k, len(contents)):
            if contents[i]+contents[j]+contents[k] == 2020:
                print(contents[i]*contents[j]*contents[k])
