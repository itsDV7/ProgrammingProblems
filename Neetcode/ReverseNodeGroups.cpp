/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k==1){
            return head;
        }
        int nodes = 0;
        ListNode* h = head;
        while (h != nullptr){
            nodes += 1;
            h = h->next;
        }
        h = head;
        if (nodes == k){
            ListNode* temp;
            ListNode* prev = nullptr;
            while (h != nullptr){
                temp = h->next;
                h->next = prev;
                prev = h;
                h = temp;
            }
            return prev;
        }
        int divs = nodes/k;
        ListNode* retnode = head;
        ListNode* start = head;
        ListNode* last = nullptr;
        ListNode* prev = nullptr;
        ListNode* temp;
        h = head;
        while (divs){
            for (int i = 0; i < k; i++){
                temp = h->next;
                h->next = prev;
                prev = h;
                h = temp;
            }
            divs -= 1;
            if (last == nullptr){
                retnode = prev;
            }
            else{
                last->next = prev;
            }
            last = start;
            start->next = h;
            start = h;
            prev = nullptr;
        }
        return retnode;
    }
};
