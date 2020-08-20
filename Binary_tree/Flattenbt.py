#without extra space
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# Utility function to print the inorder
# traversal of the tree
def PrintInorderBinaryTree(root):
    if (root is None):
        return
    PrintInorderBinaryTree(root.left)
    print(str(root.data), end=" ")
    PrintInorderBinaryTree(root.right)

def flatten(root):
    global last
    if(root is None ):
        return
    left =root.left
    right =root.right
    if(root!=last):
        last.right=root
        last.left=None
        last=root
    flatten(left)
    flatten(right)
    if(left is None and right is None):
        last=root

if __name__ == '__main__':
    # Build the tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right = Node(5)
    root.right.right = Node(6)

    # Print the inorder traversal of the
    # original tree
    print("Original inorder traversal : ", end="")
    PrintInorderBinaryTree(root)
    print("")

    # Global variable to maintain the
    # last node added to the linked list
    last = root
    flatten(root)
    print("Flattened inorder traversal : ", end="")
    PrintInorderBinaryTree(root)
    print()

'''Node* solution(Node* A) 
{ 
  
    // Declare a stack 
    stack<Node*> st; 
    Node* ans = A; 
  
    // Iterate till the stack is not empty 
    // and till root is Null 
    while (A != NULL || st.size() != 0) { 
  
        // Check for NULL 
        if (A->right != NULL) { 
            st.push(A->right); 
        } 
  
        // Make the Right Left and 
        // left NULL 
        A->right = A->left; 
        A->left = NULL; 
  
        // Check for NULL 
        if (A->right == NULL && st.size() != 0) { 
            A->right = st.top(); 
            st.pop(); 
        } 
  
        // Iterate 
        A = A->right; 
    } 
    return ans; 
} It's TC-O(N) and SC-O(logn)'''
#1 more soln
'''void flatten(struct Node* root) 
{ 
    // base condition- return if root is NULL 
    // or if it is a leaf node 
    if (root == NULL || root->left == NULL && 
                        root->right == NULL) { 
        return; 
    } 
  
    // if root->left exists then we have  
    // to make it root->right 
    if (root->left != NULL) { 
  
        // move left recursively 
        flatten(root->left); 
     
        // store the node root->right 
        struct Node* tmpRight = root->right; 
        root->right = root->left; 
        root->left = NULL; 
  
        // find the position to insert 
        // the stored value    
        struct Node* t = root->right; 
        while (t->right != NULL) { 
            t = t->right; 
        } 
  
        // insert the stored value 
        t->right = tmpRight; 
    } 
  
    // now call the same function 
    // for root->right 
    flatten(root->right); 
}'''