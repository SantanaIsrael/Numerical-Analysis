from sympy import *

#Método para ler as entradas da Regressão Linear
def LerArquivoRerLinear():
  x = []
  y = []

  with open("EntradasTeste/entrada_Regressao.txt", "r", encoding="utf-8") as arquivo:
    x = list(map(float, arquivo.readline().strip().split()))
    y = list(map(float, arquivo.readline().strip().split()))
	
  arquivo.close()
  return x, y
#Método para ler as entradas do Lagrange
def lerArquivoLagrange():
	arquivo = open('EntradasTeste/entrada_Lagrange.txt', "r")
	fx = []
	pontos = []

	aux = arquivo.readline()
	while(aux != '\n'):
		aux = aux.strip()  # remove espaços em branco no início e no fim
		if aux:  # verifica se a string não está vazia
			aux = float(aux)
			fx.append(aux)
		aux = arquivo.readline()
  
	aux = arquivo.readline()
	
	while(aux != '' and aux != '\n'):
		aux = aux.strip()  # remove espaços em branco no início e no fim
		if aux:  # verifica se a string não está vazia
			aux = float(aux)
			pontos.append(aux)
		aux = arquivo.readline()
	arquivo.close()
	return fx, pontos  # retorna os valores diretamente
#Método para ler as entradas do Newton
def lerArquivoNewton():
	fx = {}
	pontos = []
	arquivo = open('EntradasTeste/entrada_Newton.txt', "r")

	aux = arquivo.readline()
	while(aux != '\n'):
		aux = aux.strip()  # remove espaços em branco no início e no fim
		if aux:  # verifica se a string não está vazia
			aux = float(aux)
			pontos.append(aux)
		aux = arquivo.readline()
  
	aux = arquivo.readline()
 
	i = 0
 
	while(aux != '' and aux != '\n'):
		aux = aux.strip()  # remove espaços em branco no início e no fim
		if aux:  # verifica se a string não está vazia		
			aux = float(aux)
			fx[pontos[i]] = aux		
		aux = arquivo.readline()
		i += 1
	arquivo.close()
	return fx, pontos
#Método para ler as entradas de quadratura de Gauss
def lerArquivo(nome):
	x = symbols('x')
	with open('EntradasTeste/entrada_'+nome+'.txt', "r") as arquivo:
		funcao = eval(arquivo.readline())
		a = float(arquivo.readline())
		b = float(arquivo.readline())
		linha = arquivo.readline()
		
		if linha.strip():
			sub = int(linha)
			arquivo.close()
			return funcao, a, b, sub
		funcao = sympify(funcao)
		arquivo.close()
	return funcao, a, b

def lerArquivoDeri():
    
	with open('EntradasTeste/entrada_Derivadas.txt', "r") as arquivo:
		funcao = arquivo.readline()
		x = float(arquivo.readline())
		arquivo.close()
	return funcao, x

def lerArquivoRichards():
	arquivo = open('EntradasTeste/entrada_Richards.txt', "r")
	vetor_um = []
	vetor_dois = []

	aux = arquivo.readline()
	while(aux != '\n'):
		aux = aux.strip()  # remove espaços em branco no início e no fim
		if aux:  # verifica se a string não está vazia
			aux = float(aux)
			vetor_um.append(aux)
		aux = arquivo.readline()
  
	aux = arquivo.readline()
	
	while(aux != '' and aux != '\n'):
		aux = aux.strip()  # remove espaços em branco no início e no fim
		if aux:  # verifica se a string não está vazia
			aux = float(aux)
			vetor_dois.append(aux)
		aux = arquivo.readline()
	arquivo.close()
	
	return vetor_um, vetor_dois  # retorna os valores diretamente