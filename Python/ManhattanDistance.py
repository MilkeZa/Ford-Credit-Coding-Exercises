class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "point: ( {} , {} )".format(self.x, self.y)


def calc_manhattan_distance(first_point, second_point):
    manhattan_distance = (abs(first_point.x - second_point.x) + abs(first_point.y - second_point.y))

    # comment out the next line if you wish to perform testing
    return "Manhattan distance from {} to {} is {}".format(first_point, second_point, manhattan_distance)
    
    # comment out this line for final implementation
    # return manhattan_distance


if __name__ == "__main__":
    print("Enter two numbers separated by a space to match x and y coordinates. See examples below.",
        "\n( X , Y ) = 1 2\t\t will produce the point (1, 2) \n( X, Y ) = -45 23\t will produce the point"
        "(-45, 23) and so on...\n")

    x_point_a, y_point_a = input("( X , Y ): ").split()
    x_point_b, y_point_b = input("( X , Y ): ").split()

    point_a = Point(int(x_point_a), int(y_point_a))
    point_b = Point(int(x_point_b), int(y_point_b))

    print(calc_manhattan_distance(point_a, point_b))
