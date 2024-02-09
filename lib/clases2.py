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
    
    
    def promedio(self):
        ZeroDivisionError
        try:
            prom = sum(self.calificacion) /len(self.calificacion)
        except Exception as e:
            print(f"error desconocido")
        return prom
    
    def __str__(self):
        return f"matricula: {self.matricula} | nombre: {self.nombre}  {self.apellido} | calificación: {self.calificacion} | final: {self.prom}"
    
class gradAlum(Alumno):
    def __init__(self,matricula,nombre,apellido,edad):
        super().__init__(matricula,nombre,apellido,edad)
        pass

    def getGrad(self):
        prom = self.prom()
        dateGrad = " "
        if prom <= 5.9:
            dateGrad = "NO"
        else: 
            dateGrad = "SI"
        return dateGrad

    def setDate(self,fecha):
        self.fecha = fecha
        return fecha
    def getDate(self):
        prom = self.prom()
        gradDate = " "
        if prom <= 5.9:
            gradDate = "N/A"
        else:
            fecha = self.fecha
            gradDate = fecha
        return gradDate
    
    def setTesis(self,tesis):
        self.tesis = tesis
        return tesis
    def getTesis(self):
        prom = self.prom()
        gradTesis = " "
        if prom <= 5.9:
            gradTesis = "N/A"
        else:
            tesis = self.tesis
            gradTesis = tesis
        return gradTesis

    def __str__(self):
        prom = self.prom()
        if prom <= 5.9:
            return f" Matricula: {self.matricula} Nombre completo: {self.nombre} {self.apellido} Edad: {self.edad} Alumno no graduado"
        else:
            return f" Nombre Completo: {self.nombre} {self.apellido} Edad: {self.edad} Matricula: {self.matricula} Graduado: {self.fecha} con la Tesis {self.tesis}"