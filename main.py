from functions import Graph
from wrapper import hamiltonian_path_wrapper, hamiltonian_path_complex_wrapper
import time
import matplotlib.pyplot as plt
import numpy as np
import threading
from functools import wraps

def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            error = []
            
            def target():
                try:
                    result.append(func(*args, **kwargs))
                except Exception as e:
                    error.append(e)
            
            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            
            if thread.is_alive():
                raise TimeoutError(f"Function execution timed out after {seconds} seconds")
            if error:
                raise error[0]
            return result[0] if result else None
        return wrapper
    return decorator

def measure_time(func, sizes, timeout_seconds=30):
    """
    Mede o tempo de execução de uma função para diferentes tamanhos de entrada.
    
    Args:
        func: Função a ser medida
        sizes (list): Lista de tamanhos de entrada
        timeout_seconds (int): Tempo máximo de execução em segundos
        
    Returns:
        list: Lista de tempos de execução
    """
    @timeout(timeout_seconds)
    def timed_func(size):
        func(size)
    
    times = []
    for size in sizes:
        print(f"Medindo tempo para tamanho {size}...")
        try:
            start_time = time.time()
            timed_func(size)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            times.append(execution_time)
            print(f"Tempo de execução: {execution_time:.2f}ms")
        except TimeoutError as e:
            print(f"Timeout após {timeout_seconds} segundos para tamanho {size}")
            times.append(float('inf'))  # Use infinity to indicate timeout
            break  # Stop testing larger sizes if we hit a timeout
        except Exception as e:
            print(f"Erro ao executar para tamanho {size}: {str(e)}")
            times.append(float('inf'))
            break
    return times

def plot_complexity(sizes, times, title):
    """
    Plota o gráfico de complexidade.
    
    Args:
        sizes (list): Lista de tamanhos de entrada
        times (list): Lista de tempos de execução
        title (str): Título do gráfico
    """
    print(f"\nGerando gráfico para {title}...")
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'b-', label='Tempo de execução')
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Tempo de execução (s)')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.savefig('complexity_analysis.png')
    plt.close()
    print(f"Gráfico salvo como 'complexity_analysis.png'")

def main():
    # Teste básico do algoritmo de Caminho Hamiltoniano
    print("Teste básico do algoritmo de Caminho Hamiltoniano:")
    
    # Teste com grafo não direcionado
    print("\n1. Teste com grafo não direcionado:")
    g1 = Graph(5, directed=False)
    g1.add_edge(0, 1)
    g1.add_edge(0, 3)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 4)
    g1.add_edge(3, 4)
    g1.hamiltonian_path()
    
    # Teste com grafo direcionado
    print("\n2. Teste com grafo direcionado:")
    g2 = Graph(5, directed=True)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 4)
    g2.add_edge(4, 0)
    g2.hamiltonian_path()
    
    # Análise de complexidade
    print("\nIniciando análise de complexidade...")
    sizes = [5, 10, 15, 20, 25]
    
    # Medir tempo para grafo simples
    print("\nMedindo tempos para grafo simples...")
    times_simple = measure_time(hamiltonian_path_wrapper, sizes)
    plot_complexity(sizes, times_simple, 'Complexidade - Grafo Simples')
    
    # Medir tempo para grafo complexo
    print("\nMedindo tempos para grafo complexo...")
    times_complex = measure_time(hamiltonian_path_complex_wrapper, sizes)
    plot_complexity(sizes, times_complex, 'Complexidade - Grafo Complexo')
    
    # Imprimir resultados
    print("\nResultados da análise de complexidade:")
    print("Tamanho\tTempo Simples\tTempo Complexo")
    for i, size in enumerate(sizes):
        print(f"{size}\t{times_simple[i]:.6f}\t{times_complex[i]:.6f}")
    
    print("\nAnálise de complexidade concluída!")

if __name__ == "__main__":
    main() 