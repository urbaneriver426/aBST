class aBST:

    def __init__(self, depth):
        self.tree_size = 2 ** (depth+1) - 1
        self.Tree = [None] * self.tree_size

    def FindKeyIndex(self, key):
        i = 0
        while True:
            if i > self.tree_size - 1:
                return None
            if self.Tree[i] is None:
            	return -i
            else:
                if self.Tree[i] == key:
                        return i
                elif self.Tree[i] > key:
                        i = 2*i + 1
                else:
                        i = 2*i + 2

    def AddKey(self, key):
        if self.FindKeyIndex(key) is not None:
            if self.FindKeyIndex(key) < 0:
            	return self.FindKeyIndex(key)
            else:
            	self.Tree[self.FindKeyIndex(key)] = key
        else:
            return None
