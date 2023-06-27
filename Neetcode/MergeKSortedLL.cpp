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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        struct custom{
            bool operator()(ListNode* a, ListNode* b){
                return a->val > b->val;
            }
        };
        priority_queue<ListNode*, vector<ListNode*>, custom> pq;
        if (lists.empty()){
            return nullptr;
        }
        if (lists.size() == 1){
            return lists[0];
        }
        for (auto l : lists){
            if (l != nullptr)
                pq.push(l);
        }
        if (pq.empty()){
            return nullptr;
        }
        ListNode* head = pq.top();
        ListNode* top = head;
        while (!pq.empty()){
            top = pq.top();
            pq.pop();
            if (top->next != nullptr){
                pq.push(top->next);
            }
            if (!pq.empty()){
                top->next = pq.top();
            }
        }
        return head;
    }
};
