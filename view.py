import networkx as nx
import matplotlib.pyplot as plt

def visualize_hamiltonian_path(graph, path):
    """
    Visualiza o grafo e destaca o caminho hamiltoniano encontrado.
    
    Args:
        graph: Lista de adjacência representando o grafo
        path: Lista de vértices representando o caminho hamiltoniano
    """
    # Cria um grafo direcionado
    G = nx.Graph()
    
    # Adiciona os vértices
    for i in range(len(graph)):
        G.add_node(i)
    
    # Adiciona as arestas
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    # Configura o layout do grafo
    pos = nx.spring_layout(G)
    
    # Desenha o grafo
    plt.figure(figsize=(10, 8))
    
    # Desenha os nós
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500, alpha=0.8)
    
    # Desenha as arestas
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    
    # Desenha as arestas do caminho hamiltoniano em vermelho
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                          edge_color='r', width=2)
    
    # Adiciona labels aos nós
    nx.draw_networkx_labels(G, pos, font_size=16)
    
    plt.title("Grafo com Caminho Hamiltoniano")
    plt.axis('off')
    
    # Salva a imagem
    plt.savefig('hamiltonian_path.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Exemplo de uso
    from main import Graph
    
    # Cria um grafo de exemplo
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    
    # Encontra o caminho hamiltoniano
    path = [-1] * g.V
    path[0] = 0
    g.hamiltonian_path_util(path, 1)
    
    # Visualiza o grafo e o caminho
    visualize_hamiltonian_path(g.graph, path) 