from Linked_List import *
"""
链表指针指向前一个元素
实现链表元素从尾到头打印

这个办法需要改变单向链表原有的结构
"""


def reverse_linked_list(head):
    p_pre = None
    p_cur = head
    i = 0
    while p_cur:
        p_next = p_cur.next
        p_cur.next = p_pre
        p_pre = p_cur
        p_cur = p_next
        i += 1
    head.next = p_pre
    print_list(head, i)
    return True


def print_list(p, length):
    arr = []
    i = 0
    while i < length:
        arr.append(p.next.elem)
        p = p.next
        i += 1
    print(arr)
    return True


if __name__ == '__main__':
    linklist = LinkList()
    linklist.create_list_head(10)
    linklist.travel()
    reverse_linked_list(linklist.get_head())

