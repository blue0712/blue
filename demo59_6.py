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
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
            pass
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
            pass
        pass
    return graph


nodesA = ['A', 'B', 'C', 'D', 'E', 'F']
# edgesA = [c for c in itertools.combinations(nodesA, 2)]
edgesA = [c for c in itertools.permutations(nodesA, 2)]
g3 = add_nodes(g3, nodesA)
g3 = add_edges(g3, edgesA)
g3.render('graph\\demo59_6')

nodesB = [('A', {'label': 'Nissan'}), ('B', {'label': 'Toyota'}),
          ('C', {'label': 'Lexus'}), ('D', {'label': 'Ford'}),
          ('E', {'label': 'Luxgen'})]
edgesB = [(('A', 'B'), {'label': 'japan popular brand'}),
          (('A', 'C'), {'label': 'same company'}),
          (('B', 'D'), {'label': 'F1 racer'}),
          (('B', 'E'), {'label': 'electric gadget'})]
g4 = add_nodes(g4, nodesB)
g4 = add_edges(g4, edgesB)
g4.render('graph\\demo59_6_g4')

styles = {'graph': {'label': '國產車市場',
                    'fontsize': '24',
                    'fontcolor': '#444444',
                    'bgcolor': '#C0FFEE',
                    'rankdir': 'LR',  # TB,BT,LR, RL
                    'fillcolor': '#C0EEFF'},
          'nodes': {'fontname': 'Consolas',
                    'shape': 'box',
                    'fontcolor': 'blue',
                    'color': 'gray',
                    'style': 'filled',
                    'fillcolor': '#FFC0EE'},
          'edges': {
              'style': 'dotted',
              'color': '#004466',
              'arrowhead': 'open',
              'fontname': 'Courier',
              'fontsize': '24',
              'fontcolor': '#880000'
          }}


def apply_styles(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    graph.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return graph


g5 = apply_styles(g4, styles)
g5.render('graph\\demo59_6_g5')