# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Не возвращайте ничего, изменяйте 'head' на месте.
        """
        if not head or not head.next:
            return

        # ШАГ 1: Находим середину списка (Быстрый и Медленный указатели)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Теперь slow находится в конце первой половины списка.
        
        # ШАГ 2: Разворачиваем вторую половину списка
        second = slow.next   # Начало второй половины
        slow.next = None     # Отрываем первую половину от второй (разрезаем список)
        
        prev = None          # Стандартный алгоритм разворота (как в 1-й задаче)
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # Теперь prev - это голова перевернутой второй половины.
        
        # ШАГ 3: Поочередно сливаем две половины
        first = head         # Указатель на начало первой половины
        second = prev        # Указатель на начало (бывший конец) второй половины
        
        while second:        # Вторая половина всегда либо равна, либо короче первой
            # Запоминаем следующие узлы, чтобы не потерять их при переподключении
            temp1 = first.next
            temp2 = second.next
            
            # Перешиваем стрелочки:
            first.next = second  # 1-й элемент первой половины указывает на 1-й элемент второй
            second.next = temp1  # 1-й элемент второй половины указывает на 2-й элемент первой
            
            # Сдвигаем указатели вперед для следующего шага
            first = temp1
            second = temp2