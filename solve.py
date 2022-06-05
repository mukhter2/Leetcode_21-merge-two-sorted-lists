# #Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while(list1.next != None):
            lst.append(list1.val)
            list1=list1.next
        lst.append(list1.val)
        list1=list1.next
        while(list2.next != None):
            lst.append(list2.val)
            list2=list2.next
        lst.append(list2.val)
        list2=list2.next
        lst.sort()
        finList=dim=ListNode(0)
        for i in range(0,len(lst)):
            finList.next=ListNode(lst[i])
            finList=finList.next
        return dim.next
            
            
            
                
