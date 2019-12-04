import argparse

"""
Returns an array of integers read from filename
"""
def read_file(filename):
    with open(filename) as f:
        for line in f:
            return list(map(lambda x : int(x), line.split(",")))

def part1(op_list):
    index = 0
    valid_opcodes = [1,2,99]
    while op_list[index] != 99:
        opcode = op_list[index]
        if opcode not in valid_opcodes:
            return [-1]
        elif opcode == 1:
            operand1 = op_list[op_list[index + 1]]
            operand2 = op_list[op_list[index + 2]]
            val = operand1 + operand2
            op_list[op_list[index + 3]] = val
        elif opcode == 2:
            operand1 = op_list[op_list[index + 1]]
            operand2 = op_list[op_list[index + 2]]
            val = operand1 * operand2
            op_list[op_list[index + 3]] = val
        index += 4
    
    return op_list



def part2(op_list):
        for noun in range(0,100):
            for verb in range(0, 100):
                new_op_list = op_list.copy()
                new_op_list[1] = noun
                new_op_list[2] = verb
                if part1(new_op_list)[0] == 19690720:
                    return new_op_list
        


def run_tests():
    assert(part1([1,0,0,0,99]) == [2,0,0,0,99])
    assert(part1([2,3,0,3,99]) == [2,3,0,6,99])
    assert(part1([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
    assert(part1([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
    assert(part1([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50])

#part 1 guess 1: 1090665 -- too low

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parsing a file name")
    parser.add_argument("-f", help="This is the file name to read.")
    parser.add_argument("-p", default=1, help="This is the problem of the day (part 1 or 2)")

    args = parser.parse_args()
    # print(args.f)

    filename = args.f
    part = args.p

    codes = read_file(filename)

    result = []

    if part == "t":
        run_tests()
        print("Tests passed!")
    elif part == "1":
        result = part1(codes)
    elif part == "2":
        result = part2(codes)

    print(result)

