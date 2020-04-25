class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self,a):
        if self.parent[a] == a:
            return a
        else:
            return self.find(self.parent[a])

    def unite(self,a,b):
        a_parent = self.parent[a]
        b_parent = self.parent[b]
        if a_parent == b_parent:
            return
        else:
            if self.size_of(a_parent) > self.size_of(b_parent):
                self.parent[b_parent] = self.parent[a_parent]
            elif self.size_of(b_parent) > self.size_of(a_parent): 
                self.parent[a_parent] = self.parent[b_parent]
            else:
                self.parent[b_parent] = self.parent[a_parent]
                self.size[a_parent] += 1
                print(self.size)
                print(self.parent)
                
    def size_of(self,a):
        return self.size[self.parent[a]]
    
    def is_same(self,a,b):
        return self.parent(a) == self.parent(b)