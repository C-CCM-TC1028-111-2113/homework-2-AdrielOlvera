
def main():
    #Escribe tu código debajo de esta línea
    age=int(input("Ingresa tu edad: "))
io=str(input("¿Tienes identificación oficial? (s/n)"))
if age>=18:
    x=True
elif 18>age>=0:
    x=False
elif age<0:
    print("Respuesta incorrecta")
    x=False
if io=="s":
    y=True
elif io=="n":
    y=False
else:
    print("Respuesta incorrecta")
    y=False
if x and y:
    print("Trámite de licencia concedido")
else:
    print("No cumples requisitos")



    pass


if __name__ == '__main__':
    main()
