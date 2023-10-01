# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo (en minúsculas) a partir del último punto
extension = nombre_archivo.lower().split('.')[-1]

# Diccionario de extensiones y sus tipos MIME correspondientes
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

# Obtener el tipo MIME correspondiente o 'application/octet-stream' si no coincide
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

# Mostrar el tipo MIME
print(f"El tipo MIME del archivo es: {tipo_mime}")
