# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú de opciones
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

# Leer la opción del usuario
opcion = input("Ingrese el número de la operación que desea realizar (1/2/3): ")

# Realizar la operación correspondiente según la opción seleccionada
if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es igual a {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es igual a {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es igual a {resultado}")
else:
    print("Opción no válida. Por favor, seleccione una opción válida (1/2/3).")
