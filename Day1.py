import argparse

"""
Returns an array of integers read from filename
"""
def read_file(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result.append(int(line))
    return result

def day1(masses):
    required_fuel = 0
    for mass in masses:
        required_fuel += calculate_required_fuel(mass)

    return required_fuel

def calculate_required_fuel(mass):
    return (mass // 3) - 2

def day1_part2(masses):
    total_fuel = 0
    for mass in masses:
        total_for_mass = 0
        fuel = calculate_required_fuel(mass)
        while fuel > 0:
            total_for_mass += fuel
            fuel = calculate_required_fuel(fuel)
        total_fuel += total_for_mass

    return total_fuel



def run_tests():
    assert calculate_required_fuel(12) == 2
    assert calculate_required_fuel(14) == 2
    assert calculate_required_fuel(1969) == 654
    assert calculate_required_fuel(100756) == 33583

    assert day1_part2([14]) == 2
    assert day1_part2([1969]) == 966
    assert day1_part2([100756]) == 50346

    assert day1([30, 30, 30]) == 24
    assert day1_part2([30, 30, 30]) == 24

    assert day1([40]) == 11
    assert day1_part2([40]) == 11 + 1
    assert day1_part2([40, 40, 40]) == (11 + 1) * 3

    assert day1_part2([100756]) == 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2

#part 2 -- wrong 5123500

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parsing a file name")
    parser.add_argument("-f", help="This is the file name to read.")
    parser.add_argument("-p", default=1, help="This is the problem of the day (part 1 or 2)")

    args = parser.parse_args()
    # print(args.f)

    filename = args.f
    part = args.p

    result = 0

    masses = read_file(filename)

    if part == "1":
        result = day1(masses)
    elif part == "2":
        result = day1_part2(masses)
    elif part == "t":
        run_tests()
        print("Tests passed!")

    print(result)