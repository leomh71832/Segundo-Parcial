

alumno= {
    "name": "Ana",
    "edad": 21,
    "carrera": "Inge"
}
print(type(alumno))
print(alumno)

print("print(alumno['name']) = ",alumno["name"])
print("print(alumno.get('edad')) =",alumno.get("edad"))

alumno["promedio"] = 9.2
print(alumno)
alumno["edad"] = 22
print(alumno)

#como eliminar?
del alumno["carrera"]
print(alumno)

#recorrer diccionarios
for clave in alumno:
    print(clave)
    print(clave, ":", alumno[clave])
    

#funciones utiles
print("Cantidad de pares clave-valor: ",len(alumno))
print("Claves del diccionario: ",alumno.keys())
print("Valores del diccionario: ",alumno.values())
print("Pares clave-valor: ",alumno.items())






alumno1= {
    "name": "",
    "edad": 0,
    "carrera": ""
}

ico201= [alumno1,alumno1,alumno1]
print()



