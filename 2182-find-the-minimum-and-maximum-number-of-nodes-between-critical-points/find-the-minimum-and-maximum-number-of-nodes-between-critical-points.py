# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        positions=[]
        prev= head
        curr=head.next
        pos=1

        while curr and curr.next:
            if ((curr.val>prev.val and curr.val>curr.next.val)or (curr.val<prev.val and curr.val< curr.next.val)):
                positions.append(pos)
            prev =curr
            curr =curr.next
            pos+=1
        if len(positions)<2:
            return [-1,-1]
        min_distance =float('inf')
        for i in range(1,len(positions)):
            min_distance=min(min_distance,positions[i]-positions[i-1])
        max_distance =positions[-1]-positions[0]
        return [min_distance, max_distance]                                            
        