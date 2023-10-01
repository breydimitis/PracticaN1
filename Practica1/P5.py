# Solicitar al usuario la cantidad de shows musicales vistos en el último año
shows_vistos = int(input("¿Cuántos shows musicales ha visto en el último año? "))

# Comprobar si ha visto más de 3 shows
ha_visto_mas_de_3 = shows_vistos > 3

# Mostrar el resultado en pantalla
print(f"¿Ha visto más de 3 shows musicales? {ha_visto_mas_de_3}")
