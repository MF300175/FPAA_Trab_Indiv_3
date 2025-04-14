# 🎓 Análise de Complexidade do Algoritmo de Caminho Hamiltoniano

## 📝 Descrição do Projeto

Este projeto implementa e analisa a complexidade do algoritmo de caminho hamiltoniano em grafos. Um caminho hamiltoniano é um caminho em um grafo que visita cada vértice exatamente uma vez. A implementação utiliza uma abordagem de backtracking para encontrar o caminho hamiltoniano.

### 🔍 Implementação do Algoritmo

O algoritmo implementado segue os seguintes passos:
1. Inicialização: Cria-se um grafo com n vértices
2. Backtracking: Para cada vértice não visitado:
   - Marca o vértice como visitado
   - Adiciona o vértice ao caminho atual
   - Recursivamente tenta encontrar um caminho a partir deste vértice
   - Se um caminho completo é encontrado, retorna verdadeiro
   - Se não encontra caminho, desfaz a escolha e tenta o próximo vértice
3. Verificação: Se todos os vértices foram visitados, um caminho hamiltoniano foi encontrado

## 📊 Análise Técnica

### Classes de Complexidade

O problema do Caminho Hamiltoniano pertence à classe NP-Completo. Isso pode ser justificado pelos seguintes pontos:

1. **Pertence a NP**: 
   - Uma solução pode ser verificada em tempo polinomial
   - Dado um caminho, podemos verificar em O(n) se ele visita cada vértice exatamente uma vez

2. **NP-Completo**:
   - O problema pode ser reduzido ao Problema do Caixeiro Viajante (TSP)
   - TSP é NP-Completo, e o Caminho Hamiltoniano é uma versão mais simples do TSP
   - A redução é direta: um caminho hamiltoniano existe se e somente se existe um ciclo hamiltoniano

3. **Não é P**:
   - Não existe algoritmo conhecido que resolva o problema em tempo polinomial
   - A natureza do problema requer verificação de todas as possíveis permutações de vértices

### Análise da Complexidade Assintótica

#### Complexidade Temporal
- **Pior Caso**: O(n!)
  - O algoritmo precisa verificar todas as possíveis permutações de vértices
  - Para n vértices, existem n! possíveis caminhos
  - Cada verificação de caminho requer O(n) operações

- **Caso Médio**: O(n!)
  - Mesmo no caso médio, o algoritmo precisa verificar uma fração significativa das permutações
  - A natureza do problema não permite melhorias significativas no caso médio

- **Melhor Caso**: O(n)
  - Ocorre quando o primeiro caminho tentado é hamiltoniano
  - Raramente acontece na prática

#### Método de Análise
A complexidade foi determinada através da contagem de operações:
1. Para cada vértice inicial (n escolhas)
2. Para cada vértice não visitado (n-1 escolhas)
3. Para cada vértice restante (n-2 escolhas)
4. E assim por diante até n! possibilidades

### Aplicação do Teorema Mestre

O Teorema Mestre não é aplicável neste caso porque:
1. O algoritmo não segue o padrão de divisão e conquista
2. Não há subproblemas de tamanho n/b
3. A recorrência não segue a forma T(n) = aT(n/b) + f(n)

### Impacto dos Casos de Complexidade

1. **Pior Caso (O(n!))**:
   - O algoritmo se torna impraticável para grafos com mais de 20 vértices
   - O tempo de execução cresce fatorialmente com o tamanho do grafo

2. **Caso Médio (O(n!))**:
   - Similar ao pior caso devido à natureza do problema
   - Pequenas otimizações podem reduzir o tempo de execução, mas não alteram a complexidade assintótica

3. **Melhor Caso (O(n))**:
   - Teoricamente possível, mas extremamente raro
   - Não representa o comportamento típico do algoritmo

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