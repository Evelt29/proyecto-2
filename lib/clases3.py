class Alumno():
    def __init__(self,matricula,nombre,apellido,edad):
        self.matricula=matricula
        self.nombre=nombre
        self.apellido=apellido
        self.calificacion=[]
        self.edad=edad

        
        pass
    
    def setCalificacion(self,calificacion):
        self.calificacion.append(calificacion)
        return calificacion 
    
    def getPromedio(self):
        ZeroDivisionError
        try:
            promedio = sum(self.calificacion) /len(self.calificacion)
        except Exception as e:
            print(f"error desconocido")
        return promedio
    
    """def __str__(self):
        return f"Nombre Completo: {self.nombre} {self.apellido} Edad: {self.edad} Matricula: {self.matricula} Graduado: {self.fecha} con la Tesis {self.tesis}"
    """
class gradAlum(Alumno):
    def __init__(self,matricula,nombre,apellido,edad,fecha=None,tesis=None,graduacion=None):
        super().__init__(matricula,nombre,apellido,edad)
        self.fecha = fecha
        self.tesis = tesis
        self.graduacion = graduacion
        
        
        pass

    def setDate(self,fecha):
        self.fecha = fecha
        return 0
    
    def setTesis(self,tesis):
        self.tesis = tesis
        return 0
    def setGraduacion(self,graduacion):
        self.graduacion = graduacion
        return 0
    
    def getGrad(self):
        if self.graduacion == None and  self.promedio <=5.9:
            print("NO")
        else: 
            print("SI") 


    def getDate(self):
        promedio = self.promedio()
        if self.fecha == None and self.promedio <= 5.9:
            print("N/A")
        else: 
            print(self.fecha)

    def getTesis(self):
        if self.tesis == None and self. promedio  <=5.9:
            print("N/a")
        else:
            return self.tesis

    def __str__(self): 
        promedio = self.getPromedio()
        if promedio <= 5.9:
            return f"  Nombre completo: {self.nombre} {self.apellido} Matricula: {self.matricula} Edad: {self.edad} Alumno no graduado"
        else:
            return f" Nombre Completo: {self.nombre} {self.apellido} Edad: {self.edad} Matricula: {self.matricula} Graduado: {self.fecha} con la Tesis {self.tesis}"
