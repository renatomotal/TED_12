import csv

pub_maior = None
ano_maior = None

with open('filmes.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
        valor = float(linha[8])
        if pub_maior is None or valor > pub_maior:
            pub_maior = valor
            ano_maior = linha[1]

print("O maior público foi:", pub_maior)
print("No ano de:", ano_maior)
