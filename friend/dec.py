import sys
import string

fo=open(sys.argv[1],"r")
fw=open(sys.argv[2],"w")
uc=[]
ml=[]
fs=[]
sa=[]
ca=[]
sar=[]
car=[]
dm=""
lt=""

for line in fo:
    for m in line:
        ml.append(m)

for a in string.ascii_lowercase:
    sa.append(a)

c=1    
for l in sa[::-1]:
    if (c>13):
        c=1
    fv=sa.index(l)
    fv=int(fv)-c
    sar.append(sa[fv])
    c+=1

for b in string.ascii_uppercase:
    ca.append(b)

c=1
for l in ca[::-1]:
    if (c>13):
        c=1
    fv=ca.index(l)
    fv=int(fv)-c
    car.append(ca[fv])
    c+=1

for k in string.ascii_uppercase:
    uc.append(k)

for j in string.ascii_lowercase:
    uc.append(j)

for l in ml:
    if (l==" "):
        fs.append(l)
        continue
    lt=lt+l
    if (len(lt)==2):
        count=0
        for i in range (11,81):
            if(i%10==0):
                pass
            elif (int(lt)==i):
                fs.append(uc[count])
                count+=1
            else:
                count+=1
        lt=""
    else:
        pass

for l in fs:
    if (l==" "):
        dm=dm+l
    elif (l.islower()):
        c=1
        for j in sar:
            if (c>13):
                c=1
            if (l==j):
                fv=sa.index(l)
                fv=int(fv)+c
                if (fv>25):
                    fv=fv-26
                dm=dm+str(sa[fv])
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
                fv=int(fv)+c
                if (fv>25):
                    fv=fv-26
                dm=dm+str(ca[fv])
                c+=1
            else:
                c+=1

fw.write(dm)
