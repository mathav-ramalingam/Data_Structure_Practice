# Questions : https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
import time
class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self,property=None):
        if property == "both":
            value = self.name + "(" + self.designation + ")"
        elif property == "name":
            value = self.name
        else:
            value = self.designation

        spaces = " " * self.get_level() *3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property)


def build_management():

    team1 = TreeNode("Bavya","HR Head")
    team1.add_child(TreeNode("Ahalya","Recruitment Manager"))
    team1.add_child(TreeNode("Dharshini", "Policy Manager"))

    team2a = TreeNode("Vishwa","Infrastructure Head")
    team2a.add_child(TreeNode("Gowshik","Cloud Manager"))
    team2a.add_child(TreeNode("Ajay","App Manager"))


    team2 = TreeNode("Akashine","CTO")
    team2.add_child(TreeNode("Gowri","Application Head"))
    team2.add_child(team2a)

    head = TreeNode("Mathav","CEO")
    head.add_child(team1)
    head.add_child(team2)

    return head

if __name__ == "__main__":
    root = build_management()
    root.print_tree("both")
    print("------------------------------------------------")
    time.sleep(2)
    root.print_tree("name")
    print("------------------------------------------------")
    time.sleep(2)
    root.print_tree("")

