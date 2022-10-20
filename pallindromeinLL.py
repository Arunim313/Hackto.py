class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def makeList(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


class Solution(object):
    def isPalindrome(self, head):
        fast, slow = head, head
        rev = None
        flag = 1
        if not head:
            return True
        while fast and fast.next:
            if not fast.next.next:
                flag = 0
                break
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp
        fast = slow.next
        slow.next = rev
        if flag:
            slow = slow.next
        while fast and slow:
            if fast.value != slow.value:
                return False
            fast = fast.next
            slow = slow.next
        return True


head = makeList([1, 2, 3, 2, 1])
ob1 = Solution()
print(ob1.isPalindrome(head))
