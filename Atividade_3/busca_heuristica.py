from enum import Enum

class Mov(Enum):
    ESQUERDA = 0,
    CIMA = 1,
    DIREITA = 2,
    BAIXO = 3
    
tabuleiro_alvo = [[1,2,3],
                  [8,0,4],
                  [7,6,5]]

iteracoes:list[Mov] = []

class Tabuleiro: 
    def __init__(self, tabuleiro:list[list[int]]=None) -> None:
        self.tabuleiro:list[list[int]] = ([[2,8,3],
                                       [1,6,4],
                                       [7,0,5]]) if tabuleiro == None else tabuleiro
        self.heuristica:int = self.calcula_heuristica()
        self.posicao_zero:list[int] = [2, 1]
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
    
    def retorna_caminhos(self) -> list[Mov]:
        caminhos:list[int] = []
        # Avalia a posição do zero em relação à linha do tabuleiro
        if self.posicao_zero[0] == 0:
            caminhos.append(Mov.BAIXO)
        elif self.posicao_zero[0] == 1: 
            caminhos.append(Mov.CIMA)
            caminhos.append(Mov.BAIXO)
        elif self.posicao_zero[0] == 2:
            caminhos.append(Mov.CIMA)
            
        # Avalia a posição do zero em relação à coluna do tabuleiro
        if self.posicao_zero[1] == 0:
            caminhos.append(Mov.DIREITA)
        elif self.posicao_zero[1] == 1:
            caminhos.append(Mov.DIREITA)
            caminhos.append(Mov.ESQUERDA)
        elif self.posicao_zero[1] == 2:
            caminhos.append(Mov.ESQUERDA)

        caminhos.sort(key=lambda x: x.value)

        return caminhos
    
    def move_peca(self, movimento: Mov) -> None:
        # Movimento horizontal
        if(movimento == Mov.ESQUERDA or movimento == Mov.DIREITA):
            # Pega o número alvo que será substituído pela peça vazia
            numero_alvo:int = self.tabuleiro[self.posicao_zero[0]][self.posicao_zero[1] - 1 if movimento == Mov.ESQUERDA else self.posicao_zero[1] + 1]
            # Atualiza o índice da posição do zero
            self.posicao_zero = [self.posicao_zero[0], self.posicao_zero[1] - 1 if movimento == Mov.ESQUERDA else self.posicao_zero[1] + 1]
            # Substitui os dois números no tabuleiro
            self.tabuleiro[self.posicao_zero[0]][self.posicao_zero[1] + 1 if movimento == Mov.ESQUERDA else self.posicao_zero[1] - 1] = numero_alvo
            self.tabuleiro[self.posicao_zero[0]][self.posicao_zero[1]] = 0
        else:
            # Pega o número alvo que será substituído pela peça vazia
            numero_alvo:int = self.tabuleiro[self.posicao_zero[0] - 1 if movimento == Mov.CIMA else self.posicao_zero[0] + 1][self.posicao_zero[1]]
            posicao_zero_antiga = self.posicao_zero
            # Atualiza o índice da posição do zero
            self.posicao_zero = [self.posicao_zero[0] - 1 if movimento == Mov.CIMA else self.posicao_zero[0] + 1, self.posicao_zero[1]]
            # Substitui os dois números no tabuleiro
            self.tabuleiro[posicao_zero_antiga[0]][posicao_zero_antiga[1]] = numero_alvo
            self.tabuleiro[self.posicao_zero[0]][self.posicao_zero[1]] = 0
            
    def print_tabuleiro(self):
        print(self.tabuleiro[0].__str__())
        print(self.tabuleiro[1].__str__())
        print(self.tabuleiro[2].__str__())

tabuleiro = Tabuleiro()

tabuleiro.print_tabuleiro()
print()
tabuleiro.move_peca(Mov.CIMA)
tabuleiro.print_tabuleiro()