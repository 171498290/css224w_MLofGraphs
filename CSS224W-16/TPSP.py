from queue import PriorityQueue
import numpy as np

c1 = np.array([0,1,2,8])
c2 = np.array([2,0,4,3])
c3 = np.array([4,6,0,2])
c4 = np.array([0,1,2,0])

adjM = np.row_stack([c1,c2,c3,c4])

# 定义一个修改有限队列的函数
def Modify(PQ, element, elementVal):
    '''
    Desc:
        修改优先队列中元素的值
    Para:
        PQ: 待修改的优先队列
        element: 待修改的元素
        elementVal: 待修改的元素值
    Return:
        修改后的PQ
    '''
    index = 0
    for element in PQ.queue:
        if element[1] == element:
            PQ.queue[index] = (elementVal, element)
        else:
            index += 1


def TPSPDijkstra(graph, nStart, nEnd):
    '''
    Desc:
        获取开始节点和被查找节点之间的最短路径
    Para:
        graph: 图的邻接矩阵
        nStart: 开始节点的索引
        nEnd: 需要被查找的节点的索引
    Return:
    '''
    # 初始化优先队列
    PQ = PriorityQueue()

    # 初始化初始点和其他点的距离为infinity
    nodeLen = graph.shape[0]
    _d = [np.inf] * nodeLen

    # 将初始点和自己的距离设置为0并插入到优先队列中
    _d[nStart] = 0
    # 将距离放在第一个索引位置以用来进行队列的排序
    PQ.put((_d[nStart], nStart))
# PQ.queue
    while not PQ.empty():
        # 将优先队列中最小的元素弹出
        u = PQ.get()[1]
        # 如果u的索引和被查找节点的索引一致的话就返回两个节点之间的距离
        if u == nEnd:
            return _d[u]
        
        for v in range(nodeLen):
            if graph[u][v] != 0:
                if _d[u] + graph[u][v] < _d[v]:
                    _d[v] = _d[u] + graph[u][v]
                    if (v, _d[v]) not in PQ.queue:
                        PQ.put((_d[v], v))
                    else:
                        Modify(PQ, v, _d[v])

    # 如果一直没有找到最短距离, 则返回inf
    return np.inf

TPSPDijkstra(graph=adjM, nStart=2, nEnd=1)