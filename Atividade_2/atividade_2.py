# Movimentos/posição da peça vazia no grafo: 
# ◄ = 0, ► = 1, ▲ = 2, ▼ = 3

class Estado:
    def __init__(self, valor):
        self.proximos_estados:list[Estado] = []
        self.valor:str = valor
    
tabuleiro:list[list[str]] = [["2", "8", "3"], ["1", "6", "4"], ["7", "_", "5"]]

def move_peca(tabuleiro: list[list[str]], movimento:int) -> list[list[str]]:
    if(movimento == 0)    

def mostra_tabuleiro(tabuleiro: list[list[str]]) -> None:
    for linha in tabuleiro:
        print(f"{linha[0]} {linha[1]} {linha[2]}")        

def busca_dfs(tabuleiro: list[list[str]]): 