import petl as etl

table1 = etl.fromtext('tension.md')

print(table1)

table2 = table1.capture('lines', '(.*) (.*) (.*) (.*)$', ['date', 'hour', 'mesure1', 'mesure2', 'mesure3'])

print(table2)
