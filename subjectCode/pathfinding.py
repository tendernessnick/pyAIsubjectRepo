import heapq  # 导入heapq库，用于优先队列
import pygame

# A*寻路算法
def a_star(start, end, walls, grid_size):
    """
    A*寻路算法实现
    :param start: 起始点
    :param end: 终点
    :param walls: 墙体列表
    :param grid_size: 网格大小
    :return: 从起点到终点的路径
    """

    # 定义启发式函数heuristic，使用曼哈顿距离计算两个点之间的估计距离。
    # 曼哈顿距离是指在一个二维网格中，从一个点到另一个点的路径长度（只能水平和垂直移动）
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # 获取当前节点的所有邻居节点
    def get_neighbors(node):
        neighbors = [
            (node[0] + grid_size, node[1]),
            (node[0] - grid_size, node[1]),
            (node[0], node[1] + grid_size),
            (node[0], node[1] - grid_size)
        ]
        valid_neighbors = []
        for neighbor in neighbors:
            x, y = neighbor
            if 0 <= x < 800 and 0 <= y < 600:  # 检查邻居节点是否在地图范围内
                neighbor_rect = pygame.Rect(x, y, grid_size, grid_size)
                if not any(wall.colliderect(neighbor_rect) for wall in walls):  # 检查邻居节点是否与墙体碰撞
                    valid_neighbors.append(neighbor)
        return valid_neighbors

    open_set = []  # 创建一个优先队列
    heapq.heappush(open_set, (0, start))  # 将起点加入优先队列
    came_from = {}  # 用于存储每个节点的父节点
    g_score = {start: 0}  # 起点的实际代价g(n)
    f_score = {start: heuristic(start, end)}  # 起点的总代价f(n)

    # 主循环
    # 从优先队列中取出f(n)最小的节点current
    # 如果current是终点，则通过回溯came_from字典重建路径，并返回路径
    # 对每个邻居节点，计算从起点到该邻居节点的实际代价tentative_g_score
    # 如果邻居节点未在g_score中，或新的tentative_g_score小于已有的g_score值，则更新邻居节点的父节点、g_score和f_score，并将邻居节点加入优先队列
    while open_set:  # 当优先队列不为空时
        _, current = heapq.heappop(open_set)  # 取出f(n)最小的节点
        if current == end:  # 如果当前节点是目标节点
            path = []
            while current in came_from:  # 通过回溯父节点链重建路径
                path.append(current)
                current = came_from[current]
            return path[::-1]  # 返回路径

        for neighbor in get_neighbors(current):  # 对每个邻居节点
            tentative_g_score = g_score[current] + grid_size  # 计算从起点到该邻居的g(n)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current  # 更新邻居的父节点为当前节点
                g_score[neighbor] = tentative_g_score  # 更新g(n)
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)  # 更新f(n)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))  # 将邻居节点加入优先队列

    return []  # 如果找不到路径，返回空列表
