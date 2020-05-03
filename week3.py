s=input('Please type a string: ')

if len(s)==1:
    print('Μήκος=1')
else:
    s1=[]
    for i in s:
        if i==' ':
            continue
        s1.append(i)
    if s1==s1[::-1]:
        adict={s:len(s)}
        alist=[i for i in s]
        print(adict)
        print(alist)
    else:
        print('Δεν είναι παλίνδρομο')
    
    

