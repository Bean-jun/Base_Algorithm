# -*- coding:UTF-8 -*-


class Tree():
    '''链表定义二叉树结构'''
    def __init__(self,root,left=None,right=None):
        self.root = root 
        self.left = left
        self.right = right

class LinkedTree():
    '''二叉树实现'''
    def __init__(self):
        self.root = None

    def add(self,data):
        '''广度优先创建一颗二叉树'''
        node = Tree(data)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left == None:
                cur_node.left = node
                return 
            else:
                queue.append(cur_node.left)
            if cur_node.right == None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        '''广度遍历-层次遍历'''
        queue = [self.root]
        if self.root == None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.root)
            if cur_node.left != None:
                queue.append(cur_node.left)
            if cur_node.right != None:
                queue.append(cur_node.right)
        
    def preorder(self,node):
        '''深度遍历-先序遍历'''
        if node == None:
            return
        print(node.root)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        '''深度遍历-中序遍历'''
        if node == None:
            return
        self.inorder(node.left)
        print(node.root)
        self.inorder(node.right)

    def postorder(self,node):
        '''深度遍历-后序遍历'''
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.root)


if __name__ == '__main__':
    tree = LinkedTree()
    tree.add('a')
    tree.add('b')
    tree.add('c')
    tree.add('d')
    tree.add('e')
    tree.add('f')
    tree.breadth_travel()
    print('~'*10)
    tree.preorder(tree.root)
    print('~'*10)
    tree.inorder(tree.root)
    print('~'*10)
    tree.postorder(tree.root)