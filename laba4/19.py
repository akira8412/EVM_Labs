# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Создаем "пустышку" и прицепляем к ней начало нашего списка
        dummy = ListNode(0, head)
        
        # Оба указателя ставим на старт
        slow = dummy
        fast = head
        
        # 1. Даем быстрому указателю фору в 'n' шагов
        for i in range(n):
            fast = fast.next
            
        # 2. Теперь двигаем обоих одновременно, пока быстрый не дойдет до конца
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # 3. slow остановился прямо ПЕРЕД тем узлом, который надо удалить.
        # Просто перекидываем связь на следующий узел (пропуская целевой)
        slow.next = slow.next.next
        
        # dummy.next всегда указывает на актуальную голову списка
        return dummy.next