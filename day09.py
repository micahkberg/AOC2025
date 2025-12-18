from day01 import read_input
import itertools

def main():
    lines = read_input('09')[:-1]
    positions = [c.split(',') for c in lines]
    pairs = itertools.combinations(positions, 2)
    max_rect = 1
    for pair in pairs:
        p1, p2 = pair
        x1, y1 = map(int, p1)
        x2, y2 = map(int, p2)
        x = abs(x1 - x2)+1
        y = abs(y1 - y2)+1
        max_rect = max(max_rect, x*y)
    print(max_rect)
    # 4782758112 too low
    # 4782896435, forgot to include edges

if __name__ == '__main__':
    main()
