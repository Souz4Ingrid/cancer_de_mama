
# | Classificador de Câncer de Mama com Inteligência Artificial

Bem-vindo ao projeto! Esta é uma aplicação web simples e poderosa que utiliza **Machine Learning** (Aprendizado de Máquina) para prever se um tumor de mama é **Benigno** ou **Maligno** com base em dados clínicos.

A aplicação utiliza **Python**, **Flask** (para o site) e **Scikit-Learn** (para a inteligência artificial).

---

## | Estrutura do Projeto

Certifique-se de que sua pasta esteja organizada desta maneira para que tudo funcione:

```text
ClassificadorCancerDeMama/
│
├── static/                  # (Opcional, se houver arquivos CSS/JS extras)
├── templates/
│   └── index.html           # A página do site
│
├── app.py                   # O código que roda o site (Servidor Flask)
├── data.csv                 # Os dados usados para ensinar a IA
├── modelo_cancer_mama.pkl   # O cérebro da IA (gerado pelo treinamento)
├── requirements.txt         # Lista de ferramentas necessárias
├── treinamento.py           # Código que ensina a IA a classificar
└── README.md                # Este arquivo
````

-----

## | Passo 1: Instalação do Python

Antes de tudo, você precisa ter o Python instalado no seu computador.

### | Windows

1.  Acesse o site oficial: [python.org](https://www.python.org/downloads/).
2.  Baixe a versão mais recente.
3.  **MUITO IMPORTANTE:** Na tela de instalação, marque a caixinha **"Add Python to PATH"** antes de clicar em "Install Now".

### | Linux (Ubuntu/Debian)

Abra o seu terminal e digite:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

-----

## | Passo 2: Configurando o Ambiente

Agora vamos preparar o terreno para o código rodar. Abra o seu **Prompt de Comando (CMD)**, **PowerShell** ou **Terminal**.

### | No Windows

1.  **Entre na pasta do projeto:**
    Digamos que você baixou a pasta em "Downloads". Digite:

    ```cmd
    cd Downloads\ClassificadorCancerDeMama
    ```

2.  **Crie um ambiente virtual (uma caixa de areia para o projeto):**

    ```cmd
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    ```cmd
    venv\Scripts\activate
    ```

    *(Se aparecer `(venv)` no começo da linha do terminal, funcionou\!)*

4.  **Instale as ferramentas necessárias:**

    ```cmd
    pip install -r requirements.txt
    ```

### | No Linux

1.  **Entre na pasta do projeto:**

    ```bash
    cd ~/Downloads/ClassificadorCancerDeMama
    ```

    *(Ajuste o caminho conforme onde você salvou a pasta)*

2.  **Crie um ambiente virtual:**

    ```bash
    python3 -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    ```bash
    source venv/bin/activate
    ```

4.  **Instale as ferramentas necessárias:**

    ```bash
    pip install -r requirements.txt
    ```

-----

## | Passo 3: Treinando a IA (Opcional)

O projeto já vem com um modelo pronto (`modelo_cancer_mama.pkl`). Porém, se você quiser "ensinar" a IA novamente do zero usando o arquivo `data.csv`:

1.  Certifique-se de que o ambiente virtual está ativado.
2.  Rode o comando:
    ```bash
    python treinamento.py
    ```
3.  Se aparecer a mensagem *"Sucesso\! Arquivo gerado: ... modelo\_cancer\_mama.pkl"*, sua IA está nova em folha\!

-----

## | Passo 4: Rodando o Site

Agora é a hora da verdade. Vamos colocar o site no ar.

1.  No terminal (com o ambiente ativado), digite:

    ```bash
    python app.py
    ```

2.  Você verá uma mensagem parecida com esta:

    ```text
    * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

3.  Abra o seu navegador (Chrome, Edge, Firefox) e digite o endereço:
    **https://www.google.com/url?sa=E\&source=gmail\&q=http://127.0.0.1:5000**

-----

## | Como Usar

1.  Ao abrir o site, você verá um formulário com vários campos médicos.
2.  Você pode digitar os valores manualmente se tiver um exame em mãos.
3.  Para testar rapidamente, clique nos botões de exemplo no topo da página:
      - **Preencher Caso Maligno**: Preenche com dados de um tumor perigoso.
      - **Preencher Caso Benigno**: Preenche com dados de um tumor seguro.
4.  Clique em **CLASSIFICAR DIAGNÓSTICO**.
5.  A IA dirá se o resultado é **BENIGNO** (🟩) ou **MALIGNO** (🟥).

-----

## | Solução de Problemas Comuns

  * **Erro: "python não é reconhecido..."**
      * No Windows, você provavelmente esqueceu de marcar "Add Python to PATH" na instalação. Reinstale o Python e marque essa opção.
  * **Erro: "Module not found"**
      * Você esqueceu de ativar o ambiente virtual ou de rodar o `pip install -r requirements.txt`.
  * **Erro: "Modelo não encontrado" ao abrir o site**
      * O arquivo `modelo_cancer_mama.pkl` sumiu. Rode o comando `python treinamento.py` para criar um novo.

-----


