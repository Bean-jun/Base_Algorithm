# 基础算法及数据结构学习

## 算法

---

### 二分搜索 Binary Search

1. [二分搜索策略](algorithm/BinarySearch.py)
2. [递归二分搜索策略](algorithm/RecursionBinarySearch.py)

### 分治 Divide Conquer

### 宽度优先搜索 Breadth Frist Search

### 广度优先搜索 Depth First Search

### 回溯法 Backtracking

### 双指针 Two Pointers

### 动态规划 Dynamic Programming

### 扫描线 Sacn-line algorithm

### 快排 Quick Sort

1. [冒泡排序](algorithm/BubbleSort.py)

---
---

## 数据结构

---

### 一、栈和队列 Stack && Queue

1. [栈](data_structure/栈.py)
    - 结构图   
    ![alt](data_structure/img/栈结构图.png)
2. [队列](data_structure/队列.py)
    - 结构图   
    ![alt](data_structure/img/队列结构图.png)
3. [双端队列](data_structure/双端队列.py)
    - 结构图   
    ![alt](data_structure/img/双端队列结构图.png)

### 二、 链表 Linked List

1. [单链表](data_structure/单链表.py)
    - 结构图   
    ![alt](data_structure/img/单链表结构图.png)
2. [单项循环链表](data_structure/单项循环链表.py)
    - 结构图   
    ![alt](data_structure/img/单项循环链表结构图.png)
3. [双向链表](data_structure/双向链表.py)
    - 结构图   
    ![alt](data_structure/img/双向链表结构图.png)

### 三、 树
1. [基础定义及相关性质内容](data_structure/doc/树.md)
    - 结构图
    ![alt](data_structure/img/树的遍历方式.png)
    - 另外可以参考浙江大学数据结构课程中关于遍历方式的图，讲的十分详细
    ![alt](data_structure/img/先中后序遍历的规则图.png)
3. [使用链表实现二叉树](data_structure/二叉树.py)   

4. 二叉查找树
    - 非空左子树的所有键值小于根节点的键值
    - 非空右子树的所有键值大于根节点的键值
    - 左右子树都是二叉查找树
5. 补充
    - 完全二叉树
        - 如果二叉树中除去最后一层节点为满二叉树，且最后一层的结点依次从左到右分布，则此二叉树被称为完全二叉树。
    - 满二叉树
        - 如果二叉树中除了叶子结点，每个结点的度都为 2，则此二叉树称为满二叉树。

### 四、 堆 Heap
1. 堆满足的条件
    - 必须是完全二叉树
    - 各个父节点必须大于或者小于左右节点，其中最顶层的根结点必须是最大或者最小的

2. 实现方式及条件
    - 使用数组实现二叉堆，例如下图的最大堆，在数组中使用[0,100,90,85,80,30,60,50,55]存储,注意上述第一个元素0仅仅是做占位;
    - 设节点位置为x，则左节点位置为2x，右节点在2x+1；已知叶子节点x，根节点为x//2;
    - 举例说明：
        - 100为根节点(位置为1)，则左节点位置为2，即90，右节点位置为3，即85；
        - 30为子节点(位置为5),则根节点为（5//2=2）,即90；

3. 根据上述条件，我们可以绘制出堆的两种形式   
   
    - [最大堆及实现](data_structure/最大堆.py)  
    ![alt](data_structure/img/最大堆.png)
       
    - [最小堆及实现](data_structure/最小堆.py)      
    ![alt](data_structure/img/最小堆.png)

### 五、 哈希表 Hash Table

### 六、 数组 Array

### 七、 并查集 Union Find

### 八、 字典树
