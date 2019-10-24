import functools
import graphviz as gv

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            pass
        else:
            graph.node(n)
            pass
    return graph


nodesA = ['A', 'B', 'D',(4,5), 'C', 'E', 'F']
g3 = add_nodes(g3, nodesA)
g3.render('graph\\demo59')