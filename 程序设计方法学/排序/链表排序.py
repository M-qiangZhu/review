class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 添加结点方法
    def add_list(self, item):
        # 如果不是Node, 构建为Node
        if not isinstance(item, Node):
            item = Node(item)

        # 如果头结点为空, 则当前节点就是 item
        if self.head is None:
            self.head = item
        else:
            # 如果已经有了头结点, 则加到尾部后面
            self.tail.next = item

        # 更新尾结点
        self.tail = item

    # 遍历链表
    def travel_list(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    # 获取链表中的最小结点
    def getPreSmall(self):
        # 初始化, 记录最小值的指针和指向最小值的指针
        small_p = self.head
        pre_p = self.head
        # 初始化指向最终最小值的指针
        pre_small = None
        # 初始化遍历指针
        travel_p = pre_p.next
        # 开始遍历
        while travel_p is not None:
            # 如果当前指针所指的值 < 当前最小值
            if travel_p.data < small_p.data:
                # 更新最小值指针, 以及指向最小值的指针
                small_p = travel_p
                pre_small = pre_p
            #每次应该关注的是指向最小值的指针的位置, 并由它确定当前循环指针的位置
            pre_p = pre_p.next
            travel_p = pre_p.next
        return pre_small



    # 链表排序
    def select_sort(self):
        tail = None  # 排序部分的最后一个结点
        travel_p = self.head  # 尚未排序的第一个节点
        small_p = None # 最小结点
        pre_small = None # 最小结点的上一个结点
        while travel_p is not None:
            small_p = travel_p
            pre_small = self.getPreSmall()
            # 因为 small_p 有可能是头结点, 所以 pre_small 有可能为空
            if pre_small is not None:
                small_p = pre_small.next
                pre_small.next = small_p.next
            else:
                head = small_p
            if tail is None:
                head = small_p
            else:
                tail.next = small_p
            tail = small_p
        return head





if __name__ == '__main__':
    node1 = Node(4)
    node2 = Node(7.8)
    node3 = Node(3.6)
    node4 = Node(5)
    my_link = SingleLinkedList()
    my_link.add_list(node1)
    my_link.add_list(node2)
    my_link.add_list(node3)
    my_link.add_list(node4)
    my_link.travel_list()
    head = my_link.select_sort()
    print("------")
    my_link01 = SingleLinkedList()
    my_link01.add_list(head)
    my_link01.travel_list()

