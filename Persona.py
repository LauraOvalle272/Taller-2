class Persona:
    # Atributos
    tipoDocumento = ""
    documento = ""
    nombre = ""
    apellido = ""
    peso = 0,0
    estatura = 0
    edad = 0
    sexo = ""
    # Métodos
    def __init__(self, tipoDocumento, documento, nombre, apellido, peso, estatura, edad, sexo):
        self.tipoDocumento = tipoDocumento
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.estatura = estatura
        self.edad = edad
        self.sexo = sexo
    def solicitarDatos(self):
        self.tipoDocumento = input("Ingrese tipo documento ")
        self.documento = input("Ingrese documento ")
        self.nombre = input("Ingrese su nombre ")
        self.apellido = input("Ingrese su apellido ")
        self.peso = int(input("Ingrese su peso "))
        self.estatura = int(input("Ingrese su estatura "))
        self.edad = int(input("Ingrese su edad "))
        self.sexo =input("Ingrese su sexo ")
    def mostrarPersona(self):
        print(f"El nombre de la persona es {self.nombre} {self.apellido}")
        print(f"su tipo de documento es {self.tipoDocumento} y su numero de documento es {self.documento}")
        print(f"{self.nombre} pesa {self.peso} y mide {self.estatura}")
        print(f"tiene {self.edad} y es {self.sexo}")
    def calcularMc(self):
        imc = self.peso/(self.estatura * self.estatura)
        return imc
    def mayorEdad(self):
        if self.edad >= 18:
            condicion = "Es mayor de edad"
            return condicion
        else:
            condicion = "Es menor de edad"
            return condicion


        
