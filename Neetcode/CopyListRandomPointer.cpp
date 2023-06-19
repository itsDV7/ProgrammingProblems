/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    map<Node*, Node*> indexnode;
    Node* copyRandomList(Node* head) {
        Node* h = head;
        Node* dummy = new Node(-1e4 - 1);
        Node* d = dummy;
        while (h != nullptr){
            Node* newnode = new Node(h->val);
            d->next = newnode;
            indexnode[h] = newnode;
            d = d->next;
            h = h->next;
        }
        d = dummy;
        d = d->next;
        h = head;
        while (d != nullptr){
            if (h->random != nullptr){
                d->random = indexnode[h->random];
            }
            else{
                d->random = nullptr;
            }
            d = d->next;
            h = h->next;
        }
        return dummy->next;
    }
};
