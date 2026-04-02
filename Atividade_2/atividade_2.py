# Movimentos/posição da peça vazia no grafo: 
# ◄ = 0, ► = 1, ▲ = 2, ▼ = 3

class EnumMov(Enum):
    ESQUERDA = 0
    DIREITA = 1
    CIMA = 2
    BAIXO = 3
    
# 0 1 2
# 3 4 5
# 6 7 8 

class Estado:
    def __init__(self, valor: list[Estado]):
        self.proximos_estados:list[list[Estado]] = []
        self.valor:list[Estado] = valor

class Tabuleiro:
    def __init__(self, lista_estados:list[Estado]):
        self.lista_estados:list[Estado] = lista_estados
        self.tabuleiro_atual:list[Estado] = self.__monta_tabuleiro(self.lista_estados)
        self.grafo:Estado = self.__monta_grafo(self.tabuleiro_atual)
        
    def move_peca(self, tabuleiro:list[Estado], movimento:int) -> list[Estado]:
        """
        Faz um movimento da peça vazia no tabuleiro baseado no número colocado para o movimento
        Movimentos/posição da peça vazia no grafo: 
        ◄ = 0, ► = 1, ▲ = 2, ▼ = 3
        
        Args:
            movimento (int): Número do movimento
            tabuleiro (list[Estado]): Tabuleiro atual

        Returns:
            list[Estado]: Tabuleiro após o movimento da peça vazia
        """
        posicao_peca_vazia:int = tabuleiro.index(self.lista_estados[0])
        posicao_alvo:int
        if movimento == EnumMov.ESQUERDA:
            posicao_alvo = posicao_peca_vazia - 1
        elif movimento == EnumMov.DIREITA:
            posicao_alvo = posicao_peca_vazia + 1
        elif movimento == EnumMov.CIMA:
            posicao_alvo = posicao_peca_vazia - 3
        elif movimento == EnumMov.BAIXO:
            posicao_alvo = posicao_peca_vazia + 3
        
        
    def __movimentos_possiveis(posicao: int) -> list[int]:
        """
        Retorna a quantidade de movimentos possíveis baseado na posição atual da peça vazia

        Args:
            posicao (int): Posição atual da peça vazia

        Returns:
            int: Número de movimentos possíveis da peça vazia
        """
        match posicao:
            case 0:
                return [EnumMov.BAIXO, EnumMov.DIREITA]
            case 1:
                return [EnumMov.ESQUERDA, EnumMov.BAIXO, EnumMov.DIREITA]
            case 2: 
                return [EnumMov.ESQUERDA, EnumMov.BAIXO]
            case 3: 
                return [EnumMov.CIMA, EnumMov.DIREITA, EnumMov.BAIXO]
            case 4: 
                return [EnumMov.ESQUERDA, EnumMov.CIMA, EnumMov.DIREITA, EnumMov.BAIXO]
            case 5:
                return [EnumMov.ESQUERDA, EnumMov.CIMA, EnumMov.DIREITA]
            case 6: 
                return [EnumMov.CIMA, EnumMov.DIREITA]
            case 7: 
                return [EnumMov.ESQUERDA, EnumMov.CIMA, EnumMov.DIREITA]
            case 8: 
                return [EnumMov.ESQUERDA, EnumMov.CIMA]
        
    
    def __monta_tabuleiro(tabuleiro:list[Estado]) -> list[Estado]:
        return [tabuleiro[2], tabuleiro [8], tabuleiro[3],
                tabuleiro[1], tabuleiro[6], tabuleiro[4],
                tabuleiro[7], tabuleiro[0], tabuleiro[5]]
        
    def __monta_grafo(tabuleiro:list[Estado]) -> Estado:
        """
        Recebe o tabuleiro atual e retorna o estado inicial do grafo

        Args:
            tabuleiro (list[Estado]): Lista de estados que representa o tabuleiro atual

        Returns:
            Estado: Estado inicial do grafo
        """
        for 

tabuleiro = Tabuleiro(list(map(lambda x: Estado(x), range(0, 8))))

def mostra_tabuleiro(tabuleiro: list[list[str]]) -> None:
    for linha in tabuleiro:
        print(f"{linha[0]} {linha[1]} {linha[2]}")        

def busca_dfs(tabuleiro: list[list[str]]):