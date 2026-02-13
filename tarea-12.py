#pregunta cuasntosd alumnos quieres capturar
#y que haga esto mismo



alumno= {
    "name": "",
    "edad": 0,
    "carrera": "",
}
ico201=[]
num=int(input("Cuantos alumnos van a ser?"))

for i in range(num):
    name=input("Name del alumno: ")
    Edad=int(input("Edad del alumno: "))
    carrera = input("Ingrese la carrera del alumno: ")

    alumno["name"]=name
    alumno["edad"]=Edad
    alumno["carrera"]=carrera
    
    ico201.append(alumno.copy())
    
print("Lista de alumnos: ")
for alumno in ico201:
    print(alumno)
