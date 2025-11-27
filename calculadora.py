import math

print("=== Calculadora Científica en Python ===")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Raíz cuadrada")
print("7. Seno (en grados)")
print("8. Coseno (en grados)")
print("9. Tangente (en grados)")
print("10. Logaritmo natural (ln)")
print("11. Logaritmo base 10")

opcion = int(input("Elige una opción: "))

# Para operaciones que necesitan dos números
if opcion in [1, 2, 3, 4, 5]:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

# Para operaciones de un solo número
elif opcion in [6, 7, 8, 9, 10, 11]:
    num1 = float(input("Ingresa el número: "))

# Operaciones básicas
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

# Operaciones científicas
elif opcion == 5:
    print("La potencia es:", num1 ** num2)

elif opcion == 6:
    if num1 >= 0:
        print("La raíz cuadrada es:", math.sqrt(num1))
    else:
        print("Error: no existe raíz de un número negativo.")

elif opcion == 7:
    print("Seno:", math.sin(math.radians(num1)))

elif opcion == 8:
    print("Coseno:", math.cos(math.radians(num1)))

elif opcion == 9:
    print("Tangente:", math.tan(math.radians(num1)))

elif opcion == 10:
    if num1 > 0:
        print("Logaritmo natural:", math.log(num1))
    else:
        print("Error: el logaritmo solo existe para números positivos.")

elif opcion == 11:
    if num1 > 0:
        print("Logaritmo base 10:", math.log10(num1))
    else:
        print("Error: el logaritmo solo existe para números positivos.")

else:
    print("Opción inválida.")
