import datetime
import statistics

with open("tension.md") as file:
    lines = file.readlines()
iterator = filter(lambda line: line.strip(), lines)
entries = [entry.split() for entry in list(iterator)]
print(entries)

dates = []
diastolic = []
systolic = []

for item in entries:
    if len(item)>2:
       	if '/' not in item[0]:
            print("'/' not in date")
            break
        if 'h' not in item[1]:
            print("'h' not in hour")
            break
        if '/' not in item[2]:
            print("'/' not in item[2]")
            break
        date_time_obj = datetime.datetime.strptime(item[0]+","+item[1], '%d/%m/%y,%Hh%M')
        print("date : "+str(date_time_obj))
        dates.append(date_time_obj)
        #TODO => check item[2,3,4] presence and format
        sys_array = []
        dia_array = []
        for i in range(2,(len(item)-1)):
            sys_array.append(int(item[i].split('/')[0]))
            dia_array.append(int(item[i].split('/')[1]))
        print("number of measures : "+str(len(sys_array)))
        sys_mean = statistics.mean(sys_array)
        print("- sys : "+str(round(sys_mean)))
        systolic.append(round(sys_mean))
        dia_mean = statistics.mean(dia_array)
        print("- dia : "+str(round(dia_mean)))
        diastolic.append(round(dia_mean))
