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
    void reorderList(ListNode* head) {
        int num = 0;
        ListNode* h;
        while (h != nullptr){
            num += 1;
            h = h->next;
        }
        int half = num/2;
        h = head;
        ListNode* prev = nullptr;
        ListNode* hn = nullptr;
        while (h != nullptr){
            if (half == 0){
                hn = h->next;
                h->next = prev;
                prev = h;
                h = hn;
            }
            else{
                half -= 1;
                h = h->next;
            }
        }
        h = head;
        ListNode* pn;
        while (h != prev && h->next != prev){
            hn = h->next;
            pn = prev->next;
            h->next = prev;
            prev->next = hn;
            h = hn;
            prev = pn;
        }
    }
};
