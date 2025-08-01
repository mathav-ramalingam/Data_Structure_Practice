class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces  + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_value(self):
        print(self.data)
        print(self.children[1].children[0].data)


def build_product_tree():
    root = TreeNode("RV Groups")

    farms = TreeNode("Farms")
    farms.add_child(TreeNode("Karur"))
    farms.add_child(TreeNode("Coimbatore"))
    farms.add_child(TreeNode("Thanjavur"))

    electonics = TreeNode("Electronics")
    electonics.add_child(TreeNode("Mobile"))
    electonics.add_child(TreeNode("Laptops"))

    moto = TreeNode("Motors")
    moto.add_child(TreeNode("Bike"))
    moto.add_child(TreeNode("Cars"))

    root.add_child(farms)
    root.add_child(electonics)
    root.add_child(moto)


    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    root.print_value()