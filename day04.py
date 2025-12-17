from day01 import read_input

def neighbor_count(x, y, grid):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
    n = 0
    for direction in dirs:
        new_x, new_y = x + direction[0], y + direction[1]
        if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
            continue
        if grid[new_y][new_x] == "@":
            n += 1
    return n

def main():
    lines = read_input('04')[:-1]
    accessible_rolls = 0
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if lines[y][x] == '@':
                n = neighbor_count(x, y, lines)
                if n<4:
                    accessible_rolls += 1
    print(accessible_rolls)

    #pt 1 12054 too high
    #     1376

def mainpt2():
    lines = read_input('04')[:-1]
    lines = [list(i) for i in lines]
    rolls_removed = 0
    rolls_removed_this_round = 1
    while rolls_removed_this_round > 0:
        rolls_removed_this_round = 0
        for x in range(len(lines[0])):
            for y in range(len(lines)):
                if lines[y][x] == '@':
                    n = neighbor_count(x, y, lines)
                    if n<4:
                        rolls_removed += 1
                        rolls_removed_this_round += 1
                        lines[y][x] = 'x'
    print(rolls_removed)

if __name__ == '__main__':
    main()
    mainpt2()