class Tree:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val;
        self.arr=[]

# def inorder(root):
#     if(root is None):
#         return [];
#     l=inorder(root.left);
#     rt=[root.val];            #write this if you want to array
#     # print(rt);
#     r=inorder(root.right);
#     return(l+rt)

def kthSmallest(root, k: int) -> int:
    if(root is None):
        return [];
    l=kthSmallest(root.left,k);
    rt=[root.val];            #write this if you want to array
    r=kthSmallest(root.right,k);
    return(l+rt+r)





r=Tree(2);
r.left=Tree(1);
r.right=Tree(3);
r.left.left=Tree(0);
r.left.right=Tree(2)

k=1;
arr=kthSmallest(r,k)
print(arr)

