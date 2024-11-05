print("SISTEMA GERENCIADOR DE TAREFAS")
tarefas = []

#Equipe do Projeto
#Função 1: José Lucas Pereira de Andrade
#Função 2: Mickaio Gabriel Francisco da Silva
#Função 3: Raylany Shimizu de Macêdo
#Função 4: Lara Vitória da Costa Bezerra
#Função 5: Wesley Nascimento Santos

import time
import sys

def progress_bar(iterations):
    for i in range(iterations + 1):
        percent = (i / iterations) * 100
        bar = '█' * i + '-' * (iterations - i)
        sys.stdout.write(f'\r[{bar}] {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)

# Função 00 Imprimir lista formatada.
def imprimir_lista_formatada(tarefas):
    contador = 1
    for i in range(len(tarefas)):
        print(contador, " - ", tarefas[i])
        contador = contador + 1


# função 01 adicionar tarefas.
def adicionar_tarefas(tarefas, novas_tarefas):
    tarefas.extend(novas_tarefas.split(', '))


# Função 02 Marcar tarefa como concluída.
def marcar_tarefa_como_concluida(tarefas):
    if len(tarefas) == 0:
        print("Sua lista está vazia! Não há tarefas para marcar como concluída.")
        return

    imprimir_lista_formatada(tarefas)  # Lista as tarefas para o usuário

    while True:  # Loop para garantir que o usuário insira um valor válido
        try:
            indice = int(input("Qual tarefa você concluiu? Digite o número dela: ")) - 1
            if indice >= 0 and indice < len(tarefas):  # Verifica se o índice é válido
                tarefas[indice] += " - Concluída"  # Marca a tarefa como concluída
                print(f'Ótimo trabalho! A tarefa "{tarefas[indice]}" foi marcada como concluída!')
                break  # Sai do loop após uma entrada válida
            else:
                print("Número inválido! Tente novamente.")
        except ValueError:  # Captura a exceção se a conversão falhar
            print("Por favor, digite um número válido.")


# Função 03 remover tarefas.
def remover_tarefa():
    if tarefas:
        imprimir_lista_formatada(tarefas)  # Lista as tarefas antes de remover

        while True:
            entrada = input("Número da tarefa a remover: ")
            if entrada.isdigit():  # Verifica se a entrada é um número
                indice = int(entrada) - 1  # Calcula o índice
                if 0 <= indice < len(tarefas):
                    print(f'Tarefa "{tarefas[indice]}" removida!')
                    tarefas.pop(indice)  # Remove a tarefa pelo índice
                    break  # Sai do loop após remoção
                else:
                    print("Número inválido. Tente um número dentro da lista.")
            else:
                print("Por favor, insira um número válido.")  # Mensagem de erro se não for número
    else:
        print("Não há tarefas para remover.")

#Função 04 Visualizar tarefas pendentes.
def visualizar_tarefas_pendentes(tarefas):
  if not tarefas:
    print("\nNão há tarefas pendentes")

  else:
    print("\nTarefas pendentes:")
    contador = 1
    tarefa_pendente = False

    for i in range(len(tarefas)):
      if ("Concluída") not in tarefas[i]:
        print(contador, "-", tarefas[i])
        contador += 1
        tarefa_pendente = True

# interface
sistema = True
while sistema:
    print("-" * 40)
    print("\nMenu do gerenciador de tarefas \nEscolha uma ação:")
    print(
        "\n1. Adicionar tarefas \n2. Marcar tarefa como concluída \n3. Remover tarefa \n4. Visualizar tarefas pendentes \n5. Sair")
    print("-" * 40)
    while True:  # Loop para garantir que a entrada é um número válido
        try:
            opcao = int(input())  # Tenta converter a entrada para um inteiro
            if opcao in [1, 2, 3, 4, 5]:  # Verifica se a opção está dentro do intervalo esperado
                break  # Sai do loop se a opção é válida
            else:
                print("\n(((Digite uma opção válida!)))")  # Mensagem se o número não estiver entre 1 a 5
        except ValueError:  # Captura a exceção se a conversão falhar
            print("Por favor, digite um número válido.")  # Mensagem de erro para entrada inválida

    if (opcao == 1):
        print("\nEscreva o nome das novas Tarefas: ")
        novas_tarefas = str(input())
        adicionar_tarefas(tarefas, novas_tarefas)
        novas_tarefas = novas_tarefas.split(", ")
        print("\nA lista de tarefas adicionadas é:")
        for tarefa in novas_tarefas:
            print("- " + tarefa)


    elif opcao == 2:
        marcar_tarefa_como_concluida(tarefas)

    elif opcao == 3:
        remover_tarefa()

    elif opcao == 4:
        visualizar_tarefas_pendentes(tarefas)

    elif opcao == 5:
        sistema = False
        print("Saindo do sistema...")
