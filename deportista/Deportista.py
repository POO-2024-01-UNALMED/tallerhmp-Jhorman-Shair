class Deportista():
    def __init__(self,nombre,edad,altura,sexo,deporte,añosPracticando):
        super().__init__(nombre,edad,altura,sexo)
        self._deporte=deporte 
        self._añosPracticando=añosPracticando 
    
    def getDeporte(self):
        return self._deporte 
    
    def setDeporte(self,deporte):
        self._deporte=deporte 
        
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticando(self,año):
        self._añosPracticando=año 