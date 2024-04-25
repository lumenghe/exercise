graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


def bfs(visited: list, graph: dict, node: str) -> None:
    visited = [node]
    queue = [node]
    while queue:
        checking_node = queue.pop(0)
        print(checking_node, end=" ")
        for neighbour in graph[checking_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited=[], graph=graph, node="A")
