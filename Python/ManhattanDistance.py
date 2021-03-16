class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "point: ({} , {})".format(self.x, self.y)


def calc_manhattan_distance(point_a, point_b):
    manhattan_distance = (abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y))
    
    # Three lines below used for debugging total distance
    #man_dist_x = abs(point_a.x - point_b.x)
    #man_dist_y = abs(point_a.y - point_b.y)
    #print("X distance: {}\nY distance: {}".format(man_dist_x, man_dist_y))

    # following line is used for testing purposes only
    #return manhattan_distance

    # following line is used for final implementation
    return "Manhattan distance from {} to {} is {} units.".format(point_a, point_b, manhattan_distance)


if __name__ == "__main__":
    print("Enter two numbers separated by a space to match x and y coordinates. See examples below:"
        "\n( X , Y ) = 1 2\t\t will produce the point (1, 2) \n( X, Y ) = -45 23\t will produce the point"
        "(-45, 23) and so on...\tCTRL + C to exit.\n")

    flag = True  # Only integers separated by a space as we are inputting coordinates of points
    while flag:
        try:
            x_point_a, y_point_a = input("Point A - ( X , Y ): ").split()
            x_point_b, y_point_b = input("Point B - ( X , Y ): ").split()

            # without these next two lines, negative numbers are flagged as non-integers due to the '-' symbol. Doesn't affect the actual value, just to ensure validity
            pos_x_point_a, pos_y_point_a = x_point_a.strip('-'), y_point_a.strip('-')
            pos_x_point_b, pos_y_point_b = x_point_b.strip('-'), y_point_b.strip('-')

            if pos_x_point_a.isdigit() and pos_y_point_a.isdigit() and pos_x_point_b.isdigit() and pos_y_point_b.isdigit():
                flag = False
            else:
                print("Please enter only integers as we are inputting coordinates. Try again.")
        except KeyboardInterrupt:  # CTRL + C
            print("\nYou have chosen to quit the program, press enter to exit.")
            exit(0)
        except ValueError:         # only one value was entered
            print("Please enter two integers separated by a space. Try again.")

    # creating the two points to be used for calculating
    point_a = Point(int(x_point_a), int(y_point_a))
    point_b = Point(int(x_point_b), int(y_point_b))

    print(calc_manhattan_distance(point_a, point_b))
