# Definir la lista de muestra
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminar los elementos en las posiciones 0, 4 y 5
indices_a_eliminar = [0, 4, 5]

# Crear una nueva lista que excluya los elementos en los índices especificados
lista_resultante = [elemento for i, elemento in enumerate(lista_muestra) if i not in indices_a_eliminar]

# Mostrar la lista resultante
print(lista_resultante)
