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
        promedio = self.promedio()
        if self.fecha != None and self.promedio <=5.9:
            dateGrad = "NO"
        else: 
            dateGrad = "SI"
        return dateGrad


    def getDate(self):
        promedio = self.promedio()
        gradDate = " "
        if promedio <= 5.9:
            gradDate = "N/A"
        else:
            fecha = self.fecha
            gradDate = fecha
        return gradDate

    def getTesis(self):
        promedio = self.promedio()

        if promedio <= 5.9:
            print("N/A")
        else:
            tesis = self.tesis
            gradTesis = tesis
        return gradTesis

    def __str__(self): 
        promedio = self.getPromedio()
        if promedio <= 5.9:
            return f" Matricula: {self.matricula} Nombre completo: {self.nombre} {self.apellido} Edad: {self.edad} Alumno no graduado"
        else:
            return f" Nombre Completo: {self.nombre} {self.apellido} Edad: {self.edad} Matricula: {self.matricula} Graduado: {self.fecha} con la Tesis {self.tesis}"
