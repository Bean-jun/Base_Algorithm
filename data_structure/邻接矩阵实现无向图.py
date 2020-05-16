# -*- coding：utf-8 -*-

class Graph():
    '''实现图'''
    def __init__(self):
        self.start = []
        self.wight = [None]
        self.count_vertex = 0

    def add_vertex(self,key):
        '''添加顶点'''
        self.start.append(key)
        self.count_vertex += 1
        if self.count_vertex > 1:
            temp_list = [None]*(2*self.count_vertex-1)
            for i in temp_list:
                self.wight.append(i)

    def add_edge(self,key,nbr,wight=None):
        '''添加边'''
        if key not in self.start:
            self.add_vertex(key)
        if nbr not in self.start:
            self.add_vertex(nbr)
        for i in self.start:
            if key == i:
                index_01 = self.start.index(i) + 1
            if nbr == i:
                index_02 = self.start.index(i) + 1
        self.wight[index_01*index_02-1] = wight

    def get_vertex_num(self):
        '''返回所有顶点数量'''
        return self.count_vertex
    
    def get_vertex(self,i):
        '''查找顶点及相应边'''
        for n in self.start:
            new_val = [i]
            if i == n:
                if self.start.index(n) != 0:
                    for index,val in enumerate(self.wight):
                        if (index+1) % (self.start.index(n)+1) == 0:
                            if val != None:
                                temp = self.start[(index+1) // (self.start.index(n)+1)-1]
                                new_val.append([temp,val]) 
                    return new_val
                elif self.start.index(n) == 0:
                    new_list = self.wight[:self.count_vertex]
                    for i in new_list:
                        if i != None:
                            new_val.append([self.start[new_list.index(i)],i])
                    return new_val


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_edge('a','b',10)
    graph.add_edge('a','c',12)
    graph.add_edge('b','c',15)
    graph.add_edge('b','d',15)
    print(graph.get_vertex_num())
    print(graph.get_vertex('a'))