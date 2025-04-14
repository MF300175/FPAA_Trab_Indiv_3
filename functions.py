class Graph:
    def __init__(self, vertices, directed=False):
        """
        Inicializa um grafo com o número especificado de vértices.
        
        Args:
            vertices (int): Número de vértices no grafo
            directed (bool): Se True, o grafo é direcionado. Se False, é não direcionado
        """
        self.V = vertices
        self.directed = directed
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def add_edge(self, u, v):
        """
        Adiciona uma aresta entre os vértices u e v.
        
        Args:
            u (int): Vértice de origem
            v (int): Vértice de destino
        """
        self.graph[u][v] = 1
        if not self.directed:  # Para grafos não direcionados
            self.graph[v][u] = 1
    
    def is_safe(self, v, pos, path):
        """
        Verifica se um vértice pode ser adicionado ao caminho.
        
        Args:
            v (int): Vértice a ser verificado
            pos (int): Posição atual no caminho
            path (list): Caminho atual
            
        Returns:
            bool: True se o vértice pode ser adicionado, False caso contrário
        """
        # Verifica se o vértice é adjacente ao último vértice no caminho
        if self.graph[path[pos-1]][v] == 0:
            return False
        
        # Verifica se o vértice já está no caminho
        for vertex in path:
            if vertex == v:
                return False
        return True
    
    def hamiltonian_path_util(self, path, pos):
        """
        Função recursiva que implementa o backtracking para encontrar o caminho hamiltoniano.
        
        Args:
            path (list): Lista que armazena o caminho atual
            pos (int): Posição atual no caminho
            
        Returns:
            bool: True se um caminho hamiltoniano é encontrado, False caso contrário
        """
        # Caso base: se todos os vértices estão incluídos no caminho
        if pos == self.V:
            return True
        
        # Tenta diferentes vértices como próximo candidato no caminho
        for v in range(self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                
                if self.hamiltonian_path_util(path, pos + 1):
                    return True
                
                # Se não leva a uma solução, remove o vértice
                path[pos] = -1
        
        return False
    
    def hamiltonian_path(self):
        """
        Função principal que inicia a busca pelo caminho hamiltoniano.
        
        Returns:
            bool: True se um caminho hamiltoniano é encontrado, False caso contrário
        """
        # Inicializa o caminho com -1
        path = [-1] * self.V
        
        # Começa com o primeiro vértice
        path[0] = 0
        
        if not self.hamiltonian_path_util(path, 1):
            print("Não existe um Caminho Hamiltoniano")
            return False
        
        print("Caminho Hamiltoniano encontrado:")
        for vertex in path:
            print(vertex, end=" ")
        print()
        return True 