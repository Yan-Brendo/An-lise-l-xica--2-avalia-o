# Verificador de Índices de Dataset do Pandas

Este projeto em Python utiliza expressões regulares para validar se uma cadeia de texto é um índice de dataset válido no Pandas. O código foi desenvolvido como resposta à questão proposta, onde é fornecida uma expressão regular para reconhecer diferentes tipos de índices em datasets.

## Estrutura do Projeto

O código inclui uma função principal chamada `regexCheck()`, que:
1. Solicita ao usuário uma entrada para teste de índice.
2. Usa a expressão regular para verificar se o formato do índice é válido.
3. Retorna um feedback indicando se o índice é válido ou não.

## Pré-requisitos

- Python 3.x

## Como Executar

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `regex.py` está salvo.
3. Execute o comando abaixo:
   
   python regex.py

4. Insira um índice no formato suportado e pressione Enter.
5. O resultado indicará se o índice fornecido é válido.

## Sobre a Expressão Regular

A expressão regular usada para a validação é:

(?:(?:\-[1-9]\d*|\d+)(\:\-[1-9]\d*|\:\d+)?|(?:\'[a-zA-Z ]+\')(\:\'[a-zA-Z ]+\')?|(?:\"[a-zA-Z ]+\")(\:\"[a-zA-Z ]+\")?)

## Explicação dos Padrões Reconhecidos

1. Índices numéricos: Números inteiros (positivos ou negativos).
2. Nomes de colunas: Entre aspas simples ou duplas, com letras e espaços.
3. Intervalos (slices): Intervalos definidos por números ou nomes de colunas.

## Exemplos de Entradas Válidas

1 (índice numérico positivo)
-3 (índice numérico negativo)
"Nome da Coluna"
'Coluna1'
0:5 (intervalo numérico)
'Coluna A':'Coluna B'

## Observações

Este código foi projetado apenas para validar strings que representam índices. Ele não interage diretamente com datasets do Pandas.

## Licença

Este projeto é licenciado sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.



