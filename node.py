class Node:
    def __init__(self,data, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data
        
    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
            
if __name__ == "__main__":
    root = Node(10)
    
    root.left = Node(34)
    root.right = Node(89)
    root.left.left = Node(45)
    root.left.right = Node(50)
    
    root.preorder(root)
    print("-------")
    root.postorder(root)