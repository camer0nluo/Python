from __future__ import annotations

DIRECTIONS = [
    [-1, 0],  # left
    [0, -1],  # down
    [1, 0],  # right
    [0, 1],  # up
]


# function to search the path
def search(
    grid: list[list[int]],
    init: list[int],
    goal: list[int],
    cost: int,
    heuristic: list[list[int]],
) -> tuple[list[list[int]], list[list[int]]]:

    closed = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    closed[init[0]][init[1]] = 1
    action = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]  # cost from starting cell to destination cell
    cell = [[f, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if not cell:
            raise ValueError("Algorithm is unable to find solution")
        cell.sort()
        cell.reverse()
        next = cell.pop()
        x = next[2]
        y = next[3]
        g = next[1]

        if x == goal[0] and y == goal[1]:
            found = True
        else:
            for i in range(len(DIRECTIONS)):  # to try out different valid actions
                x2 = x + DIRECTIONS[i][0]
                y2 = y + DIRECTIONS[i][1]
                if (
                    x2 >= 0
                    and x2 < len(grid)
                    and y2 >= 0
                    and y2 < len(grid[0])
                    and closed[x2][y2] == 0
                    and grid[x2][y2] == 0
                ):
                    g2 = g + cost
                    f2 = g2 + heuristic[x2][y2]
                    cell.append([f2, g2, x2, y2])
                    closed[x2][y2] = 1
                    action[x2][y2] = i
    x = goal[0]
    y = goal[1]
    invpath = [[x, y]]
    while x != init[0] or y != init[1]:
        x2 = x - DIRECTIONS[action[x][y]][0]
        y2 = y - DIRECTIONS[action[x][y]][1]
        x = x2
        y = y2
        invpath.append([x, y])

    path = [invpath[len(invpath) - 1 - i] for i in range(len(invpath))]
    return path, action


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
    ]

    init = [0, 0]
    # all coordinates are given in format [y,x]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1

    # the cost map which pushes the path closer to the goal
    heuristic = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
            if grid[i][j] == 1:
                # added extra penalty in the heuristic map
                heuristic[i][j] = 99

    path, action = search(grid, init, goal, cost, heuristic)

    print("ACTION MAP")
    for i in range(len(action)):
        print(action[i])

    for i in range(len(path)):
        print(path[i])
