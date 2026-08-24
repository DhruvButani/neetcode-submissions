#include <vector>
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

        int count = 0;
        ListNode* temp = head;
        
        while(temp != NULL) {
            temp = temp->next;
            count+=1;
        }

        temp = head;
        for(int i = 0; i<((count+1)/2)-1; i++) {
            temp = temp->next;
        }
        ListNode* current = temp->next;
        temp->next = NULL;

       //reverse back half of list
        ListNode* previous = nullptr;

        while(current != nullptr)  {

            ListNode* temp = current->next;
            current->next = previous;
            previous = current;
            current = temp;
        }


        //just finish it off bruh

        ListNode* first = head;
        ListNode* second = previous;


        //once temp is Null, assign prev and leave

        while(second != NULL) {
            temp = first->next;
            first->next = second;
            second = second->next;

            first->next->next = temp;
            first = temp;

        }
        
    }
};
