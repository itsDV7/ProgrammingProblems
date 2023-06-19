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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int num = 0;
        ListNode* h = head;
        while (h != nullptr){
            num += 1;
            h = h->next;
        }
        num = num - n;
        h = head;
        if (num){
            while (num-1){
                num -= 1;
                h = h->next;
            }
        }
        else{
            return head->next;
        }
        h->next = h->next->next;
        return head;
    }
};
