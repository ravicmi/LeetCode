# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        lists = [a for a in lists if a]
        if not lists:
            return None
        # head_dict = {index: head for (index, head) in enumerate(lists)}
        heads = [(head.val, index) for  (index, head) in enumerate(lists)]
        heapq.heapify(heads)
        _, index = heapq.heappop(heads)
        result = lists[index]
        current = result
        lists[index] = lists[index].next
        if lists[index]:
            heapq.heappush(heads, (lists[index].val, index))
        while heads:
            _, index = heapq.heappop(heads)
            current.next = lists[index]
            current = current.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heads, (lists[index].val, index))
        return result

        


