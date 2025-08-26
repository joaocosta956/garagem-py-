# Sistema de garagem de carro
# Precisa ter placa, nome do carro, marca do carro
# Sistema de consulta por placa
# Criar primeiro uma instância da Classe Carro para depois poder adicionar
# parametros
# Verfica se todos requisitos foram preenchidos (Coloquei bool, mas poderia ser
# None)
# Classe de marca e carro, são instancias que compõem com a placa
# Placa é o único atributo que fica salvo em um set
# Verificação da lógica das placas

from os import system

system('cls')


class Marca:
    def __init__(self, nome, pais_origem) -> None:
        self.nome = nome
        self.pais_origem = pais_origem


class Veiculo:
    def __init__(self, placa, modelo, marca) -> None:
        self.placa = placa
        self.modelo = modelo
        self.marca = marca


class Carro(Veiculo):
    def __init__(self, placa, modelo, marca,  quilometros=None) -> None:
        # Construtor classe-mãe
        super().__init__(placa, modelo, marca)
        # Atributos da classe
        self.quilometros = quilometros


placas = {
    # Aqui fica as placas, modelo e marca placa [modelo, marca]
    'AAAA1': ['Civic', 'Honda'],

}


def terminal_clean():
    # Serve para limpar o terminal
    system('cls')


def consulta_placa():
    # A informação é recebida de dentro da função, ela não recebe parametros
    placa = input('\nInsira o número da placa: ').upper()
    if placa in placas:
        for x in placas[placa]:
            print(x)
    else:
        print('Não há esta placa!')


def adiciona_placa():
    # Parametros definidos dentro da função via input, mas poderia coletar
    # fora também, fiz assim pois evita bastante if's
    modelo = input('Insira o modelo do carro: ')
    marca = input('Insira a marca do carro: ')
    placa = input('Insira a placa: ')
    if modelo and marca and placa:
        placa = placa.upper().strip()
        placas[placa] = [modelo, marca]


def consulta_todas():
    # Pega todos os valores do dicionário
    for x in placas:
        print(x, placas[x])


def check_opcao(opcao: str):
    # Verifica se a opção digitada está dentro de opcoes
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print('Digite uma das letras informadas.')


# Aqui só funciona com funções!!!!!
opcoes = {
    'I': adiciona_placa,
    'C': consulta_placa,
    'L': terminal_clean,
    'A': consulta_todas,
    '': ...,
    '': ...,
    '': ...,
}

# Coloquei a mensagem em uma variavel, mas poderia ser mais dinamico colocando
# em um lista e pegando a primeira letra (não vejo necessidade de fazer isto
# pois está um código simples, mas seria interessante caso fique muito extenso)
mensagem = f'\n{10*"-"}[I]Inserir [C]Consultar [S]Sair [L]Limpar {10*"-"}'

if __name__ == "__main__":
    while True:
        print(mensagem)
        opcao = input('Insira o comando: ').upper()
        check_opcao(opcao)
