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
    int pairSum(ListNode* head) {
        int nodecount = 0;
        ListNode* start = head;
        while (head){
            nodecount += 1;
            // cout << head->val;
            head = head->next;
        }
        // cout << nodecount;
        head = start;
        int halfway = nodecount / 2;
        vector<int> space;
        for (int i=0; i < halfway; i++) {
            // cout << head->val;
            space.push_back(head->val);
            head = head->next;
        }
        int maxval = 0;
        for (int i=halfway-1; i >= 0; i--) {
            // cout << head->val;
            space[i] += head->val;
            head = head->next;
            maxval = max(maxval, space[i]);
        }
        return maxval;
    }
};
