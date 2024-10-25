'''Projeto 3: Sistema de Gerenciamento de Tarefas
Descrição do Projeto
Uma equipe deseja um sistema para gerenciar suas tarefas diárias. Eles precisam
registrar tarefas, marcar tarefas como concluídas, remover tarefas e visualizar todas
as tarefas pendentes.
Funcionalidades Principais:
1. Adicionar Tarefa
2. Marcar Tarefa como Concluída
3. Remover Tarefa
4. Visualizar Tarefas Pendentes
5. Sair do Sistema'''

# Lista onde será feita todas as interações do usuário
tarefas = ["tarefa1", "tarefa2", "tarefa3"]


def gerenciador(escolha, adicionar=None, indice=None, concluida=None):

    # Se a escolha for 1, adicionar uma nova tarefa ao final da lista
    if escolha == 1:
        # append() Insere uma tarefa ao final da lista
        tarefas.append(adicionar)


while True:

    print("Tarefas pendentes:" + " " + str(len(tarefas)) +
          "\nListagem de tarefas" + " " + str(tarefas))

    print("\nDigite 1 para adicionar mais um item a lista de tarefas, 2 para marcar alguma tarefa como concluída, 3 para remover alguma tarefa, 0 para fechar o sistema:")

    # (ATENÇÃO) Aqui vocês contribuem adicionando as funcionalidades que faltam eu fiz a de adicionar

    # Solicita ao usuário que escolha uma opção
    escolha = int(input())
    # Se a opção for 1, o programa solicita o nome da nova tarefa
    if escolha == 1:
        # Armazena esse nome na variável 'nova_tarefa'
        nova_tarefa = str(input("Nome da tarefa: "))
        # Chamando a função 'gerenciador' que irá adicionar 'nova_tarefa' à lista de tarefas.
        gerenciador(escolha, adicionar=nova_tarefa)
