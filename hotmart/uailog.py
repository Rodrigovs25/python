import heapq

def dijkstra(graph, start, end):
    # Min-heap to store the nodes and their distances
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == end:
            return current_distance
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return float('infinity')

# Converting the list of edges into an adjacency list
edges = [('Y', 'B', 2), ('F', 'X', 10), ('J', 'R', 8), ('Y', 'Z', 8), ('Z', 'R', 14), ('B', 'J', 4), ('H', 'Z', 1), 
         ('H', 'Z', 10), ('F', 'B', 12), ('F', 'Z', 15), ('R', 'X', 4), ('Y', 'X', 17), ('J', 'F', 8), ('Y', 'Z', 4), 
         ('H', 'Y', 19), ('J', 'F', 17), ('F', 'J', 18), ('F', 'X', 20), ('J', 'F', 16), ('Z', 'H', 3)]

graph = {}
for edge in edges:
    u, v, w = edge
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))

start = 'Z'
end = 'B'
result = dijkstra(graph, start, end)
print(f"Menor distância: {result}")
