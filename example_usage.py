from client import GraphDAGAnalyzer

def run_example():
    print("=== GenPark DAG Dependency Analyzer Example ===")
    analyzer = GraphDAGAnalyzer()
    print("Topological Order:", analyzer.benchmark_topological_analysis())

if __name__ == "__main__":
    run_example()
