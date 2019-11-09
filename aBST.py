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
    	place = self.FindKeyIndex(key)
    	if place is not None:
    		if place <= 0:
    			self.Tree[-place] = key
    			return -place
    		elif place < 0:
    			return place
    	else:
    		return None
