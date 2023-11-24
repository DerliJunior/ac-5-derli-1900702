from abc import ABC

# Nome: Derli Rodrigues de Jesus Junior
# RA: 1900702
# ADS: 3C

# Nome: Vilma Oliveira de Moraes Benedito
# RA: 2203415

def main():
    menu = Menu()

    menu.exibir_menu()

    


# Classe Pessoa:
# Atributos: nome, cpf, data_nascimento.
# MÃ©todo: __init__ para inicializaÃ§Ã£o.
# Classe Paciente (herda de Pessoa):
# Sem atributos ou mÃ©todos adicionais especÃ­ficos, apenas o mÃ©todo construtor.
# Classe Medico (herda de Pessoa):
# Atributos adicionais: crm, especialidade.
# # MÃ©todo: __init__ para inicializaÃ§Ã£o com atributos adicionais.

# Classe Consulta:
# Atributos: paciente (objeto Paciente), medico (objeto Medico), data_hora, observacoes.
# MÃ©todo: __init__ para inicializaÃ§Ã£o.
# Classe Menu:
# Atributos: medicos (dicionÃ¡rio), pacientes (dicionÃ¡rio), consultas (lista).
# MÃ©todos:
# incluir_medico(): Adiciona um novo mÃ©dico ao dicionÃ¡rio medicos.
# incluir_paciente(): Adiciona um novo paciente ao dicionÃ¡rio pacientes.
# agendar_consulta(): Cria uma nova consulta e a adiciona Ã  lista consultas.
# ver_agenda(): itera sobre a lista consultas e imprime os detalhes de cada consulta.
# exibir_menu(): Exibe as opÃ§Ãµes do menu e permite a interaÃ§Ã£o com o usuÃ¡rio.

class Pessoa(ABC):
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"Nome: {self.nome}\n CPF: {self.cpf}\n Data de Nascimento: {self.data_nascimento}"


class Paciente(Pessoa):
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(nome, cpf, data_nascimento)


class Medico(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, crm, especialidade):
        super().__init__(nome, cpf, data_nascimento)
        self.crm = crm
        self.especialidade = especialidade

    def __str__(self):
        return f"{super().__str__()}\n CRM: {self.crm}\n Especialidade: {self.especialidade}"


class Consulta:
    def __init__(self, paciente, medico, data_hora, observacoes):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.observacoes = observacoes

    def __str__(self):
        return f"Paciente:\n {self.paciente}\nMédico:\n {self.medico}\nData: {self.data_hora}\nObeservações: {self.observacoes}"


class Menu:
    def __init__(self):
        self.medicos = {}
        self.pacientes = {}
        self.consultas = []

    def incluir_paciente(self):
        nome = input("Digite o nome do paciente: ")
        cpf = input("Digite o cpf do paciente: ")
        data_nascimento = input(
            "Digite a data de nascimento do paciente: ")

        paciente = Paciente(nome, cpf, data_nascimento)
        self.pacientes[cpf] = paciente

        print(f"Paciente {nome} cadastrado com sucesso")
        print("")

    def incluir_medico(self):
        nome = input("Digite o nome do mÃ©dico: ")
        cpf = input("Digite o cpf do mÃ©dico: ")
        data_nascimento = input(
            "Digite a data de nascimento do mÃ©dico: ")
        crm = input("Digite o CRM do mÃ©dico: ")
        especialidade = input("Digite a especialidade do mÃ©dico: ")

        medico = Medico(nome, cpf, data_nascimento, crm, especialidade)
        self.medicos[crm] = medico

        print(f"MÃ©dico {nome} cadastrado com sucesso")
        print("")

    def agendar_consulta(self):
        crm = input("Digite o CRM do mÃ©dico: ")
        medico = self.medicos[crm]

        cpf = input("Digite o CPF do paciente: ")
        paciente = self.pacientes[cpf]

        data_hora = input("Digite a data e hora da consulta: ")
        observacoes = input("Digite as observaÃ§Ãµes da consulta: ")

        consulta = Consulta(paciente, medico, data_hora, observacoes)
        self.consultas.append(consulta)

        print("Consulta agendada com sucesso")
        print("")

    def listar_pacientes(self):
        if len(self.pacientes) == 0:
            print("NÃ£o hÃ¡ pacientes cadastrados")
            print("")
            return

        for cpf, paciente in self.pacientes.items():
            print(
                f"CPF: {cpf} \t Nome: {paciente.nome} \t Data de Nascimento: {paciente.data_nascimento}")
            
        print("")

    def listar_medicos(self):
        if len(self.medicos) == 0:
            print("NÃ£o hÃ¡ mÃ©dicos cadastrados")
            print("")

            return

        for crm, medico in self.medicos.items():
            print(
                f"CRM: {crm} \t Nome: {medico.nome} \t Especialidade: {medico.especialidade}")
        print("")

    def ver_agenda(self):

        if len(self.consultas) == 0:
            print("Não há consultas agendadas")
            return

        for consulta in self.consultas:
            print(consulta)
            print("")
        
        print("")

    def exibir_menu(self):
        while True:
            print("1 - Cadastrar Paciente")
            print("2 - Cadastrar Medico")
            print("3 - Cadastrar Consulta")
            print("4 - Listar Pacientes")
            print("5 - Listar Médicos")
            print("6 - Listar Consultas")
            print("7 - Sair")

            op = int(input("Digite a opção desejada: "))
            if op == 1:
                self.incluir_paciente()

            elif op == 2:
                self.incluir_medico()

            elif op == 3:
                self.agendar_consulta()

            elif op == 4:
                self.listar_pacientes()

            elif op == 5:
                self.listar_medicos()

            elif op == 6:
                self.ver_agenda()

            elif op == 7:
                print("Hospital Impacta has logoff successfully")
                break
            else:
                print("Opção inválida!")


if __name__ == '__main__':
    main()
