"""
The set, or cunjuntos
all them are unic.
those are not ordered.
"""
#
conjunto_vacio = set()
conjunto1 = {1,2,3,4}
print(f"""Este es el conjunto vacio{conjunto_vacio}
Este es el conjunto 1: {conjunto1}
El tipo de dato es:{type(conjunto1)}""")

#To add an element to the conjunto is with .add method.
conjunto1.add(6)
conjunto1.add(8)
conjunto1.add(7)
print(f"""New elements of the Conjunto: {conjunto1}""") #all the elements will be ordered.

#para verificar pertenencia
print(f"""7 esta dentro del conjunto1: {7 in conjunto1}""") #all the elements will be ordered.

#Un conjunto elimina automaticamente los elementos duplicados
conjunto2 ={'gato','tonchi','gato','luna'}
print(f"""Los valores del conjunto2 son: {conjunto2}""")

#Ayuda a quitar elementos duplicados de una lista
lista_duplicados_no_ordenados = [1,1,2,2,3,3,4,5,6,8,7]
print(f"""Lista deshordenada:{lista_duplicados_no_ordenados}""")
#Convert the lista to conjunto para quitar duplicados y ordenar valores
conjunto3 = set(lista_duplicados_no_ordenados)
print(f"""Conjunto ya ordenaldo;{conjunto3}""")
#Convertir el conjunto a lista para tener el mismo formato de datos del inicio
lista_ordenada = list(conjunto3)
print(f"""Lista ya ordenada y chida:{lista_ordenada}""")

#all in one line.
lista_duplicados_no_ordenados_letras = ['a','a','a','c','b','d']
lista_ordered = list(set(lista_duplicados_no_ordenados_letras))
print(f"""Lista de letras ordenada; {lista_ordered}""")
lista_duplicados_no_ordenados = [1,1,2,2,3,3,4,5,6,8,7]
lista_ordenada_num = list(set(lista_duplicados_no_ordenados))
print(f"""Lista de numeros ordenada; {lista_ordenada_num}""")

"""We are going to test now Diccionarios. """

employees = {'id1':'Juan', 'id2': 'Pedro', 'id3':'Andres' }
print(f"""Para imprimir todo: {employees}""")
print(f"""Para imprimir un un elemento del diccionario ocupas solo el id: {employees['id1']}""")
#To add a new element of the diccionario is:
employees['id4'] = 'Oscar'
print(f"""Ver que se agrego correctamente al final de la lista: {employees}""")
employees['id0'] = 'Juana'
print(f"""Ver que se agrego correctamente al final de la lista: {employees}""")

#Para modificar su valor es asi haces referencia al id y le pones su nuevo valor.
employees['id0'] = 'Pepe'
print(f"""Ver que se agrego correctamente al final de la lista: {employees}""")

#Tambien se pueden hacer opraciones
employees_salari = {'id1': 20, 'id2': 30, 'id3':80 }
print(f"""Ver que se agrego correctamente al final de la lista: {employees_salari}""")
employees_salari['id2'] += 20
print(f"""ver el campo con un nuevo valor {employees_salari['id2']}""")

#Sumar salarios

print(f"""Sumando dos salarios: {employees_salari['id1'] + employees_salari['id3']}""")

#Adding a bucle o un for
for i in employees_salari:
    print(f"""Las edades son: {employees_salari[i]}""")

# imprimir todo
for i,v in employees_salari.items():
    print(f"""imprimiendo id y valores: {i,v}""")
