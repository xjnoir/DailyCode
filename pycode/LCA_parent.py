'''
Find LCA(Lowest Common Ancestor) of two nodes 
in a Tree with parent pointer
'''
class Solution(object):
    # method1, using hashset
    def LCA1(self, A, B):
        if not A or not B:
            return None
        visit = set([])
        p1, p2 = A, B
        while p1.parent:
            visit.add(p1)
            p1 = p1.parent
        while p2.parent:
            if p2 in visit:
                return p2
            p2 = p2.parent
        
        return None

    # method2, without hashset
    def LCA2(self, A, B):
        if not A or not B:
            return None
        h1 = self.findheight(A)
        h2 = self.findheight(B)
        p1, p2 = A, B
        if h1 < h2:
            for _ in range(h2-h1):
                p2 = p2.parent
        else:
            for _ in range(h1-h2):
                p1 = p1.parent

        while p1.parent and p2.parent:
            if p1 == p2:
                return p1
            else:
                p1 = p1.parent
                p2 = p2.parent

        return None

    def findheight(self, node):
        p = node
        h = 1
        while p.parent:
            h += 1
            p = p.parent
        return h



