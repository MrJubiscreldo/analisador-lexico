# Nome: Luca Takemura Piccoli Usuario: MrJubiscreldo
# Grupo: RA1 15 RA1

def parseExpressao (linha, _tokens_):
  index = 0
  lenlinha = len(linha)
  while index < lenlinha:
    # Se retornar index -1 algum erro foi detectado
    if index == -1:
      estadoErro(linha)
      return None
    else:
      letra = linha[index]

    if letra == ' ':
      index += 1
    elif letra in '()':
      token, index = estadoParenteses(linha, index)
      _tokens_.append(token)
    elif letra in '1234567890':
      token, index = estadoNumero(linha, index)
      _tokens_.append(token)
    elif letra in '+-*/%^':
      token, index = estadoOperador(linha, index)
      _tokens_.append(token)
    elif letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      token, index = estadoEspecial(linha, index)
      _tokens_.append(token)
    elif letra == '\n':
      break
    else:
      estadoErro(linha)
      return None

  return _tokens_

def estadoNumero(linha, index):
  numero = linha[index]
  index += 1
  isreal = False
  while index < len(linha):
    letra = linha[index]
    if letra in '1234567890':
      numero += letra
      index += 1
    elif letra == '.':
      if not isreal:
        isreal = True
        numero += letra
        index += 1
      else:
        #Mais de um ponto dectectado
        return "n" + numero, -1
    else:
      return "n" + numero, index

  return "n" + numero, index

def estadoOperador(linha, index):
  operador = linha[index]
  if operador == '/' and linha[index + 1] == '/':
    return 'o//', index + 2
  return "o" + operador, index+1

def estadoParenteses(linha, index):
  return linha[index], index+1


def estadoEspecial(linha, index):
  especial = linha[index]
  index += 1

  if especial == 'R' and linha[index] == 'E' and linha[index + 1] == 'S':
    return 'r', index + 2
  while index < len(linha):
    letra = linha[index]
    if letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      especial += letra
      index += 1
    else:
      return "m" + especial, index

def estadoErro(linha):
  print(f'Erro! expressao: {linha}')

#Testar analisador lexico
# def testarAL(tokens_list):
#   for tokens in tokens_list:
#     for token in tokens:
      # todo: checar se token eh valido

def resolver(n1, n2, operador):
  if operador == "+":
    return float(n1) + float(n2)
  elif operador == "-":
    return float(n1) - float(n2)
  elif operador == "*":
    return float(n1) * float(n2)
  elif operador == "/":
    return float(n1) / float(n2)
  elif operador == "%":
    return int(n1) % int(n2)
  elif operador == "^":
    return float(n1) ** float(n2)
  else:
    return int(n1) // int(n2)

# Executar uma linha de tokens
def executarExpressao(tokens, memoria, resultados):
  pilha = []

  for i, token in enumerate(tokens):
    if token in "()":
      continue
    elif token[0] == "n":
      pilha.append(token[1:])
    elif token[0] == "o":
      if len(pilha) < 2:
        print("Erro: Falta tokens para operador")
        return None
      n1 = pilha.pop()
      n2 = pilha.pop()
      pilha.append(resolver(n1, n2, token[1:]))
    elif token[0] == "m":
      if len(pilha) < 1 or tokens[i+1][0] == "o":
        # Pegar valor da memoria
        mem = memoria.get(token[1:])
        if mem == None:
          mem = 0.0
        pilha.append(mem)
      else:
        # Armazenar valor na memoria
        memoria[token[1:]] = pilha[-1]
    elif token[0] == "r":
      if len(pilha) < 1:
        print("Erro: Falta tokens para RES")
        return None
      else:
        # Pegar valor de resultados
        res = int(pilha.pop())
        if res < 1 or res >= len(resultados):
          print("Erro: Resultado fora dos limites")
          return None
        else:
          pilha.append(resultados[res]) 
    else:
      print("Erro: Token invalido")
      return None
  # Retorna o resultado
  if len(pilha) == 1:
    return pilha.pop()   
  else:
    print(f"Erro: Expressao invalida, tokens restantes: {len(pilha)}")
    return None


def executarExpressoes(tokens_list):
  memoria = {}
  resultados = []
  for tokens in tokens_list:
    resultados.append(executarExpressao(tokens, memoria, resultados))
  return resultados


def testarAFD():
  expressoes =  ["((2 Y 3 +) (2 1 +)+)",
                 "(((2 3 +) Y +) (2 1 +)+)",
                 "(Y (2 1 +)+)",
                 "(3.14 2.0 +)",
                 "3 RES",]
  tokens_list = []
  for linha in expressoes:
    tokens_list.append(parseExpressao(linha, []))
  return executarExpressoes(tokens_list)

print(testarAFD())



# expressoestxt = 'teste1.txt'

# with open(expressoestxt, 'r') as expressoes:
#   tokens_list = []
#   for linha in expressoes:
#     tokens_list.append(parseExpressao(linha, []))

#   print(tokens_list)
