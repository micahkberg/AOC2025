from day01 import read_input

def product(nums):
    total = 1
    for n in nums:
        total*=n
    return total

def main():
    lines = read_input("06")[:-1]
    lines = [l.split() for l in lines]
    grand_total = 0
    for i in range(len(lines[0])):
        operator = lines[-1][i]
        operands = [int(j[i]) for j in lines[:-1]]
        if operator == '+':
            grand_total += sum(operands)
        elif operator == '*':
            grand_total += product(operands)
    print(grand_total)

def main2():
    lines = read_input("06")[:-1]
    operators = lines[-1].split()
    operands = []
    grand_total = 0
    for i in range(len(lines[0])):
        new_operand = ''
        for j in range(len(lines)-1):
            new_operand += lines[j][i]
        new_operand = new_operand.strip()
        if new_operand == '':
            op = operators.pop(0)
            if op == '+':
                grand_total += sum(operands)
                operands = []
            elif op == '*':
                grand_total += product(operands)
                operands = []
        else:
            operands.append(int(new_operand))
    op = operators.pop(0)
    if op == '+':
        grand_total += sum(operands)
    elif op == '*':
        grand_total += product(operands)
    print(grand_total)
    #11371597082440 too low
    #11371597126232



if __name__ == '__main__':
    main()
    main2()