content = open("input_5.txt", "r").read().split()
print(content)

seats = set((int(line.translate("".maketrans("FLBR", "0011")), 2) for line in content))
start = min(seats)
end = max(seats)
print("Max: " + str(max(seats)))
print("Missing: " + str(set(range(start, end)) - seats))
