# Fruit Dunk Challenge

## Sobre o Jogo

Fruit Dunk Challenge é um jogo 2D simples e divertido desenvolvido em Python com a biblioteca Pygame. O jogador controla um personagem que precisa coletar o máximo de frutas que caem do céu, enquanto desvia de obstáculos perigosos. O objetivo é alcançar a maior pontuação possível!

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `game.py`: Contém todo o código-fonte e a lógica do jogo.
- `assets/`: Pasta destinada a armazenar as imagens do jogo (`player.png`, `fruit.png`, `obstacle.png`).
- `README.md`: Este arquivo, com a documentação do projeto.

## Pré-requisitos

Para executar o jogo ou gerar o executável, você precisa ter o Python instalado em seu computador. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

Além disso, é necessário instalar a biblioteca `pygame`.

## Instalação

1.  **Clone o repositório ou baixe os arquivos do projeto.**

2.  **Instale a dependência `pygame`:**
    Abra o terminal ou prompt de comando e execute o seguinte comando:
    ```bash
    pip install pygame
    ```

## Como Jogar

1.  **Adicione as imagens (opcional):**
    Para uma experiência visual completa, coloque os arquivos de imagem `player.png`, `fruit.png` e `obstacle.png` dentro da pasta `assets/`. Caso as imagens não sejam encontradas, o jogo irá gerar formas coloridas no lugar.

2.  **Execute o jogo:**
    Navegue até a pasta do projeto pelo terminal e execute o seguinte comando:
    ```bash
    python3 game.py
    ```

### Controles

- **Seta para a Esquerda:** Move o jogador para a esquerda.
- **Seta para a Direita:** Move o jogador para a direita.

## Como Gerar um Arquivo Executável (.exe)

Para criar um arquivo `.exe` que pode ser executado em computadores Windows sem a necessidade de instalar Python ou Pygame, você pode usar a ferramenta `PyInstaller`.

1.  **Instale o PyInstaller:**
    Se você ainda não o tiver, instale-o com o seguinte comando no terminal:
    ```bash
    pip install pyinstaller
    ```

2.  **Execute o PyInstaller:**
    Navegue até a pasta raiz do projeto pelo terminal. Em seguida, execute o comando abaixo. Este comando irá agrupar o jogo, juntamente com a pasta `assets`, em um único executável.

    ```bash
    pyinstaller --onefile --windowed --add-data "assets;assets" game.py
    ```
    - `--onefile`: Cria um único arquivo executável.
    - `--windowed`: Impede que uma janela de console seja aberta ao executar o jogo.
    - `--add-data "assets;assets"`: Garante que a pasta `assets` e seu conteúdo sejam incluídos no executável.

3.  **Encontre o executável:**
    Após a conclusão do processo, o PyInstaller criará uma pasta chamada `dist` no diretório do seu projeto. Dentro dela, você encontrará o arquivo `game.exe`. Este é o seu jogo, pronto para ser compartilhado e jogado!

---

**Desenvolvido por:**

- **Nome:** Vitor M M Ribeiro
- **RU:** 958318
