from day01 import read_input

def read_inventory():
    lines = read_input("05")
    ing_ranges = []
    available_ing = []
    for line in lines:
        if '-' in line:
            r = list(map(int, line.split('-')))
            ing_ranges.append(r)
        elif line:
            available_ing.append(line)
    return ing_ranges, available_ing

def main():
    ranges, ingredients = read_inventory()
    fresh = 0
    for i in ingredients:
        for r in ranges:
            if int(i) in range(r[0], r[1]+1):
                fresh+=1
                break
    print(fresh)
    #pt 1 942 too high, counted overlapping ranges
    #     735

def main2():
    ranges, ingredients = read_inventory()
    ranges = sorted(ranges, key=lambda x: x[0])
    total_fresh = 0
    for i in range(len(ranges)):
        r = ranges[i]
        if r[1] < r[0]:
            continue
        ids_in_range = 1 + r[1] - r[0]
        total_fresh += ids_in_range
        for j in range(i+1,len(ranges)):
            next_r = ranges[j]
            if next_r[0] > r[1]:
                break
            new_next_r = [max(next_r[0], r[1]+1), next_r[1]]
            ranges[j] = new_next_r
    print(total_fresh)
    #6317675001406 too low
    #6317675001222 that's worse
    #311275188271456, fixed not accumulating ids
    #311275188280925, fixed over-deleting, still low
    #344306344403251, fixed subtracting negative ranges
    #344306344403172, fixed small overlaps

if __name__ == '__main__':
    main()
    main2()