with open('C:/Users/acer/Desktop/rollnums.txt','r') as f:
    data = f.read()

data = data.split('\n')
excep = ['406','407','416','430','451','453','456']#               type in str
a = 0
data2 = []
data1 = []
reference = []
dup =[]

start_reg = 401     #regular start
end_reg = 500       #regular end
start_LE = 401      #LE start
end_LE = 413        #LE end
e = 7       #regular abc end

#strip and convert the last 3 digits into int and print duplicates

print('duplicates are = ')

for i in range(len(data)):
    c = data.count(data[i])
    data[i] = data[i].strip()
     #----------------------------------                                 LE members
    if data[i][0:2] == '20':                                               
        data2.append(int(data[i][-3:]))
        continue
    #-----------------------------------                                 regular members
    data1.append(hex(int(data[i][-3:],16))[-3:])
    if c != 1:
        a = 1
        dup.append(data[i])
else:
    if a !=1:
        print('\t\tnone')

for i in set(dup):
    print(i)

#reference list to cross check the missing nums                         (401 - 464)
    
for i in range(start_reg,end_reg):
    reference.append(str(i))

#reference list to cross check the missing nums                         (a,b,c - (0--9))

    

for i in ['a','b','c']:
    for j in range(0,10):
        if (i == 'c') and (j >e):
            break
        reference.append(str(hex(int('4{0}{1}'.format(i,j),16))[-3:]))


print('missing numbers are = ')

#print the missing nums from 401 to 465 except in (excep list)

for i in reference:
    if i in excep:
        continue
    if i not in data1:
        a = 2
        print(i,end=',')
else:
    if a != 2:
        print('\t\tnone')

print('\nIn LE =')


#print the missing nums from LE 401 to 406


for i in range(start_LE,end_LE):
    if i not in data2:
        a = 3
        print(i,end=',')
else:
    if a!=3:
        print('\t\tnone')
