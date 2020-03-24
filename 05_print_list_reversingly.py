from Stack import *
from Linked_List import *
"""
使用栈从尾到头打印链表
"""


def print_list_reversely(p):
    s = Stack()
    li = []
    while p:
        s.push(p.elem)
        p = p.next
    while not s.is_empty():
        li.append(s.pop())
    print(li)


if __name__ == '__main__':
    linklist = LinkList()
    linklist.create_list_head(10)
    linklist.travel()
    print_list_reversely(linklist.get_head())
