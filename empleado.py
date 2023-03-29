from Persona import Persona
class empleado (Persona):
    cargo=""
    valorHora=0 
    horasTrabajadas=0
    departamento=""
    def __init__(self, cargo, valorHora, horasTrabajadas, departamento, tipoDocumento, documento, nombre, apellido, peso, estatura, edad, sexo) :
        super().__init__(tipoDocumento,documento, nombre, apellido, peso, estatura, edad, sexo)
        self.cargo=cargo 
        self.valorHora=valorHora
        self.horasTrabajadas=horasTrabajadas
        self.departamento=departamento
    def pedirDatos(self):
        self.tipoDocumento = input("Ingrese tipo documento ")
        self.documento = input("Ingrese documento ")
        self.nombre = input("Ingrese su nombre ")
        self.apellido = input("Ingrese su apellido ")
        self.valorHora=int(input("Ingrese el valor de la hora "))
        self.horaTrabajadas= int(input("Ingrese la cantidad de horas trabajadas "))
        self.cargo=input("Ingrese su cargo ")
        self.departamento=input("Ingrese al departamento que pertenece ")
    def imprimirEmpleado(self):
        print(f"el tipo de documento y número de documento de {self.nombre} {self.apellido} es {self.tipoDocumento} y {self.documento}") 
        print(f"su cargo es{self.cargo} y su departamento es {self.departamento} ") 
        print(f"su valor por hora es {self.valorHora} con un total de horas trabajadas de {self.horasTrabajadas} y un total a pagar de{total}")
    def calcularHonorarios(self):
        total =(self.valorHora * self.horasTrabajadas)* int(0.966)
        return total
    

    

laura=empleado("","","","","","","","",0,0,0,"")
laura.pedirDatos()
total= laura.calcularHonorarios()   
laura.imprimirEmpleado()      



