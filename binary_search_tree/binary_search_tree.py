class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if self.right is None and self.left is None:
            return False
        else:
            if self.left is not None:
                if self.left.contains(target):
                    return True
            if self.right is not None:
                if self.right.contains(target):
                    return True
        return False

    def get_max(self):
        max = self.value
        if self.right is None:
            return max
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
