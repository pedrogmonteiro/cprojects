#2.1.1 TAD posicao
#construção
def cria_posicao(col,lin):
    """
    Cria uma posição no tabuleiro a partir de uma coluna e uma linha.

    Parametros:
        col (str): A coluna da posição, uma letra de 'a' a 'j'.
        lin (int): A linha da posição, um número inteiro entre 1 e 10."""
    
    if not (type(col) == str and col in 'abcdefghij' and len(col) == 1 and type(lin) == int and 1 <= lin <= 10):
        raise ValueError('cria_posicao: argumentos invalidos')
    return (col,lin)


#seletores
def obtem_pos_col(p):
    """
    Obtém a coluna da posição.

    Parametros:
        p (tuple): A posição representada como um tuplo (coluna, linha)."""
    
    return p[0]


def obtem_pos_lin(p):
    """
    Obtém a linha da posição.

    Parametros:
        p (tuple): A posição representada como um tuplo (coluna, linha)."""
    
    return p[1]


#reconhecedor
def eh_posicao(arg):
    """
    Verifica se o argumento é uma posição válida no tabuleiro.

    Parametros:
        arg: Argumento a ser verificado."""
    
    return (type(arg) == tuple and len(arg) == 2 and type(arg[0]) == str and len(arg[0]) == 1 and
    arg[0] in 'abcdefghij' and type(arg[1]) == int and 1 <= arg[1] <= 10)


#teste
def posicoes_iguais(p1,p2):
    """
    Verifica se as duas posições são iguais.

    Parametros:
        p1: A primeira posição a ser comparada.
        p2: A segunda posição a ser comparada."""
    
    return (obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2))


#transformador
def posicao_para_str(p):
    """
    Converte uma posição em uma representação de string.

    Parametros:
        p: A posição a ser convertida, representada como um tuplo (coluna, linha)."""
    
    return f'{obtem_pos_col(p)}{obtem_pos_lin(p)}'


def str_para_posicao(s):
    """Converte uma string em uma posição.

    Parametros:
        s (str): A string representando a posição, no formato 'coluna - linha'."""
    
    return cria_posicao(str(s[0]), int(s[1:]))


#funcoes alto nivel
def eh_posicao_valida(p,n):
    """
    posicao x inteiro → booleano
    Verifica se uma posição é válida dentro das restrições do tabuleiro.

    Parametros:
        p: A posição a ser verificada, representada como um tuplo (coluna, linha).
        n (int): O tamanho do tabuleiro, que deve estar entre 2 e 5."""
    
    colunas = ['a','b','c','d','e','f','g','h','i']
    return (eh_posicao(p) and 2 <= n <= 5 and obtem_pos_col(p) in colunas[:2*n] \
        and 1 <= obtem_pos_lin(p) <= 2*n)


#eh_posicao(p) and 2 <= n <= 5 and 
def obtem_posicoes_adjacentes(p,n,d):
    """
    posicao x inteiro x booleano 7→ tuplo
    Retorna as posições adjacentes válidas ao redor de uma posição especificada em uma grade.

    Args:
        p (tuple): Posição atual representada como um tuplo (coluna, linha).
        n (int): Número de órbitas.
        d (bool): Se True, inclui as diagonais como adjacentes;\
            se False, considera apenas adjacentes horizontais e verticais."""
    
    col , lin, adjacentes_sem_erro = obtem_pos_col(p) , int(obtem_pos_lin(p)), ()
    if d:
        adjacentes = ((col,lin - 1),\
                     (chr(ord(col)+ 1),lin - 1), \
                     (chr(ord(col)+1),lin),\
                     (chr(ord(col)+1),lin + 1), \
                     (col,lin + 1),\
                     (chr(ord(col)-1),lin + 1), \
                     (chr(ord(col)-1),lin),\
                     (chr(ord(col)-1),lin - 1))
    if not d:
        adjacentes = ((col,lin - 1),\
                     (chr(ord(col)+1),lin), \
                     (col,lin + 1),\
                     (chr(ord(col)-1),lin))
        
    for pos in adjacentes:
        if eh_posicao_valida(pos,n):
            adjacentes_sem_erro += (pos,)

    return adjacentes_sem_erro


#auxiliar
def distancia_centro(pos,n):
    """
    Calcula a distância de uma posição ao centro de uma grade.

    Args:
        pos (tuple): Posição representada como um tuplo (coluna, linha).
        n (int): Número de órbitas."""
    col = ord(obtem_pos_col(pos)) - ord('a') + 1
    lin = int(obtem_pos_lin(pos))
    centro = n + 0.5
    distancia = max(abs(col - centro), abs(lin - centro))
    return distancia


def ordena_posicoes(t,n):
    """
    tuplo x inteiro → tuplo
    Ordena uma sequência de posições de acordo com a distância ao centro e, 
    em caso de empate, pela linha e coluna.

    Args:
        t (tuple): Tuplo de posições a ordenar, com cada posição no formato (coluna, linha).
        n (int): Número de órbitas."""
    return tuple(sorted(t, key=lambda pos: (distancia_centro(pos, n), obtem_pos_lin(pos), obtem_pos_col(pos))))
print(ordena_posicoes((('a',1),('b',1),('c',1),('d',1)),2))
    

#2.1.2 TAD pedra
#construtor
def cria_pedra_branca(): #cria uma pedra branca
    return -1

def cria_pedra_preta(): #cria uma pedra preta
    return 1

def  cria_pedra_neutra(): #cria uma pedra vazia
    return 0

#reconhecedor
def eh_pedra(arg): #verifica se é uma pedra
    return (arg == 1 or arg == -1 or arg == 0)


def eh_pedra_branca(arg): #verifica se é uma pedra branca
    return arg == cria_pedra_branca()


def eh_pedra_preta(arg): #verifica se é uma pedra preta
    return arg == cria_pedra_preta()


#teste
def pedras_iguais(p1,p2): #verifica se as pedras são iguais
    return (eh_pedra(p1) and eh_pedra(p2) and p1 == p2)


#transformador
def pedra_para_str(p): #passa a pedra para string
    if eh_pedra_branca(p): return 'O'
    if eh_pedra_preta(p): return 'X'
    else: return ' '


#funcoes de alto nivel
def eh_pedra_jogador(p): #verifica se a pedra é de um jogador
    """pedra → booleano"""
    return (eh_pedra_branca(p) or eh_pedra_preta(p))


def pedra_para_int(p): #passa a pedra para inteiro
    """pedra → int"""
    if eh_pedra_branca(p): return -1
    if eh_pedra_preta(p) == 1: return 1
    else: return 0


#2.1.3 TAD tabuleiro
#construtor
def cria_tabuleiro_vazio(n):
    """
    Cria um tabuleiro vazio com dimensões baseadas no valor de n.

    Args:
        n (int): Número de órbitas."""
    if not (2 <= n <= 5):
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    tabuleiro = []
    for i in range(n*2):
        linha = [(cria_pedra_neutra()) for _ in range(n*2)]
        tabuleiro.append(linha)
    return tabuleiro



def cria_tabuleiro(n,tp,tb):
    """
    Cria um tabuleiro com pedras posicionadas conforme as listas fornecidas.

    Args:
        n (int): Número de órbitas.
        tp (tuple): Posições das pedras pretas, representadas como tuplos (coluna, linha).
        tb (tuple): Posições das pedras brancas, representadas como tuplos (coluna, linha)."""
    
    tabuleiro = cria_tabuleiro_vazio(n)
    for pos in tp:
        col = ord(obtem_pos_col(pos)) - ord('a')
        lin = int(obtem_pos_lin(pos)) - 1
        tabuleiro[lin][col] = cria_pedra_preta()
    
    for pos in tb:
        col = ord(obtem_pos_col(pos)) - ord('a')
        lin = int(obtem_pos_lin(pos)) - 1
        tabuleiro[lin][col] = cria_pedra_branca()
    return tabuleiro


def cria_copia_tabuleiro(t): #cria uma copia do tabuleiro
    copia_tabuleiro = []
    for linha in t:
        nova_linha = linha.copy()
        copia_tabuleiro.append(nova_linha)
    return copia_tabuleiro



#seletores
def obtem_numero_orbitas(t): #atraves do tabuleiro obtem o numero de orbitas
    return int(len(t)/2)

def obtem_pedra(t,p): #obtem pedra de uma certa posição do tabuleiro
    col = ord(obtem_pos_col(p)) - ord('a')
    lin = int(obtem_pos_lin(p)) - 1
    return t[lin][col]


def obtem_linha_horizontal(t,p):
     """
    Obtém a linha horizontal de uma posição em um tabuleiro.

    Args:
        t (list): O tabuleiro representado como uma lista de listas.
        p (tuple): A posição inicial representada como um tuplo (coluna, linha)."""
     lin = obtem_pos_lin(p)
     linha_horizontal = ()
     for j in range(len(t[lin - 1])):
        col = chr(ord('a') + j)
        posicao = cria_posicao(col,lin)
        linha_horizontal += ((posicao, obtem_pedra(t,posicao)),)
     return linha_horizontal


def obtem_linha_vertical(t,p):
    """
    Obtém a linha vertical de uma posição em um tabuleiro.

    Args:
        t (list): O tabuleiro representado como uma lista de listas.
        p (tuple): A posição inicial representada como um tuplo (coluna, linha)."""
    col = obtem_pos_col(p)
    linha_vertical = ()
    for j in range(len(t)):
        lin = j + 1
        posicao = cria_posicao(col,lin)
        linha_vertical += ((posicao, obtem_pedra(t,posicao)),)
    return linha_vertical


def obtem_linhas_diagonais(t, p):
    """
    Obtém as diagonais que passam por uma posição específica no tabuleiro.

    Args:
        t (list): O tabuleiro representado como uma lista de listas.
        p (tuple): A posição inicial, representada como um tuplo (coluna, linha)."""
    
    diagonal = []
    antidiagonal = []
    
    col_idx = ord(obtem_pos_col(p)) - ord('a')
    lin_idx = obtem_pos_lin(p) - 1
    tamanho = len(t)
    
    i, j = lin_idx, col_idx
    while i >= 0 and j >= 0:
        pos = cria_posicao(chr(ord('a') + j), i + 1)
        diagonal.insert(0, (pos, obtem_pedra(t, pos)))
        i -= 1
        j -= 1

    i, j = lin_idx + 1, col_idx + 1
    while i < tamanho and j < tamanho:
        pos = cria_posicao(chr(ord('a') + j), i + 1)
        diagonal.append((pos, obtem_pedra(t, pos)))
        i += 1
        j += 1

    #antidiagonal
    i, j = lin_idx, col_idx
    while i >= 0 and j < tamanho:
        pos = cria_posicao(chr(ord('a') + j), i + 1)
        antidiagonal.append((pos, obtem_pedra(t, pos)))
        i -= 1
        j += 1
    
    i, j = lin_idx + 1, col_idx - 1
    while i < tamanho and j >= 0:
        pos = cria_posicao(chr(ord('a') + j), i + 1)
        antidiagonal.insert(0, (pos, obtem_pedra(t, pos)))
        i += 1
        j -= 1
    return tuple(diagonal), tuple(antidiagonal)


def obtem_posicoes_pedra(t,j):
    """
    Retorna todas as posições das pedras de um jogador específico no tabuleiro.

    Args:
        t (list): O tabuleiro representado como uma lista de listas.
        j (int): O jogador, representado por -1 (pedra branca), 1 (pedra preta), ou 0 (pedra neutra)."""
    
    posicoes_pedra = ()
    for lin in range(len(t)):
        for col in range(len(t[lin])):
            pos = cria_posicao(chr(ord('a') + col), lin + 1)
            pedra = obtem_pedra(t, pos)
            if pedra_para_int(pedra) == j:
                posicoes_pedra += (pos,)
    posicoes_pedra = ordena_posicoes(posicoes_pedra,obtem_numero_orbitas(t))
    return posicoes_pedra


#modificadores
def coloca_pedra(t,p,j): #coloca a pedra no tabuleiro
    col = ord(obtem_pos_col(p)) - ord('a')
    lin = obtem_pos_lin(p) - 1
    t[lin][col] = j


def remove_pedra(t,p): #remove a pedra no tabuleiro
    col = ord(obtem_pos_col(p)) - ord('a')
    lin = obtem_pos_lin(p) - 1
    t[lin][col] = cria_pedra_neutra()


#Reconhecedor
def eh_tabuleiro(arg): #verifica se é um tabuleiro
    if not (type(arg) == list): return False
    for i in range(len(arg)):
        if (not type(arg[i]) == list): return False
        if not (len(arg[0]) == len(arg[i])): return False
        for j in range(len(arg[i])):
            if not (eh_pedra(arg[i][j])): return False
    return True


#Teste
def tabuleiros_iguais(t1,t2): #verifica se os tabuleiros são iguais
    return (eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2)


#Transformador
def tabuleiro_para_str(t):
    """
    Converte o tabuleiro de jogo em uma string formatada para visualização.

    Args:
        t (list): Tabuleiro representado como uma lista de listas, onde cada célula é uma pedra (-1, 0, ou 1)."""
    jogadores = {1:pedra_para_str(cria_pedra_preta()),\
                 -1:pedra_para_str(cria_pedra_branca()),\
                0:pedra_para_str(cria_pedra_neutra())}
    tabuleiro  = '    '
    
    for i in range(len(t)):
        tabuleiro += chr(ord('a') + i) + '   '
    tabuleiro = tabuleiro[:-3]
    tabuleiro += '\n'
    espaço = '    '
    for m in range(len(t[0])):
        espaço += '|   '
    espaço = espaço[:-3]
    for i in range(len(t)):
        if i + 1 < 10:
            linha = f'0{i+1} '
        else:
            linha = '10 '
        for j in range(len(t[i])):
            linha += f'[{jogadores[t[i][j]]}]-'
        linha = linha[:-1]
        tabuleiro += linha + '\n'
        tabuleiro += espaço + '\n'

    return tabuleiro[:-len(espaço)-2]


#função alto nivel TAD
def move_pedra(t,p1,p2): #move a pedra no tabuleiro
    '''tabuleiro x posicao x posicao → tabuleiro'''
    coloca_pedra(t,p2,obtem_pedra(t,p1))
    remove_pedra(t,p1)
    return t


#auxiliar
def posicoes_do_tabuleiro(t):
    posicoes = []
    for i in range(len(t)):
        for j in range(len(t[0])):
            posicoes += [posicao_para_str(cria_posicao(chr(ord('a') + i),j + 1))]
    return ordena_posicoes(posicoes,obtem_numero_orbitas(t))


def obtem_posicao_seguinte(t,p,s):
    """
    tabuleiro x posicao x booleano → posicao
    Obtém a posição seguinte em um tabuleiro com base na posição atual e na direção desejada.

    Args:
        t: O tabuleiro representado como uma lista de listas de pedras.
        p: A posição atual, representada como um tuplo (coluna, linha).
        s (bool): Direção da movimentação; True para sentido horário e False para sentido anti-horário."""
    n = obtem_numero_orbitas(t)
    orbita = distancia_centro(p,n)
    adjacentes = obtem_posicoes_adjacentes(p,n,False)
    adjacentes_orbita = []
    for pos in adjacentes:
        if distancia_centro(pos,n) == orbita:
            adjacentes_orbita += [pos]
    diagonais = obtem_linhas_diagonais(t,cria_posicao('a',1))[0]
    adjacentes_orbita = ordena_posicoes(adjacentes_orbita,n)
    diagonais_l = []
    for i in range(len(diagonais)):
        diagonais_l += [diagonais[i][0]]
    p_parte_diagonais, s_parte_diagonais = diagonais_l[:n], diagonais_l[n:]
    diagonal_linha = p
    for i in diagonais_l:
        if obtem_pos_lin(p) == obtem_pos_lin(i):
            diagonal_linha = i
    if s: #Sentido horário
        if p in p_parte_diagonais:
            return adjacentes_orbita[0]
        if p in s_parte_diagonais:
           return adjacentes_orbita[1]
        if posicao_para_str(p) > posicao_para_str(diagonal_linha):
            return adjacentes_orbita[1]
        if posicao_para_str(p) < posicao_para_str(diagonal_linha):
            return adjacentes_orbita[0]
    if not s: #Sentido anti-horário
        if p in p_parte_diagonais:
            return adjacentes_orbita[1]
        if p in s_parte_diagonais:
           return adjacentes_orbita[0]
        if posicao_para_str(p) > posicao_para_str(diagonal_linha):
            return adjacentes_orbita[0]
        if posicao_para_str(p) < posicao_para_str(diagonal_linha):
            return adjacentes_orbita[1]


def roda_tabuleiro(t):
    '''tabuleiro → tabuleiro'''
    #Rotaciona o tabuleiro 90 graus no sentido anti-horário.

    #Args:
    #    t: O tabuleiro representado como uma lista de listas de pedras.
    copia_t = cria_copia_tabuleiro(t)
    tab_rotacionado = cria_tabuleiro_vazio(obtem_numero_orbitas(t))

    for peca in posicoes_do_tabuleiro(copia_t):
        pos_atual = str_para_posicao(peca)
        nova_pos = obtem_posicao_seguinte(copia_t,pos_atual,False)
        coloca_pedra(tab_rotacionado,nova_pos,obtem_pedra(copia_t,pos_atual))
    
    for lin in range(len(t)):
        for col in range(len(t[0])):
            t[lin][col] = tab_rotacionado[lin][col]            
    return t


def verifica_linha_pedras(t,p,j,k):
    """
    tabuleiro x posicao x pedra x int → booleano
    Verifica se há pelo menos `k` pedras do tipo `j` em linha (horizontal, vertical ou diagonal) 
    a partir da posição `p`.

    Args:
        t: O tabuleiro representado como uma lista de listas de pedras.
        p: A posição inicial para verificar, representada como um tuplo (coluna, linha).
        j: O tipo da pedra a ser verificada.
        k: O número mínimo de pedras consecutivas necessárias para considerar uma linha válida."""
    if obtem_pedra(t,p) != j:
        return False
    for linha in (obtem_linha_horizontal(t, p), obtem_linha_vertical(t, p) \
        ,obtem_linhas_diagonais(t, p)[0] , obtem_linhas_diagonais(t,p)[1]):
        posicoes, pedras = zip(*linha)
        idx = posicoes.index(p)
        count = 1
        for i in range(idx + 1, len(pedras)):
            if pedras[i] == j:
                count += 1
            else:
                break
        for i in range(idx - 1, -1, -1):
            if pedras[i] == j:
                count += 1
            else:
                break
        if count >= k:
            return True
    return False



#2.2

def eh_vencedor(t, j): #2.2.1 
    #verifica qual é o vencedor | tabuleiro x pedra → booleano
    k = 2*obtem_numero_orbitas(t)
    for pos in obtem_posicoes_pedra(t,j):
        if verifica_linha_pedras(t,pos,j,k):
            return True
    return False


def eh_fim_jogo(t): #2.2.2
    #verifica se o jogo acabou | tabuleiro → booleano
    if eh_vencedor(t,cria_pedra_branca()) or eh_vencedor(t,cria_pedra_preta()):
        return True
    for linha in t:
        for peca in linha:
            if peca == cria_pedra_neutra():
                return False
    return True


#auxiliar
def obtem_posicoes_livres(t):
    #obtem as posicoes livres do tabuleiro
    livres = ()
    posicoes = posicoes_do_tabuleiro(t)
    for posicao in posicoes:
        if obtem_pedra(t,str_para_posicao(posicao)) == cria_pedra_neutra():
            livres += (str_para_posicao(posicao),)
    return livres

def escolhe_movimento_manual(t): #2.2.3
    """
    tabuleiro → posicao 
    Solicita ao jogador para escolher uma posição livre no tabuleiro. 
    O jogador deve inserir uma posição no formato de coluna (a-i) e linha (1-10). 
    A função verifica se a posição está livre e continua solicitando até que uma posição válida 
    e livre seja escolhida.

    Args:
        t: O tabuleiro representado como uma lista de listas de pedras."""
    
    pergunta = input('Escolha uma posicao livre:')
    if not (len(pergunta) == 2 and pergunta[0] in 'abcdefghi' and 1 <= int(pergunta[1]) <= 10 \
            and type(int(pergunta[1])) == int):
        while not (len(pergunta) == 2 and pergunta[0] in 'abcdefghi' and 1 \
                   <= int(pergunta[1]) <= 10 and type(int(pergunta[1])) == int):
            pergunta = input('Escolha uma posicao livre:')
    pergunta_pos = str_para_posicao(posicao_para_str(pergunta))
    if obtem_pedra(t,pergunta_pos) != cria_pedra_neutra():
        while obtem_pedra(t,pergunta_pos) != cria_pedra_neutra():
            pergunta = input('Escolha uma posicao livre:')
            pergunta_pos = str_para_posicao(posicao_para_str(pergunta))
    return pergunta_pos


def escolhe_movimento_auto(t,j,lvl): #2.2.4
    """
    tabuleiro x pedra x str → posicao
    Determina a próxima posição para um movimento automático no tabuleiro com base no nível de dificuldade.
    O nível pode ser 'facil' ou 'normal'. A função procura posições disponíveis para o jogador, 
    priorizando a defesa e ataque em diferentes níveis de dificuldade.

    Args:
        t: O tabuleiro representado como uma lista de listas de pedras.
        j: O identificador da pedra do jogador (número).
        lvl: O nível de dificuldade ('facil' ou 'normal')."""
    pos_j = ()
    n = obtem_numero_orbitas(t)
    if lvl == 'facil':
        if len(obtem_posicoes_pedra(t,j)) != 0:
            posicao = ordena_posicoes(obtem_posicoes_pedra(t,j),n)[0]
            adjacentes = ordena_posicoes(obtem_posicoes_adjacentes(posicao,n,True),n)
            for p in adjacentes:
                if obtem_pedra(t,p) == cria_pedra_neutra():
                    return p
        return ordena_posicoes(obtem_posicoes_livres(t),n)[0]

    if lvl == 'normal':
         posicoes_disponiveis_maquina = []
    posicoes_disponiveis_adversario = []
    k = 2*n
    for l in range(k,0,-1):
        tab_rodado = roda_tabuleiro(t)
        for pos_jog in ordena_posicoes(obtem_posicoes_livres(tab_rodado),n):
            new_tab = coloca_pedra(tab_rodado,pos_jog, j)

            if verifica_linha_pedras(new_tab, pos_jog,j,l):
                return obtem_posicao_seguinte(new_tab,pos_jog,True)
        for pos_jog in ordena_posicoes(obtem_posicoes_livres(tab_rodado),n):
            new_tab2 = coloca_pedra(tab_rodado,pos_jog, -j)
            if verifica_linha_pedras(new_tab2, pos_jog,-j,l):
                return obtem_posicao_seguinte(new_tab2,pos_jog,True)
    return (ordena_posicoes(t,obtem_posicoes_livres(t)))[0]


def orbito(n,modo,jog): #2.2.5
    if not (type(n) == int and 2 <= n <= 5 and type(modo) == str and (modo == 'facil' or modo == 'normal' or \
       modo == '2jogadores') and (jog == 'O' or jog == 'X') ):
        raise ValueError('orbito: argumentos invalidos')
    
    print(f'Bem-vindo ao ORBITO-{n}.')
    tab = cria_tabuleiro_vazio(n)
    if modo == '2jogadores':
        print('Jogo para dois jogadores.')
    else:
        print(f'Jogo contra o computador ({modo})')
        print(f"O jogador joga com '{jog}'")
    jog = 1 if jog == 'X' else -1
    if modo != '2jogadores':
        print(tabuleiro_para_str(tab))