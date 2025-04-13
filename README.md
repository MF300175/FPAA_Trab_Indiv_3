# Análise de Complexidade do Algoritmo de Caminho Hamiltoniano

Este projeto implementa e analisa a complexidade do algoritmo de caminho hamiltoniano em grafos.

## Funcionalidades

- Implementação do algoritmo de caminho hamiltoniano
- Análise de complexidade para grafos simples e complexos
- Visualização gráfica dos resultados
- Sistema de timeout para evitar execuções muito longas

## Estrutura do Projeto

- `functions.py`: Implementação do algoritmo de caminho hamiltoniano
- `wrapper.py`: Funções wrapper para testes
- `main.py`: Script principal com análise de complexidade
- `complexity_analysis.png`: Gráfico com resultados da análise

## Como Executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o script principal:
```bash
python main.py
```

## Resultados

O projeto gera um gráfico de complexidade mostrando:
- Tempo de execução para grafos simples
- Tempo de execução para grafos complexos
- Análise da complexidade do algoritmo

## Complexidade

- Grafos Simples: Complexidade praticamente constante
- Grafos Complexos: Complexidade fatorial O(n!) 