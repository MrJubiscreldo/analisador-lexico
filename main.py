# Nome: Luca Takemura Piccoli Usuario:
# Grupo: RA1 15 RA1

def parseExpressao (linha, _tokens_):
  index = 0
  lenlinha = len(linha)
  while index < lenlinha:
    if index == -1:
      estadoErro()
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
    elif letra in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
      token, index = estadoEspecial(linha, index)
      _tokens_.append(token)
    elif letra == '\n':
      break
    else:
      estadoErro()
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
        return numero, -1
    else:
      return numero, index

  return numero, index

def estadoOperador(linha, index):
  operador = linha[index]
  if operador == '/' and linha[index + 1] == '/':
    return operador + '/', index + 2
  return operador, index+1

def estadoParenteses(linha, index):
  return linha[index], index+1
  

def estadoEspecial(linha, index):
  especial = linha[index]
  index += 1

  if especial == 'R' and linha[index] == 'E' and linha[index + 1] == 'S':
    return 'RES', index + 2
  while index < len(linha):
    letra = linha[index]
    if letra in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
      especial += letra
      index += 1
    else:
      return especial, index

def estadoErro():
  print(f'Erro! expressao: {linha}')

expressoestxt = 'teste1.txt'

with open(expressoestxt, 'r') as expressoes:
  tokens = []
  for linha in expressoes:
    tokens.append(parseExpressao(linha, []))

  print(tokens)

