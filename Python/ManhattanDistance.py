class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "point: ({} , {})".format(self.x, self.y)


def calc_manhattan_distance(first_point, second_point):
    manhattan_distance = (abs(first_point.x - second_point.x) + abs(first_point.y - second_point.y))
    
    # following line is used for testing purposes only
    #return manhattan_distance

    # following line is used for final implementation
    return "Manhattan distance from {} to {} is {}".format(first_point, second_point, manhattan_distance)


if __name__ == "__main__":
    print("Enter two numbers separated by a space to match x and y coordinates. See examples below.",
        "\n( X , Y ) = 1 2\t\t will produce the point (1, 2) \n( X, Y ) = -45 23\t will produce the point"
        "(-45, 23) and so on...\nCTRL + C to exit.\n")

    testing_chars = []

    # only pairs of integers separated by a space are allowed
    flag = True
    while flag:
        try:
            x_point_a, y_point_a = input("Point A - ( X , Y ): ").split()
            x_point_b, y_point_b = input("Point B - ( X , Y ): ").split()

            # without these next two lines, negative numbers are flagged as non-integers due to the '-' symbol
            pos_x_point_a, pos_y_point_a = x_point_a.strip('-'), y_point_a.strip('-')
            pos_x_point_b, pos_y_point_b = x_point_b.strip('-'), y_point_b.strip('-')

            if pos_x_point_a.isdigit() and pos_y_point_a.isdigit() and pos_x_point_b.isdigit() and pos_y_point_b.isdigit():
                flag = False
            else:
                print("Please only enter integers. Try again.")
        except KeyboardInterrupt:  # CTRL + C
            print("\nYou have chosen to quit the program, press enter to exit.")
            exit(0)
        except ValueError:         # only one value was entered
            print("Please enter two integers separated by a space. Try again.")

    point_a = Point(int(x_point_a), int(y_point_a))
    point_b = Point(int(x_point_b), int(y_point_b))

    print(calc_manhattan_distance(point_a, point_b))
