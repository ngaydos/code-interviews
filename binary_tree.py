#creates a binary tree that optimizes searching
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add(self, new):
        if new > self.value:
            if self.right is None:
                self.right = Node(new)
            else:
                self.right.add(new)
        if new < self.value:
            if self.left is None:
                self.left = Node(new)
            else:
                self.left.add(new)
    def search(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search(target)