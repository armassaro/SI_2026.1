class No:
    def __init__(self, label:str, visitado:bool=False, proximos_nos:list[No]=[]): 
        self.label = label
        self.visitado = visitado
        self.proximos_nos = proximos_nos
        
lista_nos:dict[str, No] = {
    "A": No("A"),
    "B": No("B"),
    "C": No("C"),
    "D": No("D"),
    "E": No("E")
}
