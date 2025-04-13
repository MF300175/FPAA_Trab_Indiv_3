from functions import Graph

def create_test_graph(size):
    """
    Cria um grafo de teste com o tamanho especificado.
    
    Args:
        size (int): Número de vértices no grafo
        
    Returns:
        Graph: Um grafo de teste
    """
    g = Graph(size)
    # Adiciona arestas para criar um caminho hamiltoniano
    for i in range(size - 1):
        g.add_edge(i, i + 1)
    return g

def hamiltonian_path_wrapper(size):
    """
    Wrapper para a função hamiltonian_path que aceita apenas o tamanho do grafo.
    
    Args:
        size (int): Número de vértices no grafo
        
    Returns:
        bool: True se um caminho hamiltoniano é encontrado, False caso contrário
    """
    g = create_test_graph(size)
    return g.hamiltonian_path()

def create_complex_graph(size):
    """
    Cria um grafo mais complexo para teste.
    
    Args:
        size (int): Número de vértices no grafo
        
    Returns:
        Graph: Um grafo de teste com mais arestas
    """
    g = Graph(size)
    # Adiciona arestas para criar um grafo mais denso
    for i in range(size):
        for j in range(i + 1, size):
            if (i + j) % 2 == 0:  # Adiciona arestas alternadas
                g.add_edge(i, j)
    return g

def hamiltonian_path_complex_wrapper(size):
    """
    Wrapper para testar o algoritmo em um grafo mais complexo.
    
    Args:
        size (int): Número de vértices no grafo
        
    Returns:
        bool: True se um caminho hamiltoniano é encontrado, False caso contrário
    """
    g = create_complex_graph(size)
    return g.hamiltonian_path() 