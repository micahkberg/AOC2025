# day 1
import numpy as np

def read_input(daynum):
    with open(daynum + '.txt') as f:
        return f.read().split("\n")

def main():
    rotations = read_input("01")
    lock_position = 50
    zeros = 0
    more_zeroes=0
    for r in rotations:
        print(lock_position)
        if not r:
            continue
        direction = {"L":-1, "R":1}[r[0]]
        dist = int(r[1:])*direction
        lock_position += dist
        if lock_position <= 0 or lock_position > 99:
            more_zeroes += np.ceil(np.abs(dist)/100)
        lock_position = lock_position % 100
        if lock_position == 0:
            zeros += 1
    print(zeros)
    print(more_zeroes)

    #slow way
    lock_position = 50
    more_zeroes=0
    for r in rotations:
        if not r:
            continue
        direction = {"L":-1, "R":1}[r[0]]
        dist = int(r[1:])
        for i in range(dist):
            lock_position += direction
            lock_position %= 100
            if lock_position == 0:
                more_zeroes += 1
    print(more_zeroes)

if __name__ == '__main__':
    main()
