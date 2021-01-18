#setup
import numpy as np
#probably can be done without numpy but i can´t be bothered, also I think using it in this manner sucks for perfomance lmao
print("This program converts any base 10 number to base n")
num=float(input("Number in base 10: "))
base=int(input("Base: "))
m=int(input("LaTeX Tables: (1) Yes, (2) No "))
entres=np.array([0])
fracres=np.array([0])
fracreg=np.array([0])
d=1
o=1
i=1 #d, o and i are indicators to stop the algorithm
j=0
b=""
k=0
h="."
a=0
backslash="\\"
dback=backslash+backslash


if m==1:
    ent=int(num)
    frac=round(num-ent, 10)
    #using round due to floating point weirdness lol
    print("\\begin{table}[]")
    print("\centering")
    print("\\begin{tabular}{|c|c|c|}")
    print("\hline")
    print("\multicolumn{3}{c}{Whole part}", dback)
    print("\hline")
    print("Number&","$\div",base,"$&Residue", dback)
    print("\hline")
    while d > 0 :
            e=ent%base #the residue/modulo
            d=int(ent/base)
            print(ent,"&",d,"&",e,dback)
            ent=d
            entres=np.append(entres,[e])
    entres=np.delete(entres,0)
    n=entres.size
    entres=entres[::-1]
    print("\hline")
    print("\end{tabular}")
    print("\quad")
    print("\\begin{tabular}{|c|c|c|c|}")
    print("\hline")
    while j<n :
        strj=str(entres.item(j))
        b=b+strj
        j=j+1
    print("\multicolumn{4}{c}{Fractionary part}", dback)
    print("\hline")
    print("Number&","x$",base,"$&Integer&Fraction", dback)
    print("\hline")
    while i>0 :
        fracreg=np.append(fracreg, [frac])
        f=round(frac*base, 10)
        l=int(f)
        m=round(f-l,10)
        print(frac,"&",f,"&",l,"&",m,dback)
        frac=m
        fracres=np.append(fracres, [l])       
        for c in fracreg :
            if frac==c :
                i=-1 #to check for repeated fractions, also, created fracreg as [0], so no need to check if the fraction ends, thankfully
                check=c
                if c != 0 :
                    o=np.where(fracreg==c)
                    oarray=o[0]
                    a=oarray.item(0)
    fracres=np.delete(fracres,0)
    p=fracres.size
    while k<p :
        strk=str(fracres.item(k))
        h=h+strk
        k=k+1
    res=b+h
    print("\hline")
    print("\end{tabular}")
    print("\caption{The result is: $(",res,")_{",base,"}$}")
    print("\label{Base 10 to ",base,"}")
    print("\end{table}")
    print("%Remember to specify the float option at the begining of the table!")
    if check != 0 :
        print("%The fraction repeats when Number =",c,"Position:",a,", remember to add \overline{the rest of the number} to denote it in your paper! (and maybe a couple of \\textbf to where that number is on the table if you wanna be fancy lol)")
    
if m==2:
    ent=int(num)
    frac=round(num-ent, 10)
    #using round due to floating point weirdness lol
    print("Whole part")
    print("Number       ","/",base,"       Residue")
    while d > 0 :
            e=ent%base #the residue/modulo
            d=int(ent/base)
            print(ent,"        ",d,"         ",e)
            ent=d
            entres=np.append(entres,[e])
    entres=np.delete(entres,0)
    n=entres.size
    entres=entres[::-1]
    while j<n :
        strj=str(entres.item(j))
        b=b+strj
        j=j+1
    print("Fractionary part")
    print("Number       ","x",base,"        Integer        Fraction")
    while i>0 :
        fracreg=np.append(fracreg, [frac])
        f=round(frac*base, 10)
        l=int(f)
        m=round(f-l,10)
        print(frac,"        ",f,"       ",l,"        ",m)
        frac=m
        fracres=np.append(fracres, [l])       
        for c in fracreg :
            if frac==c :
                i=-1 #to check for repeated fractions, also, created fracreg as [0], so no need to check if the fraction ends, thankfully
                if c != 0 :
                    o=np.where(fracreg==c)
                    oarray=o[0]
                    a=oarray.item(0)
                    print("The fraction repeats when Number =",c,"Position:",a)
    fracres=np.delete(fracres,0)
    p=fracres.size
    while k<p :
        strk=str(fracres.item(k))
        h=h+strk
        k=k+1
    res=b+h
    print("The result is:", res)