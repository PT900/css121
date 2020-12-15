# DFS algorithm

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Set graph with adjajency matrix
graph = {'0': set(['1', '2', '3']),
         '1': set(['0', '4']),
         '2': set(['0', '5', '6']),
         '3': set(['0']),
         '4': set(['1']),
         '5': set(['2', '7']),
         '6': set(['2']),
         '7': set(['5'])
         }

dfs(graph, '0')