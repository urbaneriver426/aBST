class aBST:

        def __init__(self, depth):
                self.tree_size = 2 ** (depth+1) - 1
                self.Tree = [None] * self.tree_size
	
        def FindKeyIndex(self, key):
                i = 0
                while True:
                        if i > self.tree_size - 1 or self.Tree[i] is None:
                                return None
                        else:
                                if self.Tree[i] == key:
                                        return i
                                elif self.Tree[i] > key:
                                        i = 2*i + 1
                                else:
                                        i = 2*i + 2

        def AddKey(self, key):
                if self.FindKeyIndex(key) is not None:
                        return self.FindKeyIndex(key)
                else:
                        i = 0
                        while True:
                                if i > self.tree_size - 1:
                                        return -1
                                else:
                                        if self.Tree[i] is None:
                                                self.Tree[i] = key
                                                return i
                                        elif self.Tree[i] > key:
                                                i = 2*i + 1
                                        else:
                                                i = 2*i + 2
