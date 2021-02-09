

with open("tension.md") as file:
    lines = file.readlines()
iterator = filter(lambda line: line.strip(), lines)
entries = [entry.split() for entry in list(iterator)]

entries = reversed(entries)

for entry in entries:
    line = ""
    for item in entry:
        line = line + item + " "
    print(line)
    print("")