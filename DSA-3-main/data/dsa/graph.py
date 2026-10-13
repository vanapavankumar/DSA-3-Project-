import json


class PatentGraph:
    def __init__(self):
        self.graph = {}

    def add_patent(self, patent_id):
        if patent_id not in self.graph:
            self.graph[patent_id] = []

    def add_citation(self, patent_id, cited_patent):
        if patent_id in self.graph and cited_patent in self.graph:
            self.graph[patent_id].append(cited_patent)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            current = queue.pop(0)

            if current not in visited:
                visited.add(current)
                result.append(current)

                for neighbor in self.graph.get(current, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        result = []

        def visit(node):
            if node in visited:
                return

            visited.add(node)
            result.append(node)

            for neighbor in self.graph.get(node, []):
                visit(neighbor)

        visit(start)
        return result


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    patents = load_patents()

    graph = PatentGraph()

    for patent in patents:
        graph.add_patent(patent["patent_id"])

    for patent in patents:
        for cited in patent["citations"]:
            graph.add_citation(patent["patent_id"], cited)

    print("PATENT CITATION GRAPH")
    print("---------------------")

    for patent, citations in graph.graph.items():
        print(patent, "->", citations)

    print()
    print("BFS from P001:", graph.bfs("P001"))
    print("DFS from P001:", graph.dfs("P001"))
