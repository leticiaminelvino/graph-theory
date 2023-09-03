class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

def dfs(graph, origin):
    visited = set()
    stack = Stack()
    stack.push(origin)

    while not stack.isEmpty():
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            
            for neighbor in graph[vertex] - visited:
                stack.push(neighbor)

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

#grafo e vertice de origem
dfs(graph, '0')