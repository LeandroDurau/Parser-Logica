'''Leandro Ceron Durau

#Todas as operações tem que ser separados por um espaço#

Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional 
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma 
da expressão (sintaxe).  
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando, 
com a seguinte formatação:  
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões 
lógicas estão no arquivo.  
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.  
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída 
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais. 
Gramática:  
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.  
Constante="T"|"F". 
Proposicao=[a−z0−9]+ 
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen 
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen 
AbreParen="(" 
FechaParen=")" 
OperatorUnario="¬" 
OperatorBinario="∨"|"∧"|"→"|"↔" 
 
Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, 
conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações. 
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em 
qualquer expressão de entrada. 
Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arquivos  contendo 
números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arquivo  de  testes  extra 
para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu 
programa carregando o arquivo de testes. 


'''


def Formula(texto,indice,n_parenteses):
  t = texto
  if(texto[indice]==''):
    return False
  if((Constante(texto,indice) or Proposicao(texto,indice))and t[indice+1]=='' and indice==0):
    return True
    
  if((Constante(texto,indice) or Proposicao(texto,indice)) and n_parenteses > 0):
    if(Constante(texto,indice-1) or Proposicao(texto,indice-1)):
      return False
    if(t[indice-1]=='('):
      return False
    return Formula(texto,indice+1,n_parenteses)

  if(FormulaUnaria(texto,indice)):
    if(n_parenteses==0):
      return False
    if(t[indice+1]=='('):
      return Formula(texto,indice+1,n_parenteses)
    if(Constante(texto,indice+1) or Proposicao(texto,indice+1)):
      return Formula(texto,indice+2,n_parenteses)
  if(FormulaBinaria(texto,indice)):
    if(t[indice+1]=='('):
      return Formula(texto,indice+1,n_parenteses)
    if(t[indice+2]=='('):
      return Formula(texto,indice+2,n_parenteses)
    if((Constante(texto,indice+1) or Proposicao(texto,indice+1))and (Constante(texto,indice+2) or Proposicao(texto,indice+2))):
      return Formula(texto,indice+3,n_parenteses)

  if(t[indice]=='(' and t[indice+1]!=')'):
    return Formula(texto,indice+1,n_parenteses+1)

  if(t[indice]==')'):
    if(t[indice+1]=='' and n_parenteses==1):
      return True
    return Formula(texto,indice+1,n_parenteses-1)

  return False
    
def Constante(texto,indice):
  if(texto[indice]=="T" or texto[indice]=="F"):
    return True
  return False

def FormulaUnaria(texto,indice):
  if(texto[indice]=='\\neg'):
    return True
  return False
  

def FormulaBinaria(texto,indice):
  if(texto[indice]=='\\vee' or texto[indice]=='\\wedge' or texto[indice]=='\\rightarrow' or texto[indice]=='\\leftrightarrow'):
    return True
  return False
  
def Proposicao(texto,indice):
  if all(x.isdigit() or x.islower() for x in texto[indice]):
    return True
  return False


def LeitordeTXT(file):
    n_strings = int(file.readline())
    for x in range(n_strings):
      text = file.readline().split()
      text.append('')
      if (Formula(text,0,0)):
        for y in text:
          print(y, end=" ")
        print(": Pertence.")
        continue
      for y in text:
          print(y, end=" ")
      print(": Não Pertence.")


r1 = open("1.txt","r")
r2 = open("2.txt","r")
print("-=-=-=-=-=-=-=-1.txt-=-=-=-=-=-=-=--=-")
LeitordeTXT(r1)
print("-=-=-=-=-=-=-=-2.txt-=-=-=-=-=-=-=--=-")
LeitordeTXT(r2)