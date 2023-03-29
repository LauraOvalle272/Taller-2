from Persona import Persona 

print("--------------------- Primera persona ---------------------")
laura = Persona("", "", "", "", 0, 0, 0, "")
laura.solicitarDatos()
laura.mostrarPersona()
imc = laura.calcularMc()
if imc<20:
    print(f"su imc es {imc}, su peso está por debajo de lo ideal")
elif 20<=imc<=25:
    print(f"su imc es {imc}, su peso es ideal")
else:
    print(f"su imc es {imc}, estas en sobrepeso")
print(laura.mayorEdad())

print("--------------------- Segunda persona ---------------------")
manuel = Persona("", "", "", "", 0, 0, 0, "")
manuel.solicitarDatos()
manuel.mostrarPersona()
imc = manuel.calcularMc()
if imc<20:
    print(f"su imc es {imc}, su peso está por debajo de lo ideal")
elif 20<=imc<=25:
    print(f"su imc es {imc}, su peso es ideal")
else:
    print(f"su imc es {imc}, estas en sobrepeso")
print(manuel.mayorEdad())
