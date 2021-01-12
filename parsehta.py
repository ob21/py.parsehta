#import petl as etl
import datetime
import statistics
#import pandas
#import plotly.express as px
import matplotlib.pyplot as plt

#table1 = etl.fromtext('tension.md')
#print("\n> print table1")
#print(table1)

#print("\n> print file lines not empty")
#for line in open("tension.md"):
#    if line.strip() :
#        print("line>" + line.strip())

def cm_to_inch(value):
    return value/2.54 

print("\n> print filtered array from a file")
with open("tension.md") as file:
    lines = file.readlines()
iterator = filter(lambda line: line.strip(), lines)
entries = [entry.split() for entry in list(iterator)]
print(entries)

dates = []
diastolic = []
systolic = []

for item in entries:
    if len(item)==5:
    	date_time_obj = datetime.datetime.strptime(item[0]+","+item[1], '%d/%m/%y,%Hh%M')
    	print("date : "+str(date_time_obj))
    	dates.append(date_time_obj)
    	syst = statistics.mean([int(item[2].split('/')[0]),int(item[3].split('/')[0]),int(item[4].split('/')[0])])
    	print("- syst : "+str(round(syst)))
    	systolic.append(round(syst))
    	dias = statistics.mean([int(item[2].split('/')[1]),int(item[3].split('/')[1]),int(item[4].split('/')[1])])
    	print("- dias : "+str(round(dias)))
    	diastolic.append(round(dias))

plt.figure(figsize=(cm_to_inch(30), cm_to_inch(10)))
plt.plot(dates, systolic, color='red', label='syst', marker="o")
plt.plot(dates, diastolic, color='blue', label='dias', marker='o')
plt.legend()
#plt.axis([dates[0], dates[len(dates)-1], 50, 180])
plt.grid(True)
plt.savefig('tension.png')
#plt.show()

