# -*- coding：utf-8 -*-

class Vertex():
    '''顶点类，包含顶点信息及连接边'''
    def __init__(self,key):
        self.id = key
        self.connect = {}

    def add_neignbor(self,nbr,wight=0):
        # nbr是顶点对象所连接的另外节点，也就是顶点对象的key值
        # wight表示的权重，也就是两点之间的距离
        self.connect[nbr] = wight

    def get_connects(self):
        # 返回顶点所连接的其他点
        return [[i.id, v] for i, v in self.connect.items()]


class Graph():
    '''实现图'''
    def __init__(self):
        self.vertlist = {}
        self.count_vertex = 0

    def add_vertex(self,key):
        '''在列表中添加节点'''
        self.count_vertex += 1
        self.vertlist[key] = Vertex(key)

    def get_vertex(self,i):
        '''查找顶点'''
        return self.vertlist[i].get_connects() if i in self.vertlist else None
    
    def add_edge(self,key,nbr,wight=0):
        '''添加边'''
        if key not in self.vertlist:
            self.add_vertex(key)
        if nbr not in self.vertlist:
            self.add_vertex(nbr)
        self.vertlist[key].add_neignbor(self.vertlist[nbr],wight)
    
    def get_vertex_num(self):
        '''返回所有顶点数量'''
        return self.count_vertex


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_edge('a','b',10)
    graph.add_edge('b','a',10)
    graph.add_edge('a','c',12)
    graph.add_edge('b','c',15)
    print(graph.get_vertex_num())
    print(graph.get_vertex('a'))