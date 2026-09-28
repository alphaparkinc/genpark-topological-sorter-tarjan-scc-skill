from collections import deque
from typing import Dict, List, Any

class GraphDAGAnalyzer:
    @staticmethod
    def topological_sort(graph: Dict[str, List[str]]) -> Dict[str, Any]:
        in_degree = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                in_degree[v] = in_degree.get(v, 0) + 1
        queue = deque([u for u in in_degree if in_degree[u] == 0])
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in graph.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        has_cycle = len(order) != len(graph)
        return {"has_cycle": has_cycle, "topological_order": order if not has_cycle else []}

    def benchmark_topological_analysis(self) -> Dict[str, Any]:
        dag = {"Build": ["Test"], "Test": ["Package", "Lint"], "Package": ["Deploy"], "Lint": [], "Deploy": []}
        return self.topological_sort(dag)
