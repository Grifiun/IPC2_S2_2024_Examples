from node.node import Node
from graphviz import Digraph
# pip install graphviz

class ListNode:
    def __init__(self, x=1):
        self.root = None
        self.x = x

    def create_node(self, y):
        return Node(id=f"node_{self.x}_{y}", text=f"({self.x}, {y})", x = self.x, y = y)

    def create_list_n_nodes(self, amount):
        head = None
        current = None
        for y in range(1, amount + 1):
            new_node = self.create_node(y)
            if head is None:
                head = new_node
                self.root = head
            else:
                current.set_next(new_node)
            current = new_node
        return head
    
    def generate_graphviz_code_list(self, dot):
        # Iterate over nodes in the list and add them to the Graphviz dot object
        for node_aux in self.root:
            dot.node(node_aux.id, label=node_aux.text)

            # Connect nodes within the same list (left-to-right)
            if node_aux.next is not None:
                dot.edge(node_aux.id, node_aux.next.id, constraint='false')

class GraphCode:
    def __init__(self):
        pass

    def generate_code_node_list(self, lista1, lista2, lista3):
        dot = Digraph(comment='Graph Representation')
        dot.attr(rankdir='TB')
        dot.attr('node', shape='box')

        # Generate nodes for each list (row by row)
        if lista1.root is not None:
            lista1.generate_graphviz_code_list(dot)
        if lista2.root is not None:
            lista2.generate_graphviz_code_list(dot)
        if lista3.root is not None:
            lista3.generate_graphviz_code_list(dot)
        
        return dot

class Main:
    def __init__(self):
        self.list1 = ListNode(1)
        self.list1.create_list_n_nodes(5)
        self.list2 = ListNode(2)
        self.list2.create_list_n_nodes(4)
        self.list3 = ListNode(3)
        self.list3.create_list_n_nodes(3)

    def run(self):
        graph_code_generator = GraphCode()
        dot = graph_code_generator.generate_code_node_list(self.list1, self.list2, self.list3)
        #dot.render('output_graph', format='png', cleanup=True)
        # Muestra el código generado en formato DOT (opcional)
        print(dot.source)

if __name__ == "__main__":
    main = Main()
    main.run()
