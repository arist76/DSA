/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head)
{
    int len;
    struct ListNode* temp = head;
    for (len = 1; temp->next != NULL; len++)
        temp = temp->next;
    
    int half_len = len/2 + 1;

    temp = head;
    for (int i = 1; i < half_len; i++)
    {
        temp = temp->next;
    }
    return temp;
}
