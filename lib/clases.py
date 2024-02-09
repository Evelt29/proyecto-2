class Alumno():
    def __init__(self,matricula,nombre,apellido,edad,promedio=None):
        self.matricula=matricula
        self.nombre=nombre
        self.apellido=apellido
        self.calificacion=[]
        self.edad=edad
        self.promedio = promedio
        
        pass
    
    def setCalificacion(self,calificacion):
        self.calificacion.append(calificacion)
        return calificacion
    def setProm(self,promedio):
        self.promedio= promedio
        return 0
    def getProm(self):
        ZeroDivisionError
        try:
            if type(self.promedio) != type(None):
                prom = sum(self.calificacion) /len(self.calificacion)
        except Exception as e:
            print(f"error desconocido")
        return prom  
    def __str__(self):
        return f"matricula: {self.matricula} | nombre: {self.nombre}  {self.apellido} | calificación: {self.calificacion} | final: {self.promedio}"
    
#fin clase alumno-----------------------------------------------------------------------------------------------------------------------------
      
class gradAlumno(Alumno):
    def __init__(self,matricula,nombre,apellido,edad,fecha,graduacion,tesis):
        super().__init__(matricula,nombre,apellido,edad)
        self.fecha = fecha  
        self.graduacion = graduacion
        self. tesis = tesis
        pass
    def setGraduacion(self,graduacion):
        self.graduacion = graduacion
        return graduacion
    def getGraduacion(self):
        prom = self.promedio
        graduacion = " "

        if self.promedio <= 5.9:
            graduacion = "NO"
        else:
            graduacion = "SÍ"
        return graduacion


    def setFecha(self,fecha):
        self.fecha = fecha
        return fecha
    
    def setTesis(self,tesis):
        self.tesis = tesis
        return tesis
    
    def getFecha(self):
        prom = self.promedio
        dateGrad = " "
        if self.promedio <= 5.9:
            dateGrad = "N/A"
        else:
            fecha = self.fecha
            dateGrad = fecha
        return dateGrad
    
    def getTesis(self):
        prom = self.promedio
        tesis = " "
        if self.promedio <= 5.9:
            tesisG = "N/A"
        else:
            tesis = self.tesis
            tesisG = tesis
        return tesisG
    def __str__(self):
        prom = self.promedio()
        if prom <= 5.9:
            return f"matricula: {self.matricula} | nombre: {self.nombre}  {self.apellido} | edad: {self.edad}" 
        else:
            return f"nombre completo: {self.nombre}  {self.apellido} | edad: {self.edad} | matricula: {self.matricula} | se gradua el: {self.fecha} | con su tesis: {self.tesis}"