from Stack import *
"""
两个栈实现一个队列
"""


class CQueue(object):
    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()

    def append_tail(self, e):
        """尾部插入"""
        self.__stack1.push(e)
        return True

    def delete_head(self):
        """头部删除"""
        if self.__stack2.is_empty():  # 判断stack2是否为空
            assert not self.__stack1.is_empty(), "CQueue is empty"
            while not self.__stack1.is_empty():
                self.__stack2.push(self.__stack1.pop())
            return self.__stack2.pop()
        else:
            return self.__stack2.pop()


if __name__ == '__main__':
    cq = CQueue()
    cq.append_tail('a')
    cq.append_tail('b')
    cq.append_tail('c')
    cq.append_tail('d')
    for i in range(0, 4):
        print(cq.delete_head())
