# Prática server/client API

Um script em Python para realizar troca de informação entre servidor e cliente

## Estrutura do Projeto

| Diretório / Arquivo | Descrição |
| :--- | :--- |
| **src/steamWS/** | **Submódulo git para funcionamento do servidor.** |
| **src/client/** | **Funcionalidades do cliente.** |
| **src/server/** | **Funcionalidades do servidor.** |

## Como Executar

### 1. Pré-requisitos
* **Python 3.10** ou superior.

### 2. Instalação
1. Clone o repositório para sua máquina:
```bash
git clone --recurse-submodules https://github.com/FilipyTav/APIs-practice/
cd APIs-practice
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

- Windows:
```bash
venv\Scripts\activate
```

- Linux:
```bash
source venv/bin/activate
```

3. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

### 3. Execução
Comece o servidor:
```bash
fastapi dev src/server/app/main.py
```

Execute o cliente:
```bash
python src/client/main.py
```
