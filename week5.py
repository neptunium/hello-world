import statistics as st
with open('inputdata.txt') as f1:
    data=f1.read().splitlines()

numdata=[]
for i in data:
    numdata.append(float(i))

mo=round(st.mean(numdata),3)
std=round(st.stdev(numdata),3)

with open('outputdata.txt','w',encoding='utf8') as f2:
    line='Μέσος όρος = '+str(mo)+'\n'+'Τυπική απόκλιση = '+str(std)
    f2.write(line)
                                                                        

