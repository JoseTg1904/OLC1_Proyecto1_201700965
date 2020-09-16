class Token:
        
    def __init__(self,tipoToken,recorrido, valor):
        self.tipoToken = tipoToken
        self.valor = valor
        self.recorrido = recorrido

class TokenParea:
    
    def __init__(self, tipo, valor, idP):
        self.tipo = tipo
        self.valor = valor
        self.idP = idP

class ResultadoSintactico:

    def __init__(self, operacion, resultado):
        self.operacion = operacion
        self.resultado = resultado