class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def preorder(root):
    if(root is None):
        return [];
    ro=[root.val];
    l=preorder(root.left)
    r=preorder(root.right);
    return l+ro+r


r=Tree(8);
r.left=Tree(5);
r.left.left=Tree(1);
r.left.right=Tree(7);

#right
r.right=Tree(10);
r.right.right=Tree(12)



print(preorder(r));


