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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr){
            return list2;
        }
        if (list2 == nullptr){
            return list1;
        }
        ListNode* temp = nullptr;
        if (list1->val > list2->val){
            swap(list1, list2);
        }
        ListNode* rethead = list1;
        while (list1->next != nullptr){
            if (list1->next->val > list2->val){
                temp = list1->next;
                list1->next = list2;
                list1 = temp;
                swap(list1, list2);
            }
            else{
                list1 = list1->next;
            }
        }
        if (list2 != nullptr){
            list1->next = list2;
        }
        return rethead;
    }
};
