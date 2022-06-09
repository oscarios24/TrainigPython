"""
This training is for tuplas.
Tuplas are not mutabled.
"""
tupla1test = ('lunes','martes','miercoles')
tupla2test = (1,2,3,'jueves',tupla1test)
print(f"""Here is the first tupla{tupla1test}
Here is the second tupla: {tupla2test}""")

print(f"""Here is the first tupla{tupla1test[1]}
Here is the second tupla: {tupla2test[2]}""")

#To change the values of a tupla you need to convert it to a list.
listatest = list(tupla2test)
listatest[2] = "sabado"
print(f"""Here is the first tupla{tupla1test[1]}
Here is the second tupla updated: {listatest}""")

#To know the index of a element you need to put

print(f"""Sabado is on the index > {tupla2test.index('jueves')}""")
#To know how many times is a value on the tuple we use .count method.
print(f"""Sabado is on the index > {tupla2test.count('jueves')}""")

