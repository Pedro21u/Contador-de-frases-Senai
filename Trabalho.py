#Começo do programa
print("Seja bem-vindo ao Contador de Palavras!")
frase = str(input("Digite uma frase: "))

#Função que faz a divisão das palavras e conta elas
def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)
#Função que detecta qual a palavra mais longa
def palavra_longa(frase):
    palavras = frase.split()
    palavra_longa = palavras[0]

    for palavra in palavras:
        if len(palavra) > len(palavra_longa):
            palavra_longa = palavra
        
    return palavra_longa
#Função que procura uma palavra desejada dentro da frase
def procurar_palavra(frase, procurar):
    palavras = frase.split()

    if procurar in palavras:
        return True
    else:
        return False

#Declaracao das funções em variaveis
plv_numero = contar_palavras(frase)
plv_longa = palavra_longa(frase)
frase_selecao = ("\n1 - Para procurar uma palavra na frase \n2 - Para escrever outra frase \n0 - Para sair \nDigite uma opção desejada: ")

#Parte do programa que mostra o numero de palavras e a mais longa
print(f"\nNúmero de palavras na frase é de: {plv_numero}")
print(f"A palavra mais longa da frase é: {plv_longa}")

#Parte do programa que apresenta as opções para serem selecionadas
opcao = int(input(f"{frase_selecao}"))
while opcao != 0:
#Opção 1, verifica se a palavra contém na frase e apresenta resultado de sim ou não
    if opcao == 1:
        procurar = str(input("\nDigite a palavra para ser pesquisada dentro da frase: "))
        if procurar_palavra(frase, procurar):
            print(f"A palavra {procurar}, foi encontrada na frase!")
        else:
            print(f"A palavra {procurar}, não foi encontrada na frase!")

        opcao = int(input(f"{frase_selecao}"))
#Opção 2, dá a opção de nova frase, e declara novamente as variaveis
    if opcao == 2:
        frase = str(input("\nDigite uma nova frase: "))
        plv_numero = contar_palavras(frase)
        plv_longa = palavra_longa(frase)
        print(f"\nNúmero de palavras na frase é de: {plv_numero}")
        print(f"A palavra mais longa da frase é: {plv_longa}")
        opcao = int(input(f"{frase_selecao}"))
print("\nPrograma finalizado com sucesso!\n")