# Fruit Dunk Challenge

**Vitor M M Ribeiro - RU: 958318**

## Descrição

'Fruit Dunk Challenge' é um jogo 2D desenvolvido em Python com a biblioteca Pygame. O jogador controla um jogador de basquete que deve coletar frutas que caem do céu, enquanto desvia de obstáculos. O objetivo é marcar o máximo de pontos possível.

## Instalação

Siga as instruções abaixo para configurar o ambiente e rodar o jogo.

### 1. Crie um Ambiente Virtual

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto. Abra o terminal e execute os seguintes comandos:

```bash
# Crie um ambiente virtual chamado 'venv'
python -m venv venv
```

### 2. Ative o Ambiente Virtual

- **No Windows:**
  ```bash
  .\\venv\\Scripts\\activate
  ```

- **No macOS e Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install pygame
```

## Como Jogar

Para iniciar o jogo, execute o seguinte comando no terminal:

```bash
python main.py
```

### Controles

- **Seta Esquerda:** Mover para a esquerda
- **Seta Direita:** Mover para a direita
- **Barra de Espaço:** Pular

## Como Gerar o Arquivo Executável (.exe)

Para criar um arquivo `.exe` que pode ser executado em qualquer computador Windows sem a necessidade de instalar Python ou Pygame, siga os passos abaixo.

### 1. Instale o PyInstaller

Certifique-se de que seu ambiente virtual esteja ativado e instale o PyInstaller:

```bash
pip install pyinstaller
```

### 2. Gere o Executável

Navegue até o diretório do projeto no terminal e execute o seguinte comando:

```bash
pyinstaller --onefile --windowed main.py
```

- `--onefile`: Agrupa tudo em um único arquivo executável.
- `--windowed`: Evita que uma janela de console apareça ao executar o jogo.

Após a conclusão, você encontrará o arquivo `main.exe` dentro de uma pasta chamada `dist`.
