# Nome: Luca Takemura Piccoli Usuario: MrJubiscreldo
# Grupo: RA1 15 RA1

import sys

# Analisa uma linha de expressão para gerar uma lista de tokens.
def parseExpressao (linha, _tokens_):
  index = 0
  lenlinha = len(linha)
  while index < lenlinha:
    # Se retornar index -1 um erro foi detectado
    if index == -1:
      estadoErro(linha)
      return None
    else:
      letra = linha[index]
    # Classifica e processa o tipo de token
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
    elif letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # Variáveis ou 'RES'
      token, index = estadoEspecial(linha, index)
      _tokens_.append(token)
    elif letra == '\n':
      break
    else:
      estadoErro(linha)
      return None # Caractere inválido

  return _tokens_

# Extrai um número (inteiro ou real) da expressão.
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

# Extrai um operador da expressão.
def estadoOperador(linha, index):
  operador = linha[index]
  if operador == '/' and linha[index + 1] == '/': # Divisão inteira
    return 'o//', index + 2
  return "o" + operador, index+1

# Extrai um parêntese da expressão.
def estadoParenteses(linha, index):
  return linha[index], index+1


def estadoEspecial(linha, index):
  especial = linha[index]
  index += 1

  if especial == 'R' and linha[index] == 'E' and linha[index + 1] == 'S': # Token 'RES'
    return 'r', index + 2
  while index < len(linha):
    letra = linha[index]
    if letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      especial += letra
      index += 1
    else:
      return "m" + especial, index

# Imprime mensagem de erro.
def estadoErro(linha):
  print(f'Erro! expressao: {linha}')

# Resolve uma operação
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
    return float(n1) % float(n2)
  elif operador == "^":
    return float(n1) ** int(float(n2))
  else:
    return float(n1) // float(n2)

# Executar uma linha de tokens
def executarExpressao(tokens, memoria, resultados):
  pilha = []

  for i, token in enumerate(tokens):
    if token in "()":
      continue
    elif token[0] == "n": # Empilha número
      pilha.append(token[1:])
    elif token[0] == "o": # Operador: desempilha 2, calcula, empilha resultado
      if len(pilha) < 2:
        print(f"Erro: Falta tokens para operador. Token: {token}")
        return None
      n2 = pilha.pop()
      n1 = pilha.pop()
      pilha.append(resolver(n1, n2, token[1:]))
    elif token[0] == "m": # Variável (MEM): leitura ou escrita
      if len(pilha) < 1 or tokens[i+1][0] == "o":
        # Pegar valor da memoria
        mem = memoria.get(token[1:])
        if mem == None:
          mem = 0.0
        pilha.append(mem)
      else:
        # Armazenar valor na memoria
        memoria[token[1:]] = pilha[-1]
    elif token[0] == "r": # 'RES': referência a resultado anterior
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

# Executa uma lista de expressões, gerenciando memória e resultados.
def executarExpressoes(tokens_list):
  memoria = {}
  resultados = []
  for tokens in tokens_list:
    resultados.append(executarExpressao(tokens, memoria, resultados))
    if resultados[-1] == None:
      print(f"Erro: {tokens}")
      return None
  return resultados

# Gera código Assembly ARM para uma lista de expressões.
def gerarAssembly(tokens_list, codigoAssembly):
  len_pilha = 0
  len_numeros = 0
  len_potencias = 0
  memoria = set()

  codigo = ".global _start\n _start:\n" # Início do código
  data = ".data\n    const_um: .double 1.0\n" # Seção de dados
  resultados = "" # Seção de resultados em .data

  for i, tokens in enumerate(tokens_list):
    for j, token in enumerate(tokens):
      if token in "()":
        continue
      elif token[0] == "n":: # Número: declara e empilha
        data += f"    n{len_numeros}: .double {token[1:]}\n"
        codigo += f"    ldr r0, =n{len_numeros}\n"
        codigo += f"    vldr.f64 d0, [r0]\n"
        codigo += f"    vpush.f64 {{d0}}\n"

        len_numeros += 1
        len_pilha += 1
      elif token[0] == "o": # Operador: desempilha 2, opera, empilha 1
        if len_pilha < 2:
          print("Erro: Falta tokens para operador")
          return None
        operador = token[1:]
        codigo += "    vpop.f64 {d1}\n"
        codigo += "    vpop.f64 {d0}\n"
        
        if operador == '+':
          codigo += "    vadd.f64 d2, d0, d1\n"
        elif operador == '-':
          codigo += "    vsub.f64 d2, d0, d1\n"
        elif operador == '*':
          codigo += "    vmul.f64 d2, d0, d1\n"
        elif operador == '/':
          codigo += "    vdiv.f64 d2, d0, d1\n"
        elif operador == '%':
          codigo += "    vdiv.f64 d2, d0, d1\n"
          codigo += "    vcvt.s32.f64 s4, d2\n"
          codigo += "    vcvt.f64.s32 d2, s4\n"
          codigo += "    vmul.f64 d2, d2, d1\n"
          codigo += "    vsub.f64 d2, d0, d2\n"
        elif operador == '^': # Potência com loop
          codigo += "    vcvt.s32.f64 s2, d1\n"
          codigo += "    vmov r2, s2\n"
          codigo += "    ldr r0, =const_um\n"
          codigo += "    vldr.f64 d2, [r0]\n"
          codigo += "    cmp r2, #0\n"
          codigo += f"    beq .fim_pot{len_potencias}\n"
          codigo += f".pot{len_potencias}:\n"
          codigo += "    cmp r2, #0\n"
          codigo += f"    ble .fim_pot{len_potencias}\n"
          codigo += "    vmul.f64 d2, d2, d0\n"
          codigo += "    sub r2, r2, #1\n"
          codigo += f"    b .pot{len_potencias}\n"
          codigo += f".fim_pot{len_potencias}:\n"
          len_potencias += 1
        elif operador == '//':
          codigo += "    vdiv.f64 d2, d0, d1\n"
          codigo += "    vcvt.s32.f64 s4, d2\n"
          codigo += "    vcvt.f64.s32 d2, s4\n"
        else:
          print("Erro: Operador invalido")
          return None
        
        codigo += "    vpush.f64 {d2}\n"
        len_pilha -= 1
      elif token[0] == "m": # Variável: leitura ou escrita em memória
        mem = token[1:]

        if len_pilha < 1 or tokens[j+1][0] == "o":
          codigo += f"    ldr r0, ={mem}\n"
          codigo += "    vldr.f64 d0, [r0]\n"
          codigo += "    vpush.f64 {d0}\n"
          len_pilha += 1
        else:
          if mem not in memoria:
            memoria.add(mem)
            data += f"    {mem}: .double 0.0\n"
          codigo += "    vpop.f64 {d0}\n"
          codigo += f"    ldr r0, ={mem}\n"
          codigo += "    vstr.f64 d0, [r0]\n"
          codigo += "    vpush.f64 {d0}\n"
      elif token[0] == "r": # 'RES': carrega resultado anterior
        if len_pilha < 1:
          print("Erro: Falta tokens para RES")
          return None
        else:
          codigo += "    vpop.f64 {d0}\n"
          codigo += "    vcvt.s32.f64 s0, d0\n"
          codigo += "    vmov r1, s0\n"
          codigo += "    ldr r0, =r_0\n"
          codigo += "    lsl r1, r1, #3\n"
          codigo += "    add r0, r0, r1\n"
          codigo += "    vldr.f64 d0, [r0]\n"
          codigo += "    vpush.f64 {d0}\n"
          
      else:
        print("Erro: Token invalido")
        return None
    # Armazena o resultado da expressão atual
    if len_pilha == 1:
      resultados += f"    r_{i}: .double 0.0\n"
      codigo += "    vpop.f64 {d0}\n"
      codigo += f"    ldr r0, =r_{i}\n"
      codigo += "    vstr.f64 d0, [r0]\n"
      len_pilha -= 1
    else:
      print(f"Erro: Expressao invalida, tokens restantes: {len_pilha}")
      return None  
  
  codigoAssembly = codigo + data + resultados # Combina seções
  return codigoAssembly
     
# Função de teste para o Analisador Léxico (AFD) e Execução de Expressões.
def testarAFD():
  expressoes =  ["((2 Y 3 +) (2 1 +)+)",
                 "(((2 3 +) Y +) (2 1 +)+)",
                 "(Y (2 1 +)+)",
                 "(3.14 2.0 +)",
                 "(3 RES)",]
  tokens_list = []
  for linha in expressoes:
    tokens_list.append(parseExpressao(linha, []))
  resultados = executarExpressoes(tokens_list)
  if resultados == None:
    print("Erro ao executar expressoes")
  elif resultados != [8.0, 10.0, 5.0, 5.140000000000001, 5.140000000000001]:
    print("Erro no resultado das expressoes")
  else:
    print("Expressoes executadas corretamente com sucesso")

# Função de teste para a geração de código Assembly.
def testarAssembly():
  expressoes =  ["(3.14 2.0 +)",
                "((1.5 2.0 *) (3.0 4.0 *) /)",
                "(5.0 MEM)",
                "(2 RES)"]
  tokens_list = []
  for linha in expressoes:
    tokens_list.append(parseExpressao(linha, []))
  codigoAssembly = gerarAssembly(tokens_list, "")
  if codigoAssembly == None:
    print("Erro ao gerar codigo assembly")
  elif codigoAssembly != ".global _start\n _start:\n    ldr r0, =n0\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    ldr r0, =n1\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d1}\n    vpop.f64 {d0}\n    vadd.f64 d2, d0, d1\n    vpush.f64 {d2}\n    vpop.f64 {d0}\n    ldr r0, =r_0\n    vstr.f64 d0, [r0]\n    ldr r0, =n2\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    ldr r0, =n3\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d1}\n    vpop.f64 {d0}\n    vmul.f64 d2, d0, d1\n    vpush.f64 {d2}\n    ldr r0, =n4\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    ldr r0, =n5\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d1}\n    vpop.f64 {d0}\n    vmul.f64 d2, d0, d1\n    vpush.f64 {d2}\n    vpop.f64 {d1}\n    vpop.f64 {d0}\n    vdiv.f64 d2, d0, d1\n    vpush.f64 {d2}\n    vpop.f64 {d0}\n    ldr r0, =r_1\n    vstr.f64 d0, [r0]\n    ldr r0, =n6\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d0}\n    ldr r0, =MEM\n    vstr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d0}\n    ldr r0, =r_2\n    vstr.f64 d0, [r0]\n    ldr r0, =n7\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d0}\n    vcvt.s32.f64 s0, d0\n    vmov r1, s0\n    ldr r0, =r_0\n    lsl r1, r1, #3\n    add r0, r0, r1\n    vldr.f64 d0, [r0]\n    vpush.f64 {d0}\n    vpop.f64 {d0}\n    ldr r0, =r_3\n    vstr.f64 d0, [r0]\n.data\n    n0: .double 3.14\n    n1: .double 2.0\n    n2: .double 1.5\n    n3: .double 2.0\n    n4: .double 3.0\n    n5: .double 4.0\n    n6: .double 5.0\n    MEM: .double 0.0\n    n7: .double 2\n    r_0: .double 0.0\n    r_1: .double 0.0\n    r_2: .double 0.0\n    r_3: .double 0.0\n":
    print("Erro no codigo assembly")
  else:
    print("Codigo assembly gerado sem erros com sucesso")

# Salva tokens em um arquivo.
def saveTokens(tokens_list, nomeArquivo):
  with open(nomeArquivo, 'w') as arquivo:
    for tokens in tokens_list:
      arquivo.write(';'.join(tokens) + '\n')

# Salva o código assembly em um arquivo.
def saveAssembly(codigoAssembly, nomeArquivo):
  with open(nomeArquivo, 'w') as arquivo:
    arquivo.write(codigoAssembly)

# Lê linhas de um arquivo.
def lerArquivo(nomeArquivo, linhas):
  try:
    with open(nomeArquivo, 'r') as arquivo:
      for linha in arquivo:
        linhas.append(linha)
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nomeArquivo}' não encontrado.")
  except Exception as e:
    print(f"Erro de leitura: {e}")

# Exibe os resultados formatados.
def exibirResultados(resultados):
  print("Resultados:")
  if resultados == None:
    print("Erro ao executar expressoes")
  else: 
    for i, resultado in enumerate(resultados):
      resultado = float(resultado)
      print(f"Resultado {i+1}: {resultado:.2f}")
    
# Bloco de execução principal.
if __name__ == '__main__':
  nomeArquivo = sys.argv[1]

  arquivoTokens = "tokens.txt"
  arquivoAssembly = "assembly.s"

  tokens_list = []
  linhas = []

  lerArquivo(nomeArquivo, linhas)

  for linha in linhas:
    tokens_list.append(parseExpressao(linha, []))

  saveTokens(tokens_list, arquivoTokens)
  resultados = executarExpressoes(tokens_list)
  exibirResultados(resultados)

  codigoAssembly = gerarAssembly(tokens_list, "")
  saveAssembly(codigoAssembly, arquivoAssembly)
