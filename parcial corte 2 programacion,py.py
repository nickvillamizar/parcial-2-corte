#Escribir el código para Invertir un array de string, por ejemplo si la entrada es
#["1","4","3","2"] la salida debe ser ["2","3","4","1"]. El código debe cumplir con los
#siguientes parámetros:
    # •Se debe solicitar la cantidad de elementos del array.
    # •Se debe solicitar por pantalla el valor de cada uno de los elementos
     #•Se debe crear una funcion que reciba el arrayyretorne el array invertido.
     #•Se debe mostrar en pantalla el array originalyel invertidoarray
awarded = []
for i in range(int(input("cuantos numeros desea meter a la lista?"))):
    awarded.append(int(input("Introduce un número : ")))
awarded.sort()
print("Los números ingresados " + str(awarded))
idx = len(awarded) - 1
newList = []
while (idx >= 0):
  newList.append(awarded[idx])
  idx = idx - 1

print(newList)



