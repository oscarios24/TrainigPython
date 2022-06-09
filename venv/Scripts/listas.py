print('hello word')
lista1=["uno","dos"]
listacompras=["manza", 2.4,"peras", 3.7, "platanos", 5.3]
type(listacompras)
type(lista1)
print(lista1,listacompras)
print(f"""La {listacompras[0]} cuesta  : {listacompras[1]}
Las {listacompras[2]} cuestan: {listacompras[3]}""")

"""La mutabilidad en las listas, puede hacer posible cambiar su contenido"""
listacompras[1]= 3
print(f"""{listacompras}
La {listacompras[0]} ahora cuesta  : {listacompras[1]}
""")

"""Metodos que en las listas
    where range(inicia,termimna,la secuencia)"""
#range
listarange = range(0,20,3) # Define the limit of the rante, starts with 0 and complete on 20, but the 3 on 3
values_listarange = list(listarange) #Create the list and assign the value to the variable
print(f"""List defined; {listarange},
Values of the range: {values_listarange}
""")

#Add values with the append function
values_listarange.append(21) #The append function will send the value to the end.
print(f"""List defined; {listarange},
Values of the range: {values_listarange}
""")
#Concaten two listas
#values_listarange [0:3] it means that we will take only the first 3 values of the list.
newlista = values_listarange [0:3] + [1,3,4,5,6,'gato','tonchi','brinca']
print(f"""Concated values: {newlista}""")

#To know the lengt of the list we use the len method.
print(f"""The lengt of the new list is = {len(newlista)}""")
#To know if a value exists in a list we use the method in
print(f"""The value gatto exits on the newlista = {"gato" in newlista}""")

# We can modify the values of the list using slaicing
newlista[0:4] = ["pez","piojo","lagartijo","alacran"] #The first 4 values will be replaced by
print(f"""New list updaed= {newlista}""")

newlista[10:0] = ["candi"] #The first 4 values will be replaced by
print(f"""New list updaed= {newlista}""")

#Listas anidadas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
matix = [lista1,lista2,lista3]
print(f"""{matix}""")
print(f"""Print the first matrix: {matix[0]}""")
print(f"""Print the second value of the second matrix: {matix[1][1]}""")
#Applaying slaicing
print(f"""Print the first and the second value of the second matrix: {matix[1][0:2]}""")
print(f"""Print the first and the second value of the second matrix: {matix[2][0:2]}""")
