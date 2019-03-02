#include <bits/stdc++.h>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }

int arr[501];

int Pre_Order_traversal(Node* tree, int c=0){  
    if(tree==NULL)
        return c;
    else{
        arr[c]=tree->data;
        c++;
        c=Pre_Order_traversal(tree->left,c);
        c=Pre_Order_traversal(tree->right,c);
    }
    return c;
}


void preOrder(Node *root)  {
    int c=Pre_Order_traversal(root);
    int i=0;
    while(i!=c){
        cout<<arr[i]<<" ";
        i++;
    }
}

}; //End of Solution

int main() {
  
    Solution myTree;
    Node* root = NULL;
    
    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }
  
	myTree.preOrder(root);
    return 0;
}
