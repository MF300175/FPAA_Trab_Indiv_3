# 🎓 Análise de Complexidade do Algoritmo de Caminho Hamiltoniano

## 📝 Descrição do Projeto

Este projeto implementa e analisa a complexidade do algoritmo de caminho hamiltoniano em grafos.

## ✨ Funcionalidades

* 🔍 Implementação do algoritmo de caminho hamiltoniano
* 📊 Análise de complexidade para grafos simples e complexos
* 📈 Visualização gráfica dos resultados
* ⏱️ Sistema de timeout para evitar execuções muito longas

## 📁 Estrutura do Projeto

* `functions.py`: Implementação do algoritmo de caminho hamiltoniano
* `wrapper.py`: Funções wrapper para testes
* `main.py`: Script principal com análise de complexidade
* `complexity_analysis.png`: Gráfico com resultados da análise

## 🚀 Como Executar

### 📋 Pré-requisitos
* Python 3.8 ou superior
* pip (gerenciador de pacotes Python)

### 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. (Recomendado) Crie um ambiente virtual:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Atualize as ferramentas básicas:
```bash
python -m pip install --upgrade pip setuptools wheel
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### ▶️ Execução

Execute o script principal:
```bash
python main.py
```

### ⚠️ Solução de Problemas

Se você encontrar erros durante a instalação:

1. Certifique-se de que o Python está instalado corretamente:
```bash
python --version
```

2. Se o comando acima falhar, você pode precisar adicionar o Python ao PATH do sistema ou usar o caminho completo:
```bash
# Windows (exemplo)
C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python3x\python.exe -m pip install -r requirements.txt
```

3. Se encontrar problemas com as dependências, tente instalar cada pacote individualmente:
```bash
pip install networkx==3.1
pip install matplotlib==3.7.1
pip install numpy==1.24.3
```

## 📊 Resultados

O projeto gera um gráfico de complexidade mostrando:
* ⏱️ Tempo de execução para grafos simples
* ⏱️ Tempo de execução para grafos complexos
* 📈 Análise da complexidade do algoritmo

## 🔍 Complexidade

* 📈 Grafos Simples: Complexidade praticamente constante
* 📉 Grafos Complexos: Complexidade fatorial O(n!) 