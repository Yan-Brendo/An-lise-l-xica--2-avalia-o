import re
import os
import sys

#O código proposto busca testar um regex válido para um índice de dataset Pandas
#O dataset visa acessar as colunas de uma certa tabela - nome_da_variavel [ índice(s) ]

#O qual o índice deve seguir os seguintes formatos:
# - O número da coluna, que é um número inteiro, positivo, negativo ou zero;
# - O nome da coluna entre aspas, simples ou duplas. Considere que os nomes das colunas são formados por letras maiúsculas, minúsculas ou espaços em branco;
# - Um intervalo (slice) formado por dois números positivos (ou zero) ou dois números negativos, separados por “:”;
# - Um intervalo (slice) formado por dois nomes de colunas entre aspas, simples ou duplas.

#O código visa somente inserir variados inputs para testar a validade do RegEx proposto

def regexCheck():
    print('Você deve inserir um teste de validade de índice num dataset Panda no formato x[indice]')
    indice = input('Aguardando o input: ')
    
    pattern = r"^(?:(?:\-[1-9]\d*|\d+)(\:\-[1-9]\d*|\:\d+)?|(?:\'[a-zA-z ]+\')(\:\'[a-zA-z ]+\')?|(?:\"[a-zA-Z ]+\")(\:\"[a-zA-Z ]+\")?)$"
    
    regex = re.compile(pattern)
    validade = regex.match(indice)
    
    os.system('cls')
    
    if validade:
        print(f"O dataset x[{indice}], é um dataset válido para Pandas")
    else:
        print('O dataset não é válido')

def waitResponse():
    response = input('Escolha uma opção: ')
    match response:
        case '0':
            os.system('cls')
            regexCheck()
        case '1':
            os.system('cls')
            print('Saindo...')
            sys.exit()
        case _:
            os.system('cls')
            print('Escolha uma opção válida')

def chooseOption():
    print('Regex Checker')
    print('[0] Inserir Índice')
    print('[1] Sair')
    waitResponse()

def main():
    while True:
        chooseOption()

main()
