graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


def dfs(visited: list, graph: dict, node: str) -> None:
    if node not in visited:
        visited.append(node)
        print(f"visiting {node}")
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited=[], graph=graph, node="A")
