import heapq
import pygame

# A*寻路算法
def a_star(start, end, walls, grid_size):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

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
            if 0 <= x < 800 and 0 <= y < 600:
                neighbor_rect = pygame.Rect(x, y, grid_size, grid_size)
                if not any(wall.colliderect(neighbor_rect) for wall in walls):
                    valid_neighbors.append(neighbor)
        return valid_neighbors

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + grid_size
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []
