/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        if (head == nullptr){
            return false;
        }
        while (true){
            slow = slow->next;
            if (slow == nullptr){
                return false;
            }
            fast = fast->next;
            if (fast == nullptr){
                return false;
            }
            fast = fast->next;
            if (fast == nullptr){
                return false;
            }
            if (slow == fast){
                return true;
            }
        }
        return false;
    }
};
