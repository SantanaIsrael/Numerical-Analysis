from math import *

def setFuncao(f):
  global funcao
  funcao = f

def func(x):

  return eval(funcao)

def derivadaPrimeira(x):

  return str((func(x + 1) - func(x - 1)) / ((x+1)-(x-1)))

def derivadaSegunda(x):

  return str((func(x + 1) - func(x)) - (func(x) - func(x - 1)))