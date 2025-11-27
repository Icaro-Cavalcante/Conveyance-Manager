# Conveyance Manager 🚗

> Um sistema de gerenciamento de frota de veículos desenvolvido em Python

## Sobre 📚

- O Conveyance Manager (do inglês "gerenciador de transportes") é um projeto da disciplina de Programação orientada a objetos da Universidade Federal do Cariri (UFCA), a qual é ministrada pelo professor Jayr Pereira. O objetivo é um desenvolver sistema de linha de comando (CLI) ou uma API mínima (FastAPI ou Flask, opcional) para gerenciar a frota de veículos de uma empresa de transporte. Nele são necessárias as funcionalidades de cadastro de veículos, controle de manutenções, alocação a motoristas, registro de abastecimentos, cálculo de custos médios e relatórios de desempenho.


## 📋 Pré-requisitos

- Python 3

## 📦 Estrutura do projeto

```
Conveyance-Manager/
├── main.py                      # Arquivo principal do sistema
|
├── data                       
|   ├── motoristas.db            # Dados dos motoristas
|   └── veiculos.db              # Dados dos veículos
|
├── config
|   └── settings.json            # Arquivo json de configurações
|
├── modules     
|   ├── abastecimentos.py        # Classe utilizada para os abastecimentos
|   ├── alocacao.py              # Classe utilizada para as alocações
|   ├── manutencoes.py           # Classe utilizada para as manutenções
|   ├── motoristas.py            # Classe utilizada para os motoristas e o cadastro deles
|   ├── relatorios.py            # Classe utilizada para os relatórios
|   └── veiculos.py              # Classe utilizada para os veículos e o cadastro deles
|
└── README.md                    # Este arquivo
```

## 📓 UML textual

### Classe - Abastecimento ⛽

> É a classe que cuida do abastecimento dos veículos e do consumo de combustível.

#### Atributos
- Data
- Tipo de combustível
- Litros
- Valor
- ID

#### Métodos
- Registrar abastecimento
- Calcular consumo
- Consumo padrão

### Classe - Alocação 🛞

> É a classe que cuida da alocação de veículos a motoristas e da quilometragem do veículo.

#### Atributos
- Origem
- Distância
- Destino
- ID

#### Métodos
- Associar e registrar
- Atualizar quilometragem
- Bloquear alocação

### Classe - Manutenção 🔧

> É a classe que cuida da manutenção de veículos.

#### Atributos
- Data
- Tipo
- Descrição
- Custo
- ID

#### Métodos
- Marcar veiculo
- Liberar veiculo
- Registrar manutenção
- Associar veículo

### Classe - Relatório 📝

> É a classe que cria os relatórios.

#### Métodos
- Gerar relatório do custo de manutenção
- Gerar ranking veículos
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

### Classe - Cadastro de veículos 🪪

> É a classe que cuida do CRUD dos veículos.

#### Atributo
- Veículo

#### Métodos
- Criar veículo
- Ler veículo
- Atualizar veículo.
- Remover veículo
- Registrar histórico

### Classe - Motorista🚦

> É a classe dos motoristas.

#### Atributos
- Nome
- CPF
- Categoria CNH
- Experiência
- Disponibilidade
- Histórico

### Classe - Cadastro de motoristas ✈️

> É a classe que cuida do CRUD dos motoristas.

#### Atributo
- Motorista

#### Métodos
- Criar motorista
- Ler motorista
- Atualizar motorista
- Remover motorista

### Relacionamentos 🫂

> São os relacionamentos entre as classes.

- Cadastro de motoristas --> Cria, lê, atualiza e remove --> Motorista
- Cadastro de veículos --> Cria, lê, atualiza, remove e registra o histórico --> Veículo
- Manutenção --> Marca, libera e associa --> Veículo
- Alocação --> Associa veículo --> Motorista
- Alocação --> Atualiza quilometragem --> Veículo
- Abastecimento --> Calcula consumo médio --> Veículo

> Mais detalhes sobre os métodos estão nas docstrings do código.
