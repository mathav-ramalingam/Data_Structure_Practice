class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,val):
        if self.data == val:
            return

        #left subtree
        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTree(val)

        #right subtree
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTree(val)


    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def max_val(self):
        if not self.right:
            return self.data
        return self.right.max_val()

    def min_val(self):
        if not self.left:
            return self.data
        return self.left.min_val()


    def calculateSum(self):
        left_sum = self.left.calculateSum() if self.left else 0
        right_sum = self.right.calculateSum() if self.right else 0

        return self.data + left_sum +right_sum
    def inOrderTraversal(self):
        element = []

        if self.left:
            element += self.left.inOrderTraversal()


        element.append(self.data)

        if self.right:
            element += self.right.inOrderTraversal()

        return element

    def preOrder(self):
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.preOrder()

        if self.right:
            element += self.right.preOrder()

        return element

    def postOrder(self):
        element = []

        if self.left:
            element += self.left.postOrder()

        if self.right:
            element += self.right.postOrder()

        element.append(self.data)

        return element


def build_tree(num):
    root = BinarySearchTree(num[0])

    for i in range(1,len(num)):
        root.add_child(num[i])

    return root

if __name__ == "__main__":
    # num = [4,17,52,64,81,2,16,32,28,1,9,16]
    num = [9,10,7,8,3]
    tree = build_tree(num)
    print(f"value 11 is in the tree: {tree.search(11)}")
    print(f"Max Value in the tree: {tree.max_val()}")
    print(f"Min Value in the tree: {tree.min_val()}")
    print(f"Sum of Values in the tree: {tree.calculateSum()}")
    print(f"Inorder : {tree.inOrderTraversal()}")
    print(f"PreOder: {tree.preOrder()}")
    print(f"PostOrder: {tree.postOrder()}")