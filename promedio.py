#nombre
#materia
#calificacion


alumno= {
    "name": "",
    "Calificacion": 0,
    "materia": "",
     
}
ico201=[]
num=int(input("Cuantos alumnos van a ser?"))

for i in range(num):
    name=input("Name del alumno: ")
    Calificacion=int(input("Calificacion del alumno: "))
    materia = input("Ingrese la materia del alumno: ")
   


    alumno["name"]=name
    alumno["Calificacion"]=Calificacion
    alumno["materia"]=materia
   
    
    ico201.append(alumno.copy())
  
    
suma=0
print("Lista de alumnos: ")
for item in ico201:
    print(item)
    suma=suma+alumno["Calificacion"]
promedio= suma/num
print(promedio)
    




