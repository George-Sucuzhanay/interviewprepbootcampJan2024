

def removeNthFromEnd(head, n):
    dummmy = l = ListNode(0, head)
    r = head
    for i in range(n): # r moves n times
        r = r.next

    while r: # r move num of nodes - n times
        r = r.next
        l = l.next
    l.next = l.next.next # moving ptrs for deletion


    # time: O(n)
    # 