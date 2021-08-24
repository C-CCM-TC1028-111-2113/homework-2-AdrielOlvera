def main():
    # Escribe el código adecuado para completar el programa
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
if num1>num2<num3:
    print(num2)
    num2=num1+num3
elif num2>num1<num3:
    print(num1)
    num1=num2+num3
elif num2>num3<num1:
    print(num3)
    num3=num1+num2
if num1>num2<num3:
    print(num2)
    num2=num1+num3
elif num2>num1<num3:
    print(num1)
    num1=num2+num3
elif num2>num3<num1:
    print(num3)
    num3=num1+num2
if num1>num2<num3:
    print(num2)
    num2=num1+num3
elif num2>num1<num3:
    print(num1)
    num1=num2+num3
elif num2>num3<num1:
    print(num3)
    num3=num1+num2

    pass


if __name__=='__main__':
    main()
