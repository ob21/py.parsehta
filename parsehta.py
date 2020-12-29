import petl as etl

table1 = etl.fromtext('tension.md')

print(table1)

for line in open("tension.md"):
    if line.strip() :
        print("line>" + line.strip())
