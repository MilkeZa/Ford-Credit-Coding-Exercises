import unittest
import ManhattanDistance


class TestManhattanCalc(unittest.TestCase):
    def test_manhattan_calc(self):
        origin = ManhattanDistance.Point(0, 0)  # point to be measured from
        
        # testing corners
        point_1 = ManhattanDistance.Point(10, 10)
        point_2 = ManhattanDistance.Point(-10, 10)
        point_3 = ManhattanDistance.Point(10, -10)
        point_4 = ManhattanDistance.Point(-10, -10)
        
        # testing on the axes
        point_5 = ManhattanDistance.Point(-5, 0)
        point_6 = ManhattanDistance.Point(5, 0)
        point_7 = ManhattanDistance.Point(0, 5)
        point_8 = ManhattanDistance.Point(0, -5)

        # testing random points
        point_9 = ManhattanDistance.Point(1, 14)
        point_10 = ManhattanDistance.Point(-7, 8)
        point_11 = ManhattanDistance.Point(47, 100)
        point_12 = ManhattanDistance.Point(-3, 2)
        point_13 = ManhattanDistance.Point(3, -2)


        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_1)), 20)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_2)), 20)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_3)), 20)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_4)), 20)

        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_5)), 5)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_6)), 5)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_7)), 5)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_8)), 5)

        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_9)), 15)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_10)), 15)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_11)), 147)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_12)), 5)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(origin, point_13)), 5)

        # to prove it works from points other than the origin
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(point_1, point_13)), 19)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(point_2, point_5)), 15)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(point_3, point_6)), 15)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(point_1, origin)), 20)
        self.assertEqual((ManhattanDistance.calc_manhattan_distance(point_8, point_11)), 152)


if __name__ == "__main__":
    unittest.main()