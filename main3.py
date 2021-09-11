nbre= int(input("entre un nombre: "))
nbre1=1
for i in range(nbre+1):
    nbre1=i*i
    i+=1
    dict={(i-1):nbre1}
    print(dict)
