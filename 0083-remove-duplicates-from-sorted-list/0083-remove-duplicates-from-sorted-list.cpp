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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return head;
        else if (head->next == nullptr) return head;
        ListNode *prev = head;
        ListNode *node = head->next;
        while (node) {
            if (node->val == prev->val) {
                ListNode *temp = node->next;
                prev->next = temp;
                node = temp;
            } 
            else {
                prev = node;
                node = node->next;
            }
        }
        return head;
    }
};