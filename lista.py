#1
list_vacia = [] 
print("lista vacia:")
print(len(list_vacia))
#2
Lista_Estudiantes = ["Ric","Fel","jhor","Jai","Rub","gis","albert"]
#3
print("lista de estudiantes: ")
print(len(Lista_Estudiantes))
#4
print("lista de estudiantes En varios puntos: ")
print(f'{Lista_Estudiantes[0]},\n{Lista_Estudiantes[3]}, \n{Lista_Estudiantes[6]}' )
#5
tipos_datos_mezclados=["Rich",26,1.90,"Casado","Barcelona de indias, calle 78 Carrera 11"]
#6
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#7
it_companies.insert(4,"Tecnar")
#8
elemento = "Tecnar" 
if elemento in it_companies: 
    print("El elemento",elemento,"si existe en la lista.") 
else: 
    print("El elemento",elemento," no existe en la lista.")
#9
it_companies.sort()
print("lista Ordenada Ascendente: ")
print(it_companies)
#10
print("lista Ordenada Descendente: ")
it_companies.sort(reverse=True) 
print(it_companies)
#11
del it_companies[0]
print("Eliminar primer elemento: ")
print (it_companies)
#12
it_companies.clear()
print("Lista Vacia: ")
print(it_companies)