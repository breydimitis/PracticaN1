# Solicitar al usuario una hora en formato HH:mm
hora_usuario = input("Ingrese una hora en formato HH:mm: ")

# Dividir la hora en horas y minutos y convertirla a float
try:
    horas, minutos = map(float, hora_usuario.split(':'))
except ValueError:
    print("Formato de hora incorrecto. Por favor, ingrese una hora válida en formato HH:mm.")
    exit()

# Comprobar si es hora de desayuno, almuerzo o cena
if 7.0 <= horas < 8.0:
    print("Es hora de desayunar.")
elif 12.0 <= horas < 13.0:
    print("Es hora de almorzar.")
elif 18.0 <= horas < 19.0:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")
