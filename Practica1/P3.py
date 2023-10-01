# Definir el peso de un payaso en gramos
peso_payaso = 112

# Definir el peso de una muñeca en gramos
peso_muñeca = 75

# Solicitar al usuario la cantidad de payasos vendidos
cantidad_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))

# Solicitar al usuario la cantidad de muñecas vendidas
cantidad_muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total = (peso_payaso * cantidad_payasos) + (peso_muñeca * cantidad_muñecas)

# Mostrar el peso total del paquete
print(f"El peso total del paquete es de {peso_total} gramos.")
