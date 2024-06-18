import statistics
def leerArchivos():
    with open("datos.txt","r") as archivo:
        for linea in archivo:
            lineas.append(linea.strip())
lineas = []
leerArchivos()
numeros = [int(i) for i in lineas]
promedio = sum(numeros)/len(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)
print(mediana)
print(moda)