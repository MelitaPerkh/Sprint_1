s = 123456 #example 
def digit_root(num):
    sum=0 
    strS = str(num)
    for i in reversed(range(0,len(strS))):
        sum += int(strS[i])       
    return(sum)

while len(str(s))>1:
    s = digit_root(s)
else:
    result = s
print(result)