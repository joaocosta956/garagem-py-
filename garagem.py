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

    def __repr__(self):
        return f'{self.nome, self.pais_origem}'


class Veiculo:
    def __init__(self, placa, modelo, marca) -> None:
        self._placa = placa
        self._modelo = modelo
        self._marca = marca

        @property
        def placa(self):
            return self._placa

        @property
        def modelo(self):
            return self._modelo

        @property
        def marca(self):
            return self._marca

    def __repr__(self) -> str:
        return f'{self._modelo,self._marca}'


class Carro(Veiculo):
    def __init__(self, placa, modelo, marca,  quilometros=None) -> None:
        # Construtor classe-mãe
        super().__init__(placa, modelo, marca)
        # Atributos da classe
        self.quilometros = quilometros


marcas = {
    'HONDA': Marca('Honda', 'Japão'),
    'VOLKSWAGEM': Marca('Volkswagem', 'Alemanha'),
}

placas = {
    # Aqui fica as placas, modelo e marca placa [modelo, Obj Marca]

}


def terminal_clean():
    # Serve para limpar o terminal
    system('cls')


def consulta_placa():
    # A informação é recebida de dentro da função, ela não recebe parametros
    placa = input('\nInsira o número da placa: ').upper()
    if placa in placas:
        print(placas[placa])
    else:
        print('Não há esta placa!')


def consulta_marcas():
    ...

# FUNCAO QUE ADICIONA MARCAS


def adiciona_marca():
    marca_input = input("Insira o nome da Marca: ").upper()
# Primeiro ve se ja n existe esta marca
    if marca_input in marcas:
        print('Marca já existente')
        return None
# Se n existir ele pede o pais
    else:
        pais_input = input("Insira o país de origem: ")
        nova_marca = Marca(
            nome=marca_input,
            pais_origem=pais_input,
        )
        marcas[marca_input] = nova_marca


def adiciona_placa():
    # Parametros definidos dentro da função via input, mas poderia coletar
    # fora também, fiz assim pois evita bastante if's
    modelo_input = input('Insira o modelo do carro: ')
    marca_input = input('Insira a marca do carro: ').upper()
    # Vai conferir se a marca existe
    if marca_input not in marcas:
        print('Marca não existente')
        return None

    placa_input = input('Insira a placa: ')
    # Vai conferir se a placa já existe
    if placa_input in placas:
        print('Placa já existente.')
        return False

    marca_obj = marcas[marca_input]

    novo_carro = Carro(
        placa=placa_input,
        modelo=modelo_input,
        marca=marca_obj
    )

    placas[placa_input] = novo_carro


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
    'M': adiciona_marca,
    'S': exit,
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
