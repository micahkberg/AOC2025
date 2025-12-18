from day01 import read_input

def main():
    grid = read_input('07')
    tachyon_prev_pos = set()
    split_count = 0
    for line in grid:
        tachyon_new_pos = set()
        for i in range(len(line)):
            char = line[i]
            if char == "S":
                tachyon_new_pos.add(i)
            elif char == "^":
                if i in tachyon_prev_pos:
                    split_count += 1
                    tachyon_prev_pos.remove(i)
                    tachyon_new_pos.add(i-1)
                    tachyon_new_pos.add(i+1)
        tachyon_prev_pos = tachyon_prev_pos.union(tachyon_new_pos)
    print(split_count)

def main2():
    grid = read_input('07')[:-1]
    timelines = [0 for _ in range(len(grid[0]))]
    for line in grid:
        new_timelines = [0 for _ in range(len(grid[0]))]
        for i in range(len(line)):
            char = line[i]
            if char == 'S':
                new_timelines[i] += 1
            elif char == '^':
                new_timelines[i + 1] += timelines[i]
                new_timelines[i - 1] += timelines[i]
            else:
                new_timelines[i] += timelines[i]
        print(new_timelines)
        timelines = new_timelines.copy()
    print(sum(new_timelines))


if __name__ == '__main__':
    main()
    main2()
