import datetime
import statistics

with open("tension.md") as file:
    lines = file.readlines()
iterator = filter(lambda line: line.strip(), lines)
entries = [entry.split() for entry in list(iterator)]
#print(entries)

entries = reversed(entries)

dates = []
days = []
diastolic = []
systolic = []

date_min = datetime.datetime.strptime("01/01/18 00h00", '%d/%m/%y %Hh%M')
date_max = datetime.datetime.strptime("30/12/22 00h00", '%d/%m/%y %Hh%M')

#date_min = datetime.datetime.strptime("01/08/20 00h00", '%d/%m/%y %Hh%M')
#date_max = datetime.datetime.strptime("06/11/20 00h00", '%d/%m/%y %Hh%M')

#date_min = datetime.datetime.strptime("25/12/20 00h00", '%d/%m/%y %Hh%M')
#date_max = datetime.datetime.strptime("29/12/20 00h00", '%d/%m/%y %Hh%M')

#date_min = datetime.datetime.strptime("28/12/20 00h00", '%d/%m/%y %Hh%M')
#date_max = datetime.datetime.strptime("18/01/21 00h00", '%d/%m/%y %Hh%M')

print("|          Date           |    Diastolique    |    Systolique    | Tendancy |    Commentaire   |")
print("|    -----------------    |    -----------    |    ----------    | -------- |    -----------   |")
for item in entries:
    #print(item)
    if len(item)>2:
       	if '/' not in item[0]:
            #print("'/' not in date (day bad format)")
            break
        if 'h' not in item[1]:
            #print("'h' not in hour (hour bad format), try matin/soir")
            if 'matin' == item[1]:
                item[1] = "8h00"
            if 'soir' == item[1]:
                item[1] = "23h00"
            if 'h' not in item[1]:
                #print("'h' not in hour definitely")
                break
        if '/' not in item[2]:
            #print("'/' not in "+item[2]+" (pressure bad format)")
            break
        date_time = datetime.datetime.strptime(item[0]+","+item[1], '%d/%m/%y,%Hh%M')
        if date_time < date_min or date_time > date_max:
            #print("exclude "+str(date_time))
            continue		
        date_hour = datetime.datetime.strptime(item[1], '%Hh%M')
        date_noon = datetime.datetime.strptime("12h00", '%Hh%M')
        bold="  "
        if date_hour<date_noon :
            bold="**"
        #print("date : "+str(date_time))
        dates.append(item[0])
        if item[0] not in days:
            days.append(item[0])
        #TODO => check item[2,3,4] presence and format
        sys_array = []
        dia_array = []
        comment=""
        for i in range(2,len(item)):
            if '/' not in item[i]:
                #print("'/' not in "+item[i]+" (pressure bad format)")
                comment=str(item[i])
                break
            if '(' in item[i]:
                item[i] = item[i].split('(')[0] #exclude bpm
            sys_array.append(int(item[i].split('/')[0]))
            dia_array.append(int(item[i].split('/')[1]))
        #print("number of measures : "+str(len(sys_array))+" "+str(sys_array))
        sys_mean = statistics.mean(sys_array)
        #print("- sys : "+str(round(sys_mean)))
        systolic.append(round(sys_mean))
        dia_mean = statistics.mean(dia_array)
        #print("- dia : "+str(round(dia_mean)))
        diastolic.append(round(dia_mean))
        if sys_mean>140 or dia_mean>90:
            tendancy="+"
        else:
            tendancy="-"
        print("| "+bold+str(date_time)+bold + " |        " + str(round(sys_mean)) + "        |        "  + 
str(round(dia_mean)).ljust(3,' ') 
+ 
"       |    "+tendancy+"     |    " + 
comment)
print("")
print("Total of measures : " + str(len(systolic)))
print("")
print("Number of days of measures : " + str(len(days)))
print("")
print("Measures from "+str(dates[0])+" to "+str(dates[len(dates)-1]))
print("")
print("Max sys : " + str(max(systolic)))
print("Min sys : " + str(min(systolic)))
print("")
print("Max dia : " + str(max(diastolic)))
print("Min dia : " + str(min(diastolic)))
print("")
print("Moy sys : " + str(round(statistics.mean(systolic))))
print("Moy dia : " + str(round(statistics.mean(diastolic))))
