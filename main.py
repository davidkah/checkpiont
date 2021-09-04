

# for i in range(2000,3200):
#     if i%7==0 and i!= i%5:
#         print(i)
#         print()


# sets={"orange","mangue"}
    
# print(sets)
# sets.add("bienvenue")
# print(sets)



# print(sets)



# mySet = {"A", "B", "C"}
# print(mySet)
# mySet.remove("B")
# print(mySet)



# mySet = {"A", "B", "C"}
# x = mySet.pop()
# print(x)
# print(mySet)

# mySet = {"A", "B", "C"}
# mySet.clear()
# print(mySet)

# mySet = {"A", "B", "C"}
# del mySe
# print(mySet)


# for i in range(0,11,2):
#     print(i)

# i=0
# while i < 10:
   
#     print(i)
#     i +=2


# import numpy as np 

# neru_array = np.array([1,2,3])

# print(neru_array)


# programmation orienté objet

# class voiture:
#     nbe_voiture = 0 
#     def __init__(self,marque): 
#         voiture.nbe_voiture +=1 
#         self.marque=marque
        
        
# voiture_1 = voiture("renault")
# voiture_2 = voiture("pegeot")

# print(voiture_1.marque)
# print(voiture_2.marque)
# print(voiture.nbe_voiture)






# ---------------la notion des listes----------------------




# une liste est une structure de donner qui contient une serie de valeur

# animaux = ["lion","girafe","tigre","sige","sourie"]
# mixte = ["tigre",12,"girafe",58,"singe",43]

# print(",".join(animaux))
# print(mixte)

# --------------utilisation d'une liste-------------------

# l'un des gros avantage d'une liste est qu'on peut appeler les element par leur position

# ----------------exemple------------------------

# print(animaux[2])
# print(mixte[0])

#  --------------opération sur des liste------------------------

# tout comme les chaîne de caractère les liste suporte des opération

# //print(animaux + mixte)//

# -------------utilisation de la methode .append


# animaux = []
# nom = "lorraine"
# nom1= "lorraine"
# animaux.append(nom+  nom1)
# print(animaux)

# -------------------- indicatoin  négatif -------------------

# une liste peut être indexée par un nombre negatif selon le modèle

# animaux = ["lion"," girafe","tigre"]
# print(animaux[0])
# print(animaux[-1])



# ----------------les tranches ----------------------

# les permets de selectionner une partie de la liste 


# animaux = ["chat","chien","lion","tigre","girafe"]

# print(animaux[0:4] )
# print()


# animaux = ["chat","chien","lion","tigre","girafe","sourie ","singe"]
# print(animaux[0:3:2])
# print()

# x = [0,1,2,3,4,5,6,7,8,9]
# print(x)
# print(x[::1])
# print(x[::2])



# ---------------- la fonction len() -----------------------

# la fonction len() vous permet de connaitre la longueur d'un liste 
# c'est dire le nombre d'élément 

# animaux = ["chat","lion","girafe","tigre","chien"]
# print(animaux)
# print(len(animaux))


# ----------------- la fonction range()--------------------

# elle permet de généré des nombres compris entres une interval

# nombre = list(range(2000,3500,5))

# print(nombre)
# print(len(nombre))


# ------------------ liste de liste ---------------------------

# animaux_1 = ["chien","char","lion","girafe","tigre"]
# animaux_2 = ["poulet","coq","porc","singe","mouton"]
# animaux_3 = ["sourie","mouche","chaton","moustique"]

# zoo = [animaux_1,animaux_2,animaux_3]
# print(zoo)
# print(len(zoo))


# animaux_5 = [["chien",1],["char",2],["lion",3],["girafe",4],["tigre",5]]
# print( animaux_5 )


# ---------------------Minimum,maximum et somme d'une liste------------------


liste = list(range(10))

# print(liste)
# print(sum(liste))
# print(min(1, 10))
# print(max(1, 10))




# ---------------- checkpionk 2---------------------

# nombre =list(range(200,3200,5)) 


# print(nombre)
# print(len(nombre)) 


# for i in range(200,3200):
#     b= i/5
#     print(b)


# ------------------------------------------------------------------------

# ----------------------------exercice----------------------------------
# ------------------------------------------------------------------------



semaine = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jours = semaine[0:5]
week_end = semaine[-2: ]

print(f"les cinq (5) premier jours : "+ ",".join(jours) + " : de la semaine")
print()
print("les deux (2)  jours du week-end : " + ",".join(week_end))

