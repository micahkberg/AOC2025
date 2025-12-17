from day01 import read_input

def get_2joltage(bank):
    #naive solution
    max_joltage = 0
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage

def get_2joltage_fast(bank):
    print(bank)
    nums = list(map(int, bank))
    x = max(nums[0:-1])
    x_pos = nums.index(x)
    y = max(nums[x_pos+1:])
    return x*10 + y

def get_Njoltage(bank, n):
    output = ''
    nums = list(map(int, bank))
    prev_pos = 0
    for i in range(n-1,-1,-1):
        #i = other digits remaining
        digit = max(nums[prev_pos:len(nums)-i])
        digit_loc = nums.index(digit, prev_pos)
        prev_pos = digit_loc
        output += str(digit)
        prev_pos = digit_loc+1
    return int(output)

def main():
    day = '03'
    lines = read_input(day)
    max_joltage = 0
    megamax_joltage = 0
    for bank in lines:
        if not bank:
            continue
        #max_joltage += get_2joltage_fast(bank)
        max_joltage += get_Njoltage(bank, 2)
        megamax_joltage += get_Njoltage(bank, 12)

    print(max_joltage) #17278
    print(megamax_joltage)
    # 171813648607564, too high


if __name__ == '__main__':
    main()