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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int ans = 0;
        int carry = 0;
        ListNode* dummy = new ListNode(-1);
        ListNode* d = dummy;
        while (l1 != nullptr && l2 != nullptr){
            ans = l1->val + l2->val;
            if (carry){
                ans += 1;
                carry = 0;
            }
            carry = ans/10;
            d->next = new ListNode(ans%10);
            d = d->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while (carry){
            if (l1 != nullptr){
                ans = l1->val + carry;
                carry = 0;
                l1 = l1->next;
            }
            else if (l2 != nullptr){
                ans = l2->val + carry;
                carry = 0;
                l2 = l2->next;
            }
            else{
                if (carry){
                    ans = 1;
                }
            }
            carry = ans/10;
            d->next = new ListNode(ans%10);
            d = d->next;
        }
        while (l1 != nullptr){
            ans = l1->val;
            d->next = new ListNode(ans);
            d = d->next;
            l1 = l1->next;
        }
        while (l2 != nullptr){
            ans = l2->val;
            d->next = new ListNode(ans);
            d = d->next;
            l2 = l2->next;
        }
        return dummy->next;
    }
};
