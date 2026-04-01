# lista_caminhos:list[list[No]] = []

# class No:
#     def __init__(self, label:str, visitado:bool=False, proximos_nos:list[No]=[]): 
#         self.label = label
#         self.visitado = visitado
#         self.proximos_nos = proximos_nos
        
# estado_atual:int = None

# lista_nos:dict[str, No] = {
#     "A": No("A"),
#     "B": No("B"),
#     "C": No("C"),
#     "D": No("D"),
#     "E": No("E")
# }

# lista_nos:dict[str, int] = {
#     "A": 0,
#     "B": 1, 
#     "C": 2, 
#     "D": 3,
#     "E": 4
# }

# lista_adjacencia = [
#     [False, True, True, True, True],
#     [True, False, True, True, True],
#     [True, True, False, True, True],
#     [True, True, True, False, True],
#     [True, True, True, True, False]
# ]

# def __busca_primeiro_no__(caminhos_no:list[bool]) -> int | None:
#     """
#     Busca o primeiro nó na lista de adjacência de um nó que possui valor True, se não encontrar nenhum nó retorna None

#     Args:
#         caminhos_no (list[bool]): Lista de adjacência de um determinado nó

#     Returns:
#         int | None: Retorna o índice do próximo nó, senão retorna None
#     """
#     for no in caminhos_no:
#         if no == True:
#             caminhos_no[no.__index__()] = False
#             return no.__index__()
#     return None

# def buscar(no_inicial:str, no_final:str) -> list[list[str]]:
#     while __busca_primeiro_no__(lista_adjacencia[lista_nos[no_inicial]]) != None:

#     return

class No:
    def __init__(self, label:str, visitado:bool=False, proximos_nos:list[No]=[]): 
        self.label = label
        self.visitado = visitado
        self.proximos_nos = proximos_nos

lista_nos:list[No] = [No("A"), No("B"), No("C"), No("D"), No("E")]

def cria_grafo() -> None:
    for no in lista_nos:
        no.proximos_nos = filter(lambda x: x != no, lista_nos)
    return 

print(cria_grafo())