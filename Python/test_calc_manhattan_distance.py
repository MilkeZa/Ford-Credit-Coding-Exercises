import unittest
import ManhattanDistance as MD


class TestManhattanCalc(unittest.TestCase):
    def test_manhattan_calc(self):
        origin = MD.Point(0, 0)  # one of the points to be measured from
        
        # -------------------- begin creating points -------------------- #
        # creating an imaginary 10x10 square's corners
        point_1 = MD.Point(10, 10)
        point_2 = MD.Point(-10, 10)
        point_3 = MD.Point(10, -10)
        point_4 = MD.Point(-10, -10)
        
        # creating points on the x and y axes
        point_5 = MD.Point(-5, 0)
        point_6 = MD.Point(5, 0)
        point_7 = MD.Point(0, 5)
        point_8 = MD.Point(0, -5)

        # creating arbitrary points to ensure even random values work
        point_9 = MD.Point(1, 14)
        point_10 = MD.Point(-7, 8)
        point_11 = MD.Point(47, 100)
        point_12 = MD.Point(-3, 2)
        point_13 = MD.Point(3, -2)
        # ----------------------- end creating points ----------------------- #


        # -------------------- begin testing of points -------------------- #
        self.assertEqual((MD.calc_manhattan_distance(origin, point_1)), 20)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_2)), 20)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_3)), 20)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_4)), 20)

        self.assertEqual((MD.calc_manhattan_distance(origin, point_5)), 5)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_6)), 5)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_7)), 5)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_8)), 5)

        self.assertEqual((MD.calc_manhattan_distance(origin, point_9)), 15)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_10)), 15)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_11)), 147)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_12)), 5)
        self.assertEqual((MD.calc_manhattan_distance(origin, point_13)), 5)

        # to prove it works from points other than the origin
        self.assertEqual((MD.calc_manhattan_distance(point_1, point_13)), 19)
        self.assertEqual((MD.calc_manhattan_distance(point_2, point_5)), 15)
        self.assertEqual((MD.calc_manhattan_distance(point_3, point_6)), 15)
        self.assertEqual((MD.calc_manhattan_distance(point_1, origin)), 20)
        self.assertEqual((MD.calc_manhattan_distance(point_8, point_11)), 152)
        # ----------------------- end testing of points ----------------------- #


if __name__ == "__main__":
    unittest.main()