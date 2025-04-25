'''
Sabendo que a relação entre vértices, arestas e faces de um objeto geométrico é dada pela 
fórmula: vértices + faces = arestas + 2, calcule o número de vértices de um cubo (6 faces 
e 12 arestas).
'''

def vertices_cubo():
    faces = 6
    arestas = 12
    vertices = arestas + 2 - faces
    print(vertices)

vertices_cubo()