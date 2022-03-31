import sys
import string

fo=open(sys.argv[1],"r")
fw=open(sys.argv[2],"w")
uc=[]
ml=[]
sa=[]
ca=[]
fs=[]
em=""

for line in fo:
    for m in line:
        ml.append(m)

    
for i in range (11,81):
    if (i%10==0):
        pass
    else:
        uc.append(i)

for a in string.ascii_lowercase:
    sa.append(a)
sar=sa[::-1]

for b in string.ascii_uppercase:
    ca.append(b)
car=ca[::-1]

for l in ml:
    if (l==" "):
        fs.append(l)
    elif (l.islower()):
        c=1
        for j in sar:
            if (c>13):
                c=1
            if (l==j):
                fv=sa.index(l)
                fv=int(fv)-c
                fs.append(sa[fv])
                c+=1
            else:
                c+=1
    else:
        c=1
        for k in car:
            if (c>13):
                c=1
            if (l==k):
                fv=ca.index(l)
                fv=int(fv)-c
                fs.append(ca[fv])
                c+=1
            else:
                c+=1

for l in fs:
    if (l==" "):
        em=em+l
    elif (l.islower()):
        count=26
        for j in string.ascii_lowercase:
            if (l==j):
                em=em+str(uc[count])
                count+=1
            else:
                count+=1
    else:
        count=0
        for k in string.ascii_uppercase:
            if (l==k):
                em=em+str(uc[count])
                count+=1
            else:
                count+=1


fw.write(em)

