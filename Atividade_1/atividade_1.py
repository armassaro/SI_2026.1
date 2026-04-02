# Autores: 
# 1 -> Arthur Romano Massaro
# 2 -> Pedro Miguel Lorin 
# 3 -> Paulo Uejima Varella

class No: 
    def __init__(self, valor:str):
        self.valor = valor
        self.proximos_nos = []
        self.visitado = False
        pass
    
lista_nos:list[No] = [No("A"), No("B"), No("C"), No("D"), No("E")]

# Lista de todos os caminhos possíveis
caminhos:list[list[str]] = []
# Array do caminho atual
caminho_atual:list[str] = []

# Gera o grafo do exercício
def gera_grafo() -> None:
    for no in lista_nos:
        no.proximos_nos = list(filter(lambda x: x != no, lista_nos))

def busca(no_inicial: No, no_alvo: No) -> None:
    # Se o nó já foi visitado, volta para o nó anterior
    if no_inicial.visitado:
        return

    # Marca o nó atual como "visitado"
    no_inicial.visitado = True
    
    # Adiciona o nó atual no array de caminho atual
    caminho_atual.append(no_inicial.valor)

    # Se o nó atual for o nó alvo, adiciona o caminho no array de caminhos
    if no_inicial.valor == no_alvo.valor:
        caminhos.append(caminho_atual.copy())
    else:
        for no in no_inicial.proximos_nos:
            busca(no, no_alvo)
    
    caminho_atual.pop()
    no_inicial.visitado = False     
    
gera_grafo()

busca(lista_nos[0], lista_nos[2])

print(list(caminhos))