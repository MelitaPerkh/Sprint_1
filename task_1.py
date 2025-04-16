sumResult = 0
s = '1h 45m,360s,25m,30m 120s,2h 60s'
timeS =s.replace(',',' ') 
timeVal = timeS.split(' ')
for val in timeVal:
    if 'h' in val:
        sumResult += int(val[0:len(val)-1])*60 
    elif 'm' in val:
        sumResult += int(val[0:len(val)-1])
    elif 's' in val:
        sumResult += int(val[0:len(val)-1])/60 
print(sumResult)   