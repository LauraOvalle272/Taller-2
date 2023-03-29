notas=[]
print("¿Cuantos notas ingresará?")
h = int(input())
cont=0 
while cont < h:
    print("ingrese la nota ",cont+1)
    val=float(input())
    notas.append(val)
    cont+=1
promedio=sum(notas)/len(notas)  
p = print("Su promedio es", promedio)
if promedio < 3.0: 
    print("Reprobaste")
elif promedio > 4.0:
    print("Pasaste con buenos resultados")
else: 
    print("pasate raspando")
