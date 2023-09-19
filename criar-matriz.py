#Função de criar matriz

def main():
    A=cria_matriz()
    imprime_matriz(A)
def cria_matriz():
    '''Nome->matriz
    Pede informações para o usuário(numero de linhas,
    numero de colunas e elementos) e retorna uma matriz
    com essas caracteristicas'''
    n_linhas=int(input("Digite o numero de Linhas:")) 
    n_colunas=int(input("Digite o numero de Colunas:"))
    matriz=[]
    for i in range(n_linhas):
        linha=[]
        for j in range(n_colunas):
            print("Digite o elemento(%d,%d):"%(i+1, j+1), end="") 
            #'end' é só pro print não pular a linha
            num=int(input())
            linha.append(num)
        matriz.append(linha)
    return matriz
#------------------------------------------------------------------------
#Função que imprime a matriz
def imprime_matriz(matriz):
    '''Matriz->None
    Função que imprime uma matriz de forma legível'''
    m=len(matriz)
    n=len(matriz[0])
    for i in range(m):
        for j in range(n):
            print("%6d"%(matriz[i][j]),end="")#[linha][coluna]
#O 6 são os espaços ocupados pelos numeros
        print()#para pular linha
main()