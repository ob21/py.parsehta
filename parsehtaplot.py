import datetime
import statistics
import matplotlib.pyplot as plt

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
        #TODO => check item[0] and item[1] format
    	date_time_obj = datetime.datetime.strptime(item[0]+","+item[1], '%d/%m/%y,%Hh%M')
    	print("date : "+str(date_time_obj))
    	dates.append(date_time_obj)
        #TODO => check item[2,3,4] presence and format
    	sys_mean = statistics.mean([int(item[2].split('/')[0]),int(item[3].split('/')[0]),int(item[4].split('/')[0])])
    	print("- sys : "+str(round(sys_mean)))
    	systolic.append(round(sys_mean))
    	dia_mean = statistics.mean([int(item[2].split('/')[1]),int(item[3].split('/')[1]),int(item[4].split('/')[1])])
    	print("- dia : "+str(round(dia_mean)))
    	diastolic.append(round(dia_mean))

#plt.figure(figsize=(cm_to_inch(30), cm_to_inch(10)))
#plt.plot(dates, systolic, color='red', label='syst', marker="o")
#plt.plot(dates, diastolic, color='blue', label='dias', marker='o')
#plt.legend()
#plt.grid(True)
#plt.savefig('tension.png')
#plt.show()

