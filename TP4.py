
#%%
def afficher(p):
    liste=[]
    for i in range(len(p)-1,-1,-1):
        coeff=p[i]
        if i==0:
            liste.append(f"{coeff}")
        elif i==1:
            liste.append(f"{coeff}.x")
        else:
            liste.append(f"{coeff}.x^{i}")
    
    polynome=' + '.join(liste)
    print(polynome) 

#%%
def get_valeur(p,x):
    somme=0
    for i in range (len(p)-1,-1,-1):
        poly=p[i]*x**i
        somme+=poly
    return somme 

#%%
def deriver(p):
    liste=[]
    for i in range(len(p)-1,-1,-1):
        j=i-1
        coeff=p[i]
        if (j==0) or (j==-1):
            liste.append(f"{coeff*i}")
        elif j==1:
            liste.append(f"{coeff*i}.x")
        else:
            liste.append(f"{coeff*i}.x^{j}")

    polynome=' + '.join(liste)
    print(polynome)
    
#%%
p=[0,2,4,6,8,10]
afficher(p)
print(get_valeur(p,2))
deriver(p)


