# Sistema de Gestão de Garagem (em desenvolvimento)

Este é um sistema de console para gestão de veículos, focado em organização e eficiência. Através de uma interface de terminal, o programa permite ao usuário registrar, consultar e editar informações de carros.

## Funcionalidades Atuais
***Adicionar Veículo:*** Permite inserir novos carros no sistema, coletando informações como placa, modelo e marca.

***Consultar por Placa:*** Possibilita buscar um veículo específico a partir de sua placa.

***Consultar Todos:*** Exibe uma lista completa de todos os veículos cadastrados no banco de dados.

***Limpar Terminal:*** Um recurso de utilidade que limpa a tela do console para uma visualização mais organizada.

# Arquitetura e Design
A base do projeto é uma estrutura sólida de **programação orientada a objetos (POO)** e design modular.

***Classes e Relações:*** O sistema utiliza classes para representar os objetos do mundo real. A classe Veiculo serve como uma classe-base, da qual a classe Carro herda atributos e funcionalidades. A classe Marca, por sua vez, é um componente que se relaciona com as outras classes, demonstrando o uso de composição para estruturar os dados de forma mais organizada e consistente.

***Gerenciamento de Dados:*** O sistema utiliza um dicionário (dict) onde a placa é a chave única, e o valor é um objeto do veículo. Embora a sua versão inicial use uma lista como valor, a estrutura de classes já está definida para armazenar objetos, o que garante a integridade dos dados e um acesso mais rápido à informação.

***Lógica de Controle:*** Um dos pontos mais fortes do projeto é a centralização da lógica de controle. A sua implementação de um dicionário de opções (opcoes) mapeia os comandos do usuário ('I', 'C') diretamente para as funções correspondentes. Isso cria um sistema de menu elegante, que elimina a necessidade de cadeias longas de if/elif e facilita a adição de novas funcionalidades no futuro.
