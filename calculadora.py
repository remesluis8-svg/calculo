print("=== Calculadora Básica en Python ===")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Elige una opción: "))

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == 1:
    print("La suma es:", num1 + num2)

elif opcion == 2:
    print("La resta es:", num1 - num2)

elif opcion == 3:
    print("La multiplicación es:", num1 * num2)

elif opcion == 4:
    if num2 != 0:
        print("La división es:", num1 / num2)
    else:
        print("Error: no se puede dividir entre cero.")

else:
    print("Opción inválida.")