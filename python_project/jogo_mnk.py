
def eh_tabuleiro(arg): #2.1.1
    """
    eh_tabuleiro: universal → booleano
    Verifica se o argumento é um tabuleiro válido. Um tabuleiro válido é um
    tuplo de tuplos de inteiros (-1, 0 ou 1), com 2 a 100 linhas e 2 a 100 colunas, 
    onde todas as linhas têm o mesmo número de colunas.
    Parâmetro:
    arg (tuple): Possível tabuleiro a ser verificado.
    """

    if not (type(arg)==tuple and 2 <= len(arg) <= 100):
        return False
    for i in range(len(arg)):
        if not (type(arg[i]) == tuple and len(arg[i]) != 0):
            return False
    for i in range(len(arg)):
        if not(len(arg[0]) == len(arg[i])): #verifica se todas as linhas têm o mesmo numero colunas
            return False
        for j in range(len(arg[0])):
            if not ((arg[i][j] == 0 or arg[i][j] == 1 or arg[i][j] == -1) and type(arg[i][j]) == int):
                return False #verifica se as posicoes sao ocupadas somente por 0, -1 ou 1 e por inteiros
            if not (2 <= len(arg[i]) <= 100):
                return False
            if not (type(arg[i]) == tuple):
                return False
    return True

def eh_posicao(arg): #2.1.2
    """
    eh_posicao: universal → booleano
    Verifica se o argumento é uma posição válida. Uma posição válida é um 
    inteiro entre 1 e 10.000 (inclusive).
    Parâmetro:
    arg (int): Possível posição a ser verificada.
    """

    if type(arg) == (int) and (1 <= arg <= 10000):
        return True
    return False


def obtem_dimensao(tab): #2.1.3
    """
    obtem dimensao: tabuleiro → tuplo
    Retorna as dimensões do tabuleiro. A dimensão é representada por um 
    tuplo contendo o número de linhas e o número de colunas.
    Parâmetro:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    """

    dimensao = (len(tab),len(tab[0]))
    return (dimensao)



def obtem_valor(tab, pos): #2.1.4
    """
    obtem valor: tabuleiro * posicao → inteiro
    Retorna o valor da posição especificada no tabuleiro. A posição é 
    comparada com a posição no tabuleiro.

    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição no tabuleiro.
    """

    s = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if pos == (((j + 1))+(s)): #verifica se está na posição
                return tab[i][j]
        s += len(tab[i])
    return s


def obtem_coluna(tab,pos): #2.1.5
    """
    obtem coluna: tabuleiro * posicao → tuplo
    Retorna as posições de uma coluna no tabuleiro, baseada na posição
    fornecida, ajustando a posição linearizada para determinar a coluna correta.
    Parâmetros:
    tab (tuple): Tabuleiro representado por uma tuplo de tuplos.
    pos (int): Posição inicial para identificar a coluna.
    """

    coluna = ()
    s = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if pos > len(tab[i]):
                while pos > len(tab[i]):
                    pos -= len(tab[i]) #subtrai em loop ate chegar ao primeiro elemento da coluna
            if pos == (j + 1):
                coluna += ((j+1+s),)
        s += len(tab[i])
    return coluna




def obtem_linha(tab,pos): #2.1.6
    """
    obtem linha: tabuleiro * posicao → tuplo 
    Retorna as posições de uma linha no tabuleiro, baseada na posição fornecida,
    ajustando a posição para determinar a linha correta.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição inicial para identificar a linha.
    """
    s = 0
    linha = ()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if pos == (j+1+s): #procura a posicao tendo em conta a linha
                for m in range(len(tab[i])):
                    linha += ((m+1+s),) #adiciona ao tuplo todas as posições da linha
        s += len(tab[i])
    return linha


def obtem_diagonais(tab,pos): #2.1.7
    """
    obtem diagonais: tabuleiro * posicao → tuplo
    Retorna as diagonais que passam por uma posição específica no tabuleiro.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição usada para calcular as diagonais.
    """
    diagonal , antidiagonal = () , ()
    p_diagonal = pos
    p_anti_diagonal = pos
    #para as diagonais
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            #ir para o primeiro elemento da diagonal
            if p_diagonal > len(tab[i]) and p_diagonal not in obtem_coluna(tab,1):
                p_diagonal -= len(tab[i]) + 1
    for i in range(len(tab)):
        diagonal += (p_diagonal,)
        #nao aumentar o numero caso a posicao da diagonal esteja na ultima coluna ou na ultima linha 
        if p_diagonal not in obtem_coluna(tab,len(tab[0])) and p_diagonal not in obtem_linha(tab,len(tab)*len(tab[0])):
            p_diagonal += (len(tab[0]) + 1)
        else:
            break
    #para as antidiagonais
    for i in range(len(tab)):
        if p_anti_diagonal in (obtem_linha(tab, len(tab)*len(tab[i]))) or p_anti_diagonal in (obtem_coluna(tab,1)):
            break
        else: #ir para o primeiro elemento da diagonal
            p_anti_diagonal += len(tab[0]) - 1
    for i in range(len(tab)):
        antidiagonal += (p_anti_diagonal,)
        #nao diminuir o numero caso a antidiagonal esteja na primeira linha ou na ultima coluna
        if p_anti_diagonal in obtem_linha(tab, 1) or p_anti_diagonal in obtem_coluna(tab,len(tab[i])*len(tab)):
            break
        else:
            p_anti_diagonal -= len(tab[i]) - 1
    return (diagonal,antidiagonal)



def tabuleiro_para_str(tab): #2.1.8
    """
    tabuleiro para str: tabuleiro → cad. carateres
    Converte o tabuleiro de jogo para uma string formatada com 'X', 'O', e '+'.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    """
    jogadores = {1:'X',-1:'O',0:'+'}
    tabuleiro = ''
    espaço = ''
    for m in range(len(tab[0])):
        espaço += '|   '
    espaço = espaço[:-3]
    for i in range(len(tab)):
        linha = ''
        for j in range(len(tab[i])):
            linha += jogadores[tab[i][j]] + '---'
        linha = linha[:-3]
        tabuleiro += linha + '\n'
        tabuleiro += espaço + '\n'

    return tabuleiro[:-len(espaço)-2]

def eh_posicao_valida(tab, pos): #2.2.1
    """
    eh posicao valida: tabuleiro * posicao → booleano
    Verifica se uma posição é válida no tabuleiro.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição a ser verificada.
    """
    if eh_tabuleiro(tab) == False or eh_posicao(pos) == False:
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    contador = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            contador += 1
            if contador == pos:
                return True
    return False

def eh_posicao_livre(tab,pos): #2.2.2
    """
    eh posicao livre: tabuleiro * posicao → booleano
    Verifica se uma posição no tabuleiro está livre.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição a ser verificada.
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos)):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    if obtem_valor(tab,pos) == 0:
        return True
    return False

def obtem_posicoes_livres(tab): #2.2.3
    """
    obtem posicoes livres: tabuleiro → tuplo
    Obtém uma tuplo com as posições livres no tabuleiro.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    """
    livres = ()
    posicao = 0
    if not (eh_tabuleiro(tab)):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            posicao += 1
            if obtem_valor(tab,posicao) == 0:
                livres += (posicao,)
    return livres



def eh_jogadores(jog): #verificar se é um jogador ou não
    return (jog == 1 or jog == -1) and type(jog) == int


def obtem_posicoes_jogador(tab,jog): #2.2.4
    """
    obtem posicoes jogador: tabuleiro * inteiro → tuplo
    Obtém as posições ocupadas por um jogador específico no tabuleiro.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    jog (int): Identificador do jogador (-1 ou 1).
    """
    if not (eh_tabuleiro(tab) and eh_jogadores(jog)):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    posicoes_do_jogador = ()
    posicao = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            posicao += 1
            if tab[i][j] == jog:
                posicoes_do_jogador += (posicao,)
    return posicoes_do_jogador

def obtem_coordenadas(tab,pos): #transformar as posições em coordenadas do tabuleiro
    m = 1
    for y in range(len(tab)):
        for x in range(len(tab[y])):
            if m == pos:
                return (x, y)
            m += 1


def obtem_posicoes_porcoordenadas(tab,coordenada): #transformar as coordenadas em posições do tabuleiro
    if not (eh_tabuleiro(tab)):
        pass
    pos = coordenada[1]*len(tab[0]) + coordenada[0] + 1
    return pos

def todas_as_coordendas(tab): #dá todas as coordenadas do tabuleiro
    coordenadas_conjunto = ()
    for i in range(len(tab)*len(tab[0])):
        coordenadas_conjunto += ((obtem_coordenadas(tab,(i + 1))),)
    return coordenadas_conjunto

def obtem_posicoes_adjacentes(tab,pos): #2.2.5
    """
    obtem posicoes adjacentes: tabuleiro * posicao → tuplo
    Obtém as posições adjacentes a uma posição específica no tabuleiro.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição para na qual se deseja encontrar as posições adjacentes.
    """

    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos)):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    adjacentes = ()
    coordenadas_do_tabuleiro = todas_as_coordendas(tab)
    coordenadas = obtem_coordenadas(tab,pos)
    if (coordenadas[0] - 1,coordenadas[1] - 1) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0] - 1,coordenadas[1] - 1)),)
    if (coordenadas[0],coordenadas[1] - 1) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0],coordenadas[1] - 1)),)
    if (coordenadas[0] + 1,coordenadas[1] - 1) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0] + 1,coordenadas[1] - 1)),)
    if (coordenadas[0] - 1,coordenadas[1]) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0] - 1,coordenadas[1])),)
    if (coordenadas[0] + 1,coordenadas[1]) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0] + 1,coordenadas[1])),)
    if (coordenadas[0] - 1,coordenadas[1] + 1) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0] - 1,coordenadas[1] + 1)),)
    if (coordenadas[0],coordenadas[1] + 1) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0],coordenadas[1] + 1)),)
    if (coordenadas[0] + 1,coordenadas[1] + 1) in coordenadas_do_tabuleiro:
            adjacentes += (obtem_posicoes_porcoordenadas(tab,(coordenadas[0] + 1,coordenadas[1] + 1)),)
    return adjacentes


def chebyshev_distance(tab,pos): #faz a distancia das posicoes ao centro do tabuleiro
    m = len(tab)
    n = len(tab[0])
    centro = (m//2)*n + n//2 + 1
    c_centro, c_pos = obtem_coordenadas(tab,centro), obtem_coordenadas(tab,pos)
    distancia = max(abs(c_centro[0] - c_pos[0]), abs(c_centro[1] - c_pos[1]))
    return distancia


def ordena_posicoes_tabuleiro(tab, tup): #2.2.6
    """
    ordena posicoes tabuleiro: tabuleiro * tuplo → tuplo
    Ordena as posições de um tabuleiro com base na distância de Chebyshev.
    Parâmetros:
    tab (tuple): Tabuleiro representado por uma tuplo de tuplos.
    tup (tuple): Tuplo que contem as posições a serem ordenadas.
    """

    if not (eh_tabuleiro(tab) and type(tup) == tuple):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    for posicao in tup:
        if not (eh_posicao(posicao) and eh_posicao_valida(tab,posicao)):
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    distancias = []
    ordenado = ()
    for pos in tup:
        distancia = chebyshev_distance(tab, pos)
        distancias.append((pos, distancia))
    for i in range(len(distancias)):
        for j in range(len(distancias) - 1):
            if (distancias[j][1] > distancias[j + 1][1] or 
                (distancias[j][1] == distancias[j + 1][1] and distancias[j][0] > distancias[j + 1][0])):
                distancias[j], distancias[j + 1] = distancias[j + 1], distancias[j]
    for pos, _ in distancias:
        ordenado += (pos,)
    return ordenado
    

def marca_posicao(tab,pos,jog): #2.2.7
    """
    marca posicao: tabuleiro * posicao * inteiro → tabuleiro
    Marca uma posição no tabuleiro para um jogador específico.
    Parâmetros:
    tab (tuple): Tabuleiro representado por uma tuplo de tuplos.
    pos (int): Posição a ser marcada no tabuleiro.
    jog (int): Identificador do jogador que fará a marcação.
    """
    lista_tab = []
    res = ()
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos) and eh_posicao_livre(tab,pos) and
             eh_jogadores(jog)):
        raise ValueError('marca_posicao: argumentos invalidos')
    for i in range(len(tab)):
        lista_tab += [list(tab[i])]
    for i in range(len(lista_tab)):
        for j in range(len(lista_tab[0])):
            if (i*len(lista_tab[0])+j+1) == pos:
                if lista_tab[i][j] != 0:
                    raise ValueError('marca_posicao: argumentos invalidos')
                lista_tab[i][j] = jog
    for i in range(len(lista_tab)):
        res += (tuple(lista_tab[i]),)
    return res


def eh_k(k): #para verificar se é um k possivel
    return (k > 0 and type(k) == int)


def verifica_k_linhas(tab,pos,jog,k): #2.2.8
    """
    verifica k linhas: tabuleiro * posicao * inteiro * inteiro → booleano
    Verifica se há k marcas consecutivas de um jogador a partir de uma posição específica.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    pos (int): Posição a ser verificada.
    jog (int): Identificador do jogador.
    k (int): Número de marcas consecutivas a verificar.
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos) and eh_jogadores(jog) and eh_k(k)):
        raise ValueError('verifica_k_linhas: argumentos invalidos')
    if obtem_valor(tab,pos) != jog:
        return False
    k_linhas = (obtem_coluna(tab,pos),obtem_linha(tab,pos),obtem_diagonais(tab,pos)[0],obtem_diagonais(tab,pos)[1])
    #fazer para a coluna, linha, diagonal e antidiagonal respetivamente
    for tuplo in k_linhas:
        indice = tuplo.index(pos)
        #para a frente
        count  = 1
        contar = -1
        for i in range(len(tuplo[indice:])-1):
            contar += 1
            if obtem_valor(tab,tuplo[indice]) == obtem_valor(tab,tuplo[indice + 1 + contar]):
                count += 1
            else:
                break
        if count >= k:
            return True
        #para baixo
        contar = -1
        for i in range(len(tuplo[:indice + 1])-1):
            contar += 1
            if obtem_valor(tab,tuplo[indice]) == obtem_valor(tab,tuplo[indice - 1 - contar]):
                count += 1
            else:
                break
        if count >= k:
            return True
    return False


def eh_fim_jogo(tab, k): #2.3.1
    """
    eh fim jogo: tabuleiro * inteiro → booleano
    Verifica se o jogo terminou, seja por vitória de um jogador ou por empate.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    k (int): Número de marcas consecutivas necessárias para ganhar.
    """
    if not (eh_tabuleiro(tab) and eh_k(k)):
            raise ValueError('eh_fim_jogo: argumentos invalidos')
    if len(obtem_posicoes_livres(tab)) == 0:
        return True
    for jog in (1,-1):
        for pos in obtem_posicoes_jogador(tab,jog):
            if verifica_k_linhas(tab,pos,jog,k):
                return True
    return False


def escolhe_posicao_manual(tab): #2.3.2
    """
    escolhe posicao manual: tabuleiro → posicao
    Solicita ao jogador que escolha uma posição livre no tabuleiro.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    res = ""
    while (not res.isdigit() or not eh_posicao(int(res)) 
           or not eh_posicao_valida(tab, int(res)) or not eh_posicao_livre(tab, int(res))):
        res = input('Turno do jogador. Escolha uma posicao livre: ')
    return int(res)







def escolhe_posicao_auto(tab,jog,k,lvl): #2.3.3
    """
    escolhe posicao auto: tabuleiro * inteiro * inteiro * cad. carateres → posicao
    Escolhe automaticamente uma posição para o jogador no tabuleiro com base no nível de dificuldade.
    Parâmetros:
    tab (tuple): Tabuleiro representado por um tuplo de tuplos.
    jog (int): O jogador atual (1 ou -1).
    k (int): O número de peças em linha necessárias para vencer.
    lvl (str): Nível de dificuldade ('facil', 'normal' ou 'dificil').
    """
    if not (eh_tabuleiro(tab) and len(obtem_posicoes_livres(tab)) != 0 and eh_jogadores(jog) 
            and eh_k(k) and (lvl == 'facil' or lvl == 'normal' or lvl == 'dificil')):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    res = ()
    adj = ()
    if lvl == 'facil':
        if len(obtem_posicoes_jogador(tab,jog)) != 0:
            for tuplo in obtem_posicoes_jogador(tab,jog):
                    res += obtem_posicoes_adjacentes(tab,tuplo)
            for i in range(len(res)):
                if obtem_valor(tab,res[i]) == 0:
                    adj += (res[i],)
            adj = ordena_posicoes_tabuleiro(tab,adj)
            if len(adj) != 0:
                return adj[0]
            else:
                jogada = ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab))
                return jogada[0]
        else:
            jogada = ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab))
            return jogada[0]
    elif lvl == 'normal':
        enemy = -1 if jog == 1 else 1
        for l in range(k,0,-1):
            for pos_jog in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
                new_tab = marca_posicao(tab,pos_jog, jog)
                if verifica_k_linhas(new_tab, pos_jog,jog,l):
                    return pos_jog
            for pos_jog in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
                new_tab2 = marca_posicao(tab,pos_jog, enemy)
                if verifica_k_linhas(new_tab2, pos_jog,enemy,l):
                    return pos_jog
        return (ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)))[0]
    elif lvl == 'dificil':
        game = tab
        j = jog
        vencedores = {1: [], -1: [], 0: []}
        for pos_jog in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
            game = marca_posicao(game, pos_jog, jog)
            posicao = pos_jog
            while not eh_fim_jogo(game, k):
                j = -1 if j == 1 else 1
                posicao = escolhe_posicao_auto(game, j, k, 'normal')
                game = marca_posicao(game, posicao, j)
            # calcular vencedor 
            if verifica_k_linhas(game, posicao, j, k): 
                vencedores[j].append(pos_jog)
            elif verifica_k_linhas(game,posicao,-j,k):
                vencedores[0].append(pos_jog) 
            else:
                vencedores[-j].append(pos_jog)
            game = tab

        if len(vencedores[jog]) > 0:
            return ordena_posicoes_tabuleiro(tab,tuple(vencedores[jog]))[0]
        elif len(vencedores[0]) > 0:
            return ordena_posicoes_tabuleiro(tab,tuple(vencedores[0]))[0]
        else:
            return ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab))[0]
                


                    


def jogo_mnk(cfg,jog,lvl):
    """
    jogo mnk: tuplo * inteiro * cad. carateres → inteiro
    Inicia o jogo MNK com as configurações fornecidas, permitindo que dois jogadores (humano e computador) joguem.
    Parâmetros:
    cfg (tuple): Um tuplo contendo três inteiros, representando o número de linhas (m), colunas (n) e peças
    em linha necessárias para vencer (k).
    jog (int): O jogador atual (1 para 'X' e -1 para 'O').
    lvl (str): Nível de dificuldade do computador ('facil', 'normal' ou 'dificil').
    """
    if not (type(cfg) == tuple and len(cfg) == 3 and eh_jogadores(jog) and (lvl == 'facil' or
            lvl == 'normal' or lvl == 'dificil')):
        raise ValueError('jogo_mnk: argumentos invalidos')
    
    m,n,k = cfg[0],cfg[1],cfg[2]
    tab_game = ((0,)*n,)*m
    tab_mostra = tabuleiro_para_str(tab_game)
    print('Bem-vindo ao JOGO MNK.')
    
    if jog == 1:
        print("O jogador joga com 'X'.")
        print(tab_mostra)
        while not eh_fim_jogo(tab_game,k):
            posicao = escolhe_posicao_manual(tab_game)
            tab_game = marca_posicao(tab_game,posicao,1)
            print(tabuleiro_para_str(tab_game))
            if verifica_k_linhas(tab_game,posicao,jog,k):
                print('VITORIA')
                return 1
            if eh_fim_jogo(tab_game,k):
                print('EMPATE')
                return 0
            print(f'Turno do computador ({lvl}):')
            posicao = escolhe_posicao_auto(tab_game,-jog,k,lvl)
            tab_game = marca_posicao(tab_game,posicao,-1)
            print(tabuleiro_para_str(tab_game))
            if verifica_k_linhas(tab_game,posicao,-jog,k):
                print('DERROTA')
                return -1
            if eh_fim_jogo(tab_game,k):
                print('EMPATE')
                return 0
    
    if jog == -1:
        bot = 1
        print("O jogador joga com 'O'.")
        print(tab_mostra)
        while not eh_fim_jogo(tab_game,k):
            print(f'Turno do computador ({lvl}):')
            posicao = escolhe_posicao_auto(tab_game,bot,k,lvl)
            tab_game = marca_posicao(tab_game,posicao,bot)
            print(tabuleiro_para_str(tab_game))
            if verifica_k_linhas(tab_game,posicao,jog,k):
                print('DERROTA')
                return -jog
            if eh_fim_jogo(tab_game,k):
                print('EMPATE')
                return 0
            posicao = escolhe_posicao_manual(tab_game)
            tab_game = marca_posicao(tab_game,posicao,-1)
            print(tabuleiro_para_str(tab_game))
            if verifica_k_linhas(tab_game,posicao,-jog,k):
                print('VITORIA')
                return jog
            if eh_fim_jogo(tab_game,k):
                print('EMPATE')
                return 0