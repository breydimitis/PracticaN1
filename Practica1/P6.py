# Solicitar al usuario la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif 4 <= edad <= 18:
    precio_entrada = 5  # Entre 4 y 18 años, el precio es $5
else:
    precio_entrada = 10  # Mayores de 18 años, el precio es $10

# Mostrar el precio de la entrada al cliente
print(f"El precio de la entrada es de ${precio_entrada}.")
