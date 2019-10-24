import functools
import graphviz as gv
import itertools

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


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            pass
        else:
            graph.edge(*e)
            pass
        pass
    return graph


nodesA = ['A', 'B', 'C', 'D', 'E', 'F']
edgesA = [c for c in itertools.combinations(nodesA, 2)]
#edgesA = [c for c in itertools.permutations(nodesA, 2)]
g3 = add_nodes(g3, nodesA)
g3 = add_edges(g3, edgesA)
g3.render('graph\\demo59_1')

g4 = add_nodes(g4, nodesA)
g4 = add_edges(g4, edgesA)
g4.render('graph\\demo59_1_g4')