lista_brojeva = []
for x in range(0, 10):
    lista_brojeva.append(int(input("Unesi broj: ")))
pomocnaLista = []
for item in lista_brojeva:
    if item % 2 != 0:
        pomocnaLista.append(item)
for item in pomocnaLista:
    print(item)
