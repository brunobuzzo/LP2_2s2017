
aluno ={}

nome = 'nome'

while len(nome) > 0:
    nome = input("Infome o nome do aluno: ")
    aluno["nome"] = 0
    if len(nome) == 0:
        del aluno['nome']
        break
    else:
        n1 = float(input("Informe a primeira nota: "))
        n2 = float(input("Informe a segunda nota: "))
        media = (n1+n2)/2
        aluno[nome] = media


