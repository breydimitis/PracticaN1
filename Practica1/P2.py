# Solicitar el costo de la comida al usuario
costo_comida = float(input("Ingrese el costo de la comida: $"))

# Solicitar el porcentaje de propina al usuario
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15): "))

# Calcular la cantidad de dinero a dejar como propina
propina = (costo_comida * porcentaje_propina) / 100

# Mostrar la cantidad de dinero a dejar como propina
print(f"Debe dejar ${propina:.2f} como propina.")
