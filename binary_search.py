
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

COUNT=[10]

class BST :
    def __init__(self):
        self.root = None

    def insert_root(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self.insert(self.root,value)

    def insert(self,root,value): #O(h)
        if root is None:
            return Node(value)
        else :
            if value < root.value :
                root.left = self.insert(root.left,value)
            else :
                root.right = self.insert(root.right , value)
        
        return root

    def search(self,value):
        if value in self.inorder_traversal(self.root):
            print("value exist")
        else :
            print("value doesn't exist")   


    def delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                print("one child deleted")
                return node.right
            elif node.right is None:
                print("one child deleted")
                return node.left
            else:
                # Node has two children
                curr = self.find_min(node.right)
                node.value = curr.value
                node.right = self.delete(node.right, curr.value)
        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    def inorder_traversal(self, root):#time comp = O(N) / N : the number of nodes
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.value)
            result = result + self.inorder_traversal(root.right)
        return result 


    def preorder_traversal(self, root):#time comp = O(N) / N : the number of nodes
        result = []
        if root:
            result.append(root.value)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result
    
    def postorder_traversal(self, root):#time comp = O(N) / N : the number of nodes
        result = []
        if root:
            result = self.postorder_traversal(root.left)
            result = result + self.postorder_traversal(root.right)
            result.append(root.value)
        return result
    

    def print2DUtil(self,root, space):

        # Base case
        if (root == None):
            return
    
        # Increase distance between levels
        space += COUNT[0]
    
        # Process right child first
        self.print2DUtil(root.right, space)
    
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.value)
    
        # Process left child
        self.print2DUtil(root.left, space)
 
    def print2D(self,root):
    
        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(root, 0)

binary_search = BST()

binary_search.insert_root(10)
binary_search.insert(binary_search.root,5)
binary_search.insert(binary_search.root,20)
binary_search.insert(binary_search.root,6)
binary_search.insert(binary_search.root,55)
binary_search.insert(binary_search.root,23)
binary_search.insert(binary_search.root,15)

binary_search.search(55)
binary_search.search(660)
binary_search.print2D(binary_search.root)
print("inorder traversal" , binary_search.inorder_traversal(binary_search.root))
print("preorder traversal" , binary_search.preorder_traversal(binary_search.root))
print("postorder traversal" , binary_search.postorder_traversal(binary_search.root))

binary_search.delete(binary_search.root,15)
print("inorder traversal" , binary_search.inorder_traversal(binary_search.root))

binary_search.print2D(binary_search.root)
