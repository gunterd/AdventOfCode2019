import argparse

"""
Returns an the lines as read from filename
"""
def read_file(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result.append(list(line.split(",")))
    return result


def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def get_coords(wire):
    coords = {}
    current_coord = (0,0)
    coords[current_coord] = 0

    total_distance = 0

    for seg in wire:
        direction = seg[0]
        distance = int(seg[1:])

        x_move = 0
        y_move = 0

        if direction == "U":
            y_move = 1
        elif direction == "D":
            y_move = -1
        elif direction == "L":
            x_move = -1
        elif direction == "R":
            x_move = 1
        
        for i in range(0, distance):
            total_distance += 1
            new_coord = (current_coord[0] + x_move, current_coord[1] + y_move)
            if new_coord not in coords:
                coords[new_coord] = total_distance
            current_coord = new_coord

    return coords

def part1(wires):
    wire1 = wires[0]
    wire2 = wires[1]

    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)

    closest_point_distance = 2 ** 30

    for wire1_coord in coords1:
        if wire1_coord in coords2:
            distance = manhattan_distance((0,0), wire1_coord)
            if distance < closest_point_distance and distance > 0:
                closest_point_distance = distance
    
    return closest_point_distance

def part2(wires):
    wire1 = wires[0]
    wire2 = wires[1]

    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)

    closest_point_distance = 2 ** 30

    for wire1_coord in coords1:
        if wire1_coord in coords2:
            distance = coords1[wire1_coord] + coords2[wire1_coord]
            if distance < closest_point_distance and distance > 0:
                closest_point_distance = distance
    
    return closest_point_distance


def run_tests():
    assert(manhattan_distance([0,0], [2,2]) == 4)
    assert(manhattan_distance([1,1], [1,1]) == 0)
    assert(manhattan_distance([1,2], [2,1]) == 2)


    test_data = ["R2", "U5"]
    points = get_coords(test_data)
    # print(points)
    assert((0,0) in points)
    assert((1,0) in points)
    assert((2,0) in points)
    assert((3,0) not in points)

    assert((1, 2) not in points)
    assert((2, 1) in points)
    assert((2, 2) in points)
    assert((2, 5) in points)
    assert((2, 6) not in points)


    # print(part1(["R2"], ["U5"]))

    assert(part1(
        [["R75","D30","R83","U83","L12","D49","R71","U7","L72"],
        ["U62","R66","U55","R34","D71","R55","D58","R83"]]
    ) == 159)

    assert(part1(
        [["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
        ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]]
    ) == 135)

    assert(part2(
        [["R8","U5","L5","D3"],
        ["U7","R6","D4","L4"]]
    ) == 30)

    assert(part2(
        [
            ["R75","D30","R83","U83","L12","D49","R71","U7","L72"],
            ["U62","R66","U55","R34","D71","R55","D58","R83"]
        ]
    ) == 610)
    
    assert(part2(
        [
            ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
            ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
        ]
    ) == 410)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parsing a file name")
    parser.add_argument("-f", help="This is the file name to read.")
    parser.add_argument("-p", default=1, help="This is the problem of the day (part 1 or 2)")

    args = parser.parse_args()
    # print(args.f)

    filename = args.f
    part = args.p

    wires = read_file(filename)

    result = -1

    # print(wires)

    if part == "t":
        run_tests()
        print("Tests passed!")
    elif part == "1":
        result = part1(wires)
    elif part == "2":
        result = part2(wires)

    print(result)