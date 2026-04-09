from enum import Enum

tabuleiro_alvo = [[1,2,3],
                  [8,0,4],
                  [7,6,5]]

class Mov(Enum):
    ESQUERDA = 0,
    CIMA = 1,
    DIREITA = 2,
    BAIXO = 3

class Tabuleiro: 
    def __init__(self, tabuleiro:list[list[int]]=None) -> None:
        self.tabuleiro:list[list[int]] = ([[2,8,3],
                                       [1,6,4],
                                       [7,0,5]]) if tabuleiro == None else tabuleiro
        self.heuristica:int = self.calcula_heuristica()
        self.posicao_zero:tuple[int] = [2, 1]
        self.caminhos_possiveis:list[int] = self.retorna_caminhos()
        
    def calcula_heuristica(self) -> int:
        heuristica = 0
        for idx_linha, linha in enumerate(self.tabuleiro): 
            for idx_num, num in enumerate(linha):
                if num == tabuleiro_alvo[idx_linha][idx_num]:
                    heuristica += 1
        return heuristica
    
    def _calcula_heuristica(tabuleiro) -> int:
        heuristica = 0
        for idx_linha in range(0, len(tabuleiro) - 1): 
            for idx_num in range(0, idx_linha):
                if tabuleiro[idx_linha][idx_num] == tabuleiro_alvo[idx_linha][idx_num]:
                    heuristica += 1
        return heuristica
    
    def retorna_caminhos(self) -> list[int]:
        caminhos:list[int] = []
        # Avalia a posição do zero em relação à linha do tabuleiro
        if self.posicao_zero[0] == 0:
            caminhos.append(Mov.BAIXO.value)
        elif self.posicao_zero[0] == 1: 
            caminhos.append(Mov.CIMA.value)
            caminhos.append(Mov.BAIXO.value)
        elif self.posicao_zero[0] == 2:
            caminhos.append(Mov.CIMA.value)
            
        # Avalia a posição do zero em relação à coluna do tabuleiro
        if self.posicao_zero[1] == 0:
            caminhos.append(Mov.DIREITA.value)
        elif self.posicao_zero[1] == 1:
            caminhos.append(Mov.DIREITA.value)
            caminhos.append(Mov.ESQUERDA.value)
        elif self.posicao_zero[1] == 2:
            caminhos.append(Mov.ESQUERDA.value)
            
        return caminhos.sort()
    
print(Tabuleiro().caminhos_possiveis)
print(Tabuleiro().heuristica)
print(Tabuleiro().posicao_zero)