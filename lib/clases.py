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
            if self.promedio != None:
                prom = sum(self.calificacion) /len(self.calificacion)
        except Exception as e:
            print(f"error desconocido")
        return prom  
    def __str__(self):
        return f"matricula: {self.matricula} | nombre: {self.nombre}  {self.apellido} | calificación: {self.calificacion} | promedio: {self.promedio} | Grad?: {self.graduacion} | fecha: {self.fecha} | tesis: {self.tesis}"
    
#fin clase alumno-----------------------------------------------------------------------------------------------------------------------------
      
class gradAlumno(Alumno):
    def __init__(self,matricula,nombre,apellido,edad,graduacion,fecha=None,tesis=None):
        super().__init__(matricula,nombre,apellido,edad)
        self.graduacion= graduacion
        self.fecha = fecha
        self.tesis = tesis
        pass
    def setGraduacion(self,graduación):
        self.graduacion = graduación
        return 0
    def getGraduacion(self):
        if self.promedio > 6:
            print("sí")
        else:
            print("No")

    def setFecha(self,fecha):
        self.fecha = fecha
        return 0
    def setTesis(self,tesis):
        self.tesis = tesis
        return 0
    def getFecha(self):
        if self.promedio > 6:
            print ("23/05/28")
        else:
            print("N/A")
    def getTesis(self):
        if self.promedio > 6:
            print(" tesis ")
        else: 
            print("N/A")
   
        return f"matricula: {self.matricula} | nombre: {self.nombre}  {self.apellido} | calificación: {self.calificacion} | final: {self.prom_final} | Grad?: {self.graduacion} | fecha: {self.fecha} | tesis: {self.tesis} "