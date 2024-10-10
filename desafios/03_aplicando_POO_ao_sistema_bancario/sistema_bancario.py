from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


class Transacao(ABC):
    @abstractmethod
    def registrar(self) -> str:
        pass


class Deposito(Transacao):
    def __init__(self, valor:float):
        self._valor: float = valor

    def registrar(self):
        return f'{datetime.now()} - Depósito no valor de R${self._valor:.2f}'


class Saque(Transacao):
    def __init__(self, valor:float):
        self._valor: float = valor

    def registrar(self):
        return f'{datetime.now()} - Saque no valor de R${self._valor:.2f}'


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao) -> None:
        self._transacoes.append(transacao.registrar())

    def __str__(self):
        return self._transacoes


class PessoaFisica:
    def __init__(self, nome:str, cpf:str, data_nascimento:str):
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: str = data_nascimento


class Cliente(PessoaFisica):
    def __init__(self, nome:str, cpf:str, data_nascimento:str, endereco:str):
        super().__init__(nome, cpf, data_nascimento)
        self._endereco: str = endereco
        self._contas: list = []

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def contas(self) -> list:
        return self._contas

    def realizar_transacao(self) -> None:
        pass

    def adicionar_conta(self, conta:object) -> None:
        self._contas.append(conta)

    def __str__(self):
        return f'Cliente: {self.nome}, CPF: {self.cpf}'


class Conta:
    _AGENCIA: str = '0001'

    def __init__(self, cliente:Cliente, numero:int):
        self._cliente: Cliente = cliente
        self._numero: int = numero
        self._saldo: float = 0
        self._historico = Historico()
        self._cliente.adicionar_conta(self)

    @property
    def agencia(self) -> str:
        return self._AGENCIA

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def titular(self) -> str:
        return self._cliente.nome

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def historico(self):
        if len(self._historico.transacoes) != 0:
            return self._historico.transacoes
        else:
            return None

    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int) -> object:
        return cliente.adicionar_conta(cls(cliente, numero))

    def sacar(self, valor:float) -> None:
        pass

    def depositar(self, valor:float) -> None:
        try:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
        except:
            print('Algo deu errado...')
        else:
            print('Depósito realizado com sucesso!')

    def __str__(self):
        return f'Conta de {self._cliente.nome}\nAgência: {self._AGENCIA}\nConta: {self._numero}'


class ContaCorrente(Conta):
    _saques_realizados = 0

    def __init__(self, cliente:Cliente, numero:int):
        super().__init__(cliente, numero)
        self._limite: float = 500
        self._LIMITE_SAQUES: int = 3

    @property
    def limite(self) -> float:
        return self._limite

    def sacar(self, valor: float) -> None:
        if self._saques_realizados < self._LIMITE_SAQUES:
            if valor <= self.saldo:
                try:
                    self._saldo -= valor
                    self._historico.adicionar_transacao(Saque(valor))
                except:
                    print('Algo deu errado...')
                else:
                    self._saques_realizados += 1
                    print('Saque realizado com sucesso!')
            elif valor <= self._saldo + self._limite:
                try:
                    self._limite -= valor - self._saldo
                    self._saldo = 0
                    self._historico.adicionar_transacao(Saque(valor))
                except:
                    print('Algo deu errado...')
                else:
                    self._saques_realizados += 1
                    print('Saque realizado utilizando o limite da conta!')
            else:
                print('Saldo e limite insuficientes para realizar este saque.')
        else:
            print('Você já atingiu o limite de saques permitidos para esta conta.')


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente_existe = filtrar_cliente(cpf, clientes)

    if cliente_existe:
        print("Já existe um cliente cadastrado com esse cpf.")
        return

    nome = input("Informe o nome do usuário: ")
    nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = Cliente(nome, cpf, nasc, endereco)

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")

    return clientes


def criar_conta(numero, clientes, contas):
    cpf = input("Informe o CPF do titular (apenas números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        numero += 1
        conta = ContaCorrente(cliente, numero)
        contas.append(conta)
        print("Conta criada com sucesso!")
        return contas, numero

    print("Usuário não encontrado para o CPF informado. Por favor, cadastre o usuário antes de criar uma conta.")
    return contas, numero


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def listar_contas(contas) -> None:
    if len(contas) != 0:
        for conta in contas:
            linha = f"""
            Agência: {conta.agencia}
            C/C: {conta.numero}
            Titular: {conta.titular} 
            """

            print("=" * 50)
            print(textwrap.dedent(linha))
    else:
        print('Não há contas registradas ainda.')


def deposito(contas, valor) -> None:
    numero = int(input('Informe o número da conta em que o valor será depositado: '))

    for conta in contas:
        if numero == conta.numero:
            conta.depositar(valor)
            return

    print('A conta informada não foi encontrada. Tente novamente.')


def saque(contas, valor):
    numero = int(input('Informe o número da conta da qual o valor será sacado: '))

    for conta in contas:
        if numero == conta.numero:
            conta.sacar(valor)
            return

    print('A conta informada não foi encontrada. Tente novamente.')


def exibir_extrato(contas):
    numero = int(input('Informe o número da conta da qual deseja ver o extrato: '))

    for conta in contas:
        if numero == conta.numero:
            print("\n================ EXTRATO ================")
            if conta.historico is not None:
                for transacao in conta.historico:
                    print(transacao)
            else:
                print('Não foram realizadas transações nesta conta ainda.')
            print(f"\nSaldo atual: {conta.saldo:.2f}\nLimite disponível: R${conta.limite:.2f}")
            print("==========================================")


def main():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Cadastrar Novo Cliente
    [ncc] Cadastrar Nova Conta Corrente
    [lc] Listar Contas
    [q] Sair

    => """

    clientes = []
    contas = []
    numero_conta = 0

    while True:

        opcao = input(textwrap.dedent(menu))

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            deposito(contas, valor)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saque(contas, valor)
        elif opcao == "e":
            exibir_extrato(contas)
        elif opcao == "nc":
            clientes = criar_cliente(clientes)
        elif opcao == "ncc":
            contas, numero_conta = criar_conta(
                numero=numero_conta,
                clientes=clientes,
                contas=contas
            )
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
