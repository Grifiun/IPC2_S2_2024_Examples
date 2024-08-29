from node.node import Node

class ListNode:
    def __init__(self, x=1):
        self.root = None
        self.x = x

    def create_node(self, y):
        return Node(id=f"node_{self.x}_{y}", text=f"({self.x}, {y})", x=self.x, y=y)

    def create_list_n_nodes(self, size):
        head = None
        current = None
        for y in range(0 + 1, size + 1):
            new_node = self.create_node(y)
            if head is None:
                head = new_node
                self.root = head
            else:
                current.set_next(new_node)
            current = new_node

        return head
    
    def generate_graphviz_code_list(self):
        string_graphviz_list = ''
        # Iterate over nodes in the list and generate the Graphviz code

        for node_aux in self.root:
            string_graphviz_list += f'    {node_aux.id} [pos="{node_aux.x},{node_aux.y}!", label="{node_aux.text}"];\n'

            # Connect nodes within the same list (left-to-right)
            if node_aux.next != None:
                string_graphviz_list += f' {node_aux.id + " -> " + node_aux.next.id} [constraint=false];\n'

        return string_graphviz_list

class GraphCode:
    def __init__(self):
        pass

    def generate_code_node_list(self, lista1, lista2, lista3):
        graph_code = 'digraph G {\n'
        graph_code += 'graph [layout=fdp]\n'
        graph_code += '    rankdir=TB;\n'
        graph_code += '    node [shape=box];\n\n'

        # Generate nodes for each list (row by row)
        if lista1.root is not None:
            graph_code += lista1.generate_graphviz_code_list()
        if lista2.root is not None:
            graph_code += lista2.generate_graphviz_code_list()
        if lista3.root is not None:
            graph_code += lista3.generate_graphviz_code_list()
        
        graph_code += '}\n'
        return graph_code

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
        graph_code = graph_code_generator.generate_code_node_list(self.list1, self.list2, self.list3)
        print(graph_code)

if __name__ == "__main__":
    main = Main()
    main.run()
