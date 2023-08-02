
# 1:Implement Binary tree

from binarytree import Node
root = Node(3)
root.left = Node(6)
root.right = Node(8)
print('Binary tree :', root)
print('List of nodes :', list(root))
print('Inorder of nodes :', root.inorder)
print('Size of tree :', root.size)
print('Height of tree :', root.height)
print('Properties of tree : \n', root.properties)


# 2:Find height of a given tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def maxDepth(node):
    if node is None:
        return 0
 
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Height of tree is %d" % (maxDepth(root)))


# 3:Perform Pre-order, Post-order, In-order traversa

INorder

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def printInorder(root):
 
    if root:
        printInorder(root.left)
        print(root.val, end=" "),
        printInorder(root.right)
 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traversal of binary tree is")
    printInorder(root)

PRE Order
def printPreorder(root):
 
    if root:
        print(root.val, end=" "),
        printPreorder(root.left)
        printPreorder(root.right)
 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is")
    printPreorder(root)

POST Order

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" "),
 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Postorder traversal of binary tree is")
    printPostorder(root)

# 4:Function to print all the leaves in a given binary tree    
class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root: Node) -> None:
    if (not root):
        return

    if (not root.left and
        not root.right):
        print(root.data,
              end = " ")
        return

    if root.left:
        printLeafNodes(root.left)
    if root.right:
        printLeafNodes(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
    printLeafNodes(root)


# 5:Implement BFS Breath First Search and DFS Depth First Search
BFS:
from collections import defaultdict
 
class Graph:
    def __init__(self):
 
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)
        queue = []
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            print(s, end=" ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
 
if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)

#DFS:
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()

def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')



# 6:Find sum of all left leaves in a given Binary Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def leftLeavesSumRec(root, isLeft, summ):
    if root is None:
        return

    if root.left is None and root.right is None and isLeft == True:
        summ[0] += root.key
 
    leftLeavesSumRec(root.left, 1, summ)
    leftLeavesSumRec(root.right, 0, summ)
     
def leftLeavesSum(root):
    summ = [0] 
    leftLeavesSumRec(root, 0, summ)
     
    return summ[0]

root = Node(20);
root.left= Node(9);
root.right   = Node(49);
root.right.left = Node(23);
root.right.right= Node(52);
root.right.right.left  = Node(50);
root.left.left  = Node(5);
root.left.right = Node(12);
root.left.right.right  = Node(12);
 
print ("Sum of left leaves is", leftLeavesSum(root))


# 7:Find sum of all nodes of the given perfect binary tree

def SumNodes(l):
    leafNodeCount = pow(2, l - 1)
    vec = [[] for i in range(l)]

    for i in range(1, leafNodeCount + 1):
        vec[l - 1].append(i)
 
    for i in range(l - 2, -1, -1):
        k = 0
        while (k < len(vec[i + 1]) - 1):
 
            vec[i].append(vec[i + 1][k] +
                          vec[i + 1][k + 1])
            k += 2
 
    Sum = 0

    for i in range(l):
        for j in range(len(vec[i])):
            Sum += vec[i][j]
 
    return Sum
 
if __name__ == '__main__':
    l = 3
    print(SumNodes(l))


# 8:Count subtress that sum up to a given value x in a binary tree

 
class getNode:
    def __init__(self, data):
 
        self.data = data
        self.left = self.right = None

 
def countSubtreesWithSumX(root, count, x):
 
    if (not root):
        return
    ls = countSubtreesWithSumX(root.left,
                               count, x)
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    Sum = ls + rs + root.data
    if (Sum == x):
        count[0] += 1
    return Sum


def countSubtreesWithSumXUtil(root, x):
    if (not root):
        return 0
 
    count = [0]

    ls = countSubtreesWithSumX(root.left,
                               count, x)
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    if ((ls + rs + root.data) == x):
        count[0] += 1
 
    return count[0]
 
if __name__ == '__main__':
 
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)
 
    x = 7
 
    print("Count =",
          countSubtreesWithSumXUtil(root, x))


# 9:Find maximum level sum in Binary Tree

from collections import deque
class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None
def maxLevelSum(root):
    if (root == None):
        return 0
    result = root.data
    q = deque()
    q.append(root)
     
    while (len(q) > 0):
         
        count = len(q)
 
        sum = 0
        while (count > 0):
            
            temp = q.popleft()
            sum = sum + temp.data

            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
                 
            count -= 1   
        result = max(sum, result)
 
    return result
if __name__ == '__main__':
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
 
    print("Maximum level sum is", maxLevelSum(root))


# 10:Print the nodes at odd levels of a tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
    if (root == None):
        return
    if (isOdd):
        print(root.data, end = " ")
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)