informacion_personal = {
    "nombre": "María López",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Diseñadora gráfica"
}

# Acceder y modificar "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar/actualizar "profesion" (si existe se actualiza, si no se crea)
informacion_personal["profesion"] = "Ingeniera de software"

# Verificar existencia de "telefono" y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593987654321"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
