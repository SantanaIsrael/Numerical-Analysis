def salvar_resultado(a1, a0, r):
  with open("resultado.txt", "w", encoding="utf-8") as arquivo:
      arquivo.write("Resultado Regressão\n")
      arquivo.write(f"y =~ {a0} + {a1}x\n")
      arquivo.write(f"r: {r}")
      arquivo.close()

def salvar_Lagrange(result):
   with open("resultado.txt", "a") as arquivo:
        arquivo.write("\n\nResultado Lagrange\n")
        arquivo.write("P(x) = " + result)
        arquivo.close()


def salvar_Newton(result):
   with open("resultado.txt", "a") as arquivo:
        arquivo.write("\n\nResultado Newton\n")
        arquivo.write("P(x) = " + result)
        arquivo.close()

def salvar(result, nome):
   with open("resultado.txt", "a") as arquivo:
        arquivo.write("\n\nResultado "+ nome +"\n")
        arquivo.write("I(f(x)) ~= " + result)
        arquivo.close()

def salvar_Richards(result, num_extrapolacao):
   with open("resultado.txt", "a") as arquivo:
        arquivo.write("\n\nResultado richards\n")
        arquivo.write("Valor extrapolado de y para x = " + num_extrapolacao +": " + result)
        arquivo.close()