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
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return
        else:
            if self.size_of(b_root) > self.size_of(a_root): 
                self.parent[a_root] = self.parent[b_root]
                self.size[b_root] += self.size[a_root]
            else:
                self.parent[b_root] = self.parent[a_root]
                self.size[a_root] += self.size[b_root]
                
    def size_of(self,a):
        return self.size[self.find(a)]
    
    def is_same(self,a,b):
        return self.find(a) == self.find(b)


N,M,K = map(int, input().split())
uf = UnionFind(N+1)
friends = []
blocks = [0]*(N+1)
for i in range(N+1):
    blocks.append([])
    friends.append(0)

for i in range(M):
    a,b = map(int, input().split())
    friends[a] += 1
    friends[b] += 1
    uf.unite(a,b)
    

for j in range(K):
    x,y = map(int, input().split())
    if uf.is_same(x,y):
        blocks[x] += 1
        blocks[y] += 1

for i in range(1,N+1):
    print(uf.size_of(i) - friends[i] - blocks[i] -1)