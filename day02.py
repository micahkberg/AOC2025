#day 2
import re
from day01 import read_input
day = '02'

def main():
    test_data = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
    data = read_input(day)[0].split(",")
    #data = test_data.split(",")
    total_pt1 = 0
    total_pt2 = 0
    for item in data:
        if not item:
            continue
        first, last = list(map(int, item.split("-")))
        #naive solution
        for i in range(first, last + 1):
            id_str = str(i)
            if not determine_validity(id_str):
                total_pt2 += i
            half = len(id_str)/2
            if half%1 == 0:
                half = int(half)
                if id_str[:half] == id_str[half:]:
                    total_pt1 += i

    print(total_pt1)
    print(total_pt2)
    #25894449318 too low
    #25912654282

def determine_validity(idcode):
    l = len(idcode)
    for i in range(1, l//2+1):
        if l%i == 0:
            segment = idcode[:i]
            check_value = segment*(int(l/i))
            if idcode == check_value:
                return False
    return True

if __name__ == '__main__':
    main()
