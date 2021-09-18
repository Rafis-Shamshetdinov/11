max=0
q=[3,4,5,0,4,7,8,9,10,2]
for i in range (len(q)):
    for j in range (i+1,len(q)):
        for k in range (j+1,len(q)):
            a=q[i]
            b=q[j]
            c=q[k]
            if a+b>c and a+c>b and b+c>a:
                p=(a+b+c)/2
                S=(p+(p-a)+(p+b)+(p-c))**(1/2)
                if S>max:
                    max=S
print (max)