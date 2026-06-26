class Grupo :



#Objetivo: Método constructor de la clase Grupo
#Entrada: Nombre del grupo
#Salida: Un objeto tal construido de la clase Grupo
#Restricciones: nombre_grupo debe ser un string no vacío
    def __init__(self, nombre_grupo):

        

        self.__nombre_grupo = nombre_grupo

        self.__equipos = []

        self.__partidos = []


#Objetivo: Método que agrega un equipo a la lista de equipos del grupo
#Entrada: equipo (objeto de la clase Equipo), es una selección de un país que participa en el grupo
#Salida: Se agrega el equipo a la lista de equipos del grupo
#Restricciones: El equipo no puede ya estar en la lista del grupo, y debe tener máximo 3 selecciones para poder añadírsele una más.

    def agregar_equipo(self, equipo):
#Validad que no sea de =+4 el grupo ya.
        if len(self.__equipos) == 4:

            return f"Grupo ya tiene 4 selecciones"
        
#Validar no repetidos
        for seleccion in self.__equipos: 

            

            if seleccion == self.__equipos:

                return f"equipo ya está en el grupo"
            
#Añadir selección al grupo

        self.__equipos.append(equipo)
            

            
