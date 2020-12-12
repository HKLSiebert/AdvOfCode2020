#This doesn't work and I don't know why!
contents = open("input_3.txt", "r").read().splitlines()
y = len(contents[0])

totalCount = 1
toCheck = [[1, 1], [3, 1], [5, 1], [7,1], [1, 2]]
answers = []
for j in range(len(toCheck)):
    xVal = toCheck[j][0]
    yVal = toCheck[j][1]
    count = 0
    for i in range(len(contents)//yVal):
        row = i * yVal
        col = (i * xVal) % y
        if contents[row][col] == "#":
            count += 1
    print(count)
    answers.append(count)
print(answers)

for val in answers:
    totalCount *= val

print(totalCount)
