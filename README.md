# Conveyance Manager 🚗

> Um sistema de gerenciamento de frota de veículos desenvolvido em Python

## Sobre 📚

- O Conveyance Manager (do inglês "gerenciador de transportes") é um projeto da disciplina de Programação orientada a objetos da Universidade Federal do Cariri (UFCA), a qual é ministrada pelo professor Jayr Pereira. O objetivo é um desenvolver sistema de linha de comando (CLI) para gerenciar a frota de veículos de uma empresa de transporte. Nele são necessárias as funcionalidades de cadastro de veículos, controle de manutenções, alocação a motoristas, registro de abastecimentos, cálculo de custos médios e relatórios de desempenho.


## 📋 Pré-requisitos

- Python 3

## 📦 Estrutura do projeto

```
Conveyance-Manager/
├── main.py                      # Arquivo principal do sistema
|
├── data                       
|   └── dados.db                 # Arquivo de dados do sistema
|
├── config
|   └── settings.json            # Arquivo json de configurações
|
├── modules
|   ├── __init__.py              # Transforma o diretório em um pacote    
|   ├── abastecimentos.py        # Classe utilizada para os abastecimentos
|   ├── alocacao.py              # Classe utilizada para as alocações
|   ├── configuracoes.py         # Classe utilizada para as configurações
|   ├── manutencoes.py           # Classe utilizada para as manutenções
|   ├── motoristas.py            # Classe utilizada para os motoristas e o cadastro deles
|   ├── relatorios.py            # Classe utilizada para os relatórios
|   └── veiculos.py              # Classe utilizada para os veículos e o cadastro deles
|
└── README.md                    # Este arquivo
```

## Como usar ✍️
- 1 - Clone o repositório.
- 2 - Execute o arquivo principal `python main.py`.
- 3 - Siga as instruções do programa.


## 📓 UML textual

### Classe - Abastecimento ⛽

> É a classe que cuida do abastecimento dos veículos e do consumo de combustível.

#### Atributos
- Data
- Tipo de combustível
- Litros
- Valor
- Veículo
- ID

#### Métodos
- Tabela de abastecimentos
- Registrar abastecimento
- Calcular valor
- Abastecer veículo
- Atualizar status
- Consumo padrão

### Classe - Alocação 🛞

> É a classe que cuida da alocação de veículos a motoristas e da quilometragem do veículo.

#### Atributos
- Origem
- Data
- Distância
- Destino
- ID
- Motorista
- Veículo

#### Métodos
- Associar e registrar
- Procurar alocação
- Atualizar quilometragem
- Tabela de alocações
- Permissão para alocação
- Validar CNH
- Validar combustível

### Classe - Configurações ⚙️

> É a classe que cuida das configurações.

#### Métodos
- Configurar gasolina
- Configurar manutenção
- Consultar manutenção
- Configurar compatibilidade
- Configurar limite
- Configurar consumo padrão

### Classe - Manutenção 🔧

> É a classe que cuida da manutenção de veículos.

#### Atributos
- Data
- Tipo
- Descrição
- Custo
- ID

#### Métodos
- Tabela de manutenções
- Ler manutenção
- Consultar manutenção
- Marcar veiculo
- Liberar veiculo
- Registrar manutenção

### Classe - Relatório 📝

> É a classe que cria os relatórios.

#### Métodos
- Relatório inicial
- Gerar relatório do custo de manutenção
- Gerar relatório viagens
- Gerar relatório da quilometragem

### Classe - Veículo 🚘

> É a classe dos veículos.

#### Atributos
- Placa
- Marca
- Modelo
- Tipo
- Ano
- Quilometragem
- Consumo médio
- Status
- Combustível

#### Métodos
- Tabela de veículos
- Criar veículo
- Ler veículo
- Mostrar veículo
- Atualizar veículo
- Remover veículo

#### Herança
- É herdado por moto
- É herdado por caminhão
- É herdado por carro

### Classe - Moto 🏍️

> É a classe das motos.

#### Herança
- Herda da classe veículo

### Classe - Carro 🚘

> É a classe dos carros.

#### Herança
- Herda da classe veículo

### Classe - Caminhão 🚚

> É a classe das caminhão.

#### Herança
- Herda da classe veículo

### Classe - Motorista🚦

> É a classe dos motoristas.

#### Atributos
- Nome
- CPF
- Categoria CNH
- Experiência
- Disponibilidade
- Histórico

#### Métodos
- Tabela de motoristas
- Criar motorista
- Ler motorista
- Mostrar motorista
- Atualizar motorista
- Remover motorista

### Relacionamentos 🫂

> São os relacionamentos entre as classes.

- Cadastro de motoristas --> Cria, lê, atualiza e remove --> Motorista
- Cadastro de veículos --> Cria, lê, atualiza, remove e registra o histórico --> Veículo
- Manutenção --> Marca, libera e associa --> Veículo
- Alocação --> Associa veículo --> Motorista
- Veículo --> É associado --> Motorista
- Alocação --> Atualiza quilometragem --> Veículo
- Abastecimento --> Calcula consumo médio, abastece, atualiza status --> Veículo

> Mais detalhes sobre os métodos estão nas docstrings do código.
