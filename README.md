# JumpQuest - Atividade Prática

## Sobre o Projeto
Este projeto é uma atividade prática para a disciplina de **Linguagem de Programação Aplicada**, com o objetivo de aplicar conceitos de programação através do desenvolvimento de um jogo em **Python** utilizando a biblioteca **Pygame**.

## Objetivo Educacional
O principal objetivo desta atividade é proporcionar um aprendizado prático sobre:
- Estruturas de controle e laços de repetição;
- Manipulação de eventos e entradas do usuário;
- Uso de classes e objetos para modelagem de entidades do jogo;
- Gerenciamento de estados do jogo e transição entre fases;
- Persistência de dados (salvamento de scores).

## Tecnologias Utilizadas
- **Python 3**
- **Pygame** (para renderização e controle do jogo)
- **SQLite** (para armazenamento de pontuações)

## Como Executar o Projeto
### 1. Instalar Dependências
Certifique-se de que possui o Python instalado em sua máquina. Em seguida, instale as dependências necessárias com o seguinte comando:
```sh
pip install pygame
```

### 2. Executar o Jogo
Para iniciar o jogo, basta rodar o seguinte comando no terminal:
```sh
python main.py
```

## Estrutura do Projeto
```
📁 projeto-jogo
│-- 📂 code
│   │-- Const.py       # Constantes do jogo
│   │-- Level.py       # Gerenciamento de fases
│   │-- Menu.py        # Menu principal
│   │-- Score.py       # Gerenciamento de pontuações
│   │-- Player.py      # Classe do jogador
│   │-- Obstacle.py    # Classe de obstáculos
│   │-- Entity.py      # Entidades gerais do jogo
│-- assets/           # Recursos do jogo (imagens, sons, etc.)
│-- main.py           # Arquivo principal do jogo
│-- README.md         # Documentação do projeto
```

## Funcionalidades do Jogo
- Menu interativo para iniciar ou visualizar scores anteriores;
- Fases progressivas com desafios crescentes;
- Sistema de colisão e movimentação do personagem;
- Registro e exibição dos 10 melhores scores.

## Contribuição
Este é um projeto educacional, mas sugestões e melhorias são bem-vindas! Caso queira contribuir, faça um fork do repositório e envie um Pull Request com suas melhorias.

## Autor
Desenvolvido para a disciplina de **Linguagem de Programação Aplicada**.

---
*Este projeto tem fins exclusivamente educacionais.*

