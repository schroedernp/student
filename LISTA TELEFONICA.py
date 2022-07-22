class Contato():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.telefone

class Processamento():
    def inserir_pessoa(nome, telefone):
        return Contato(nome, telefone)

    def listar_todos(lista):
        for tel in lista:
            print(f'{tel.getNome()} - {tel.getTelefone()}')

    def listarNome(lista, nome):
        cont = 0
        for tel in lista:
            if tel.getNome() == nome:
                print(f'{tel.getNome()} - {tel.getTelefone()}')
                break
            cont += 1

    def deletar_todos(lista):
        if len(lista) != 0:
            lista.clear()
            return 'Todos os contatos foram removidos!'
        else:
            return 'A lista telefônica está vazia!'

    def deletarNome(lista, nome):
        if len(lista) != 0:
          cont = 0
          for tel in lista:
            if tel.getNome() == nome:
              lista.pop(cont)
              return print(f'Contado {nome} removido com sucesso!')
            else:
              return 'Nome não encontrado!'
        else:
          return 'Lista está vazia!'

#------------------------------------------------------------------------------------------------------------------------------
agenda = []
titulo = 'Bem vindo à agendar telefônica'
print('-='*30)
print(titulo.center(60, ' '))
print('-='*30)

while True:
    print('1 - Cadastrar contato;')
    print('2 - Listar contato;')
    print('3 - Listar todos os contatos;')
    print('4 - Apagar contato;')
    print('5 - Apagar todos os contatos;')
    print('6 - Sair.')
    op = (int(input('\nDigite a opção desejada: ')))
    if op == 1:
        nome = input('Digite o nome:')
        tel = int(input('Digite o telefone:'))
        agenda.append(Processamento.inserir_pessoa(nome, tel))
    elif op == 2:
        nome = input('Digite o nome para a pesquisa: ')
        Processamento.listarNome(agenda, nome)
    elif op == 3:
        Processamento.listar_todos(agenda)
    elif op == 4:
        nome = input('Digite o nome para a pesquisa: ')
        print(Processamento.deletarNome(agenda, nome))
    elif op == 5:
        print(Processamento.deletar_todos(agenda))
    elif op == 6:
        break
    else:
        print('Digite a opção correta!')

print('Obrigado por usar a agenda!!!')