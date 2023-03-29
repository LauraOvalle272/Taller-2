competidores= []
tiempos=[]
cont= "s"
while cont == "s":
    n = input("Ingrese su nombre: ")
    competidores.append(n)
    t = (input("Ingrese su tiempo: "))
    tiempos.append(t)
    cont= input("Desea almacenar otro tiempo")
print(competidores, tiempos)
h = print("Quien obtuvo el menor tiempo es el ganador")
print("El menor tiempo fue:", min(tiempos)) 