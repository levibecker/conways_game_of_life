import unittest
import numpy as np
from run import Game

class TestRun(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.board = Game(10, 10)
        self.board.set_entity(6, 5)
        self.board.set_entity(4, 6)
        self.board.set_entity(5, 6)
        self.board.set_entity(5, 7)
        self.board.set_entity(6, 7)
        self.board.set_entity(0, 9)
        self.board.set_entity(0, 8)
        self.board.set_entity(8, 9)

    def test_initial_value(self):
        init_setup = Game(3, 4)
        self.assertEqual(init_setup.heigth, 3)
        self.assertEqual(init_setup.width, 4)
        expected_map = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        self.assertTrue((expected_map == init_setup.map).all())

    def test_instantiate_map(self):
        self.board.instantiate_map()
        produced_result = self.board.map
        expected_result = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        #comparing two arrays produce array of booleans
        self.assertTrue((produced_result == expected_result).all())

    def test_set_entity(self):
        self.board.set_entity(0,0)
        produced_result = self.board.map
        expected_result = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertTrue((produced_result == expected_result).all())

    def test_kill_entity(self):
        self.board.kill_entity(0,9)
        produced_result = self.board.map
        expected_result = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        self.assertTrue((produced_result == expected_result).all())

    def test_return_neighbours(self):
        #first corner case
        the_cell = (0,0)
        produced_neighbours = self.board.return_neighbours(the_cell[0], the_cell[1])
        expected_neighbours = [
        (9, 9),
        (9, 0),
        (9, 1),
        (0, 9),
        (0, 1),
        (1, 9),
        (1, 0),
        (1, 1)
        ]
        self.assertEqual(produced_neighbours, expected_neighbours)
        #second corner case
        the_cell = (9,9)
        produced_neighbours = self.board.return_neighbours(the_cell[0], the_cell[1])
        expected_neighbours = [
        (8, 8),
        (8, 9),
        (8, 0),
        (9, 8),
        (9, 0),
        (0, 8),
        (0, 9),
        (0, 0)
        ]
        self.assertEqual(produced_neighbours, expected_neighbours)
        #third corner case
        the_cell = (0,9)
        produced_neighbours = self.board.return_neighbours(the_cell[0], the_cell[1])
        expected_neighbours = [
        (9, 8),
        (9, 9),
        (9, 0),
        (0, 8),
        (0, 0),
        (1, 8),
        (1, 9),
        (1, 0)
        ]
        self.assertEqual(produced_neighbours, expected_neighbours)
        #fourth corner case
        the_cell = (9,0)
        produced_neighbours = self.board.return_neighbours(the_cell[0], the_cell[1])
        expected_neighbours = [
        (8, 9),
        (8, 0),
        (8, 1),
        (9, 9),
        (9, 1),
        (0, 9),
        (0, 0),
        (0, 1)
        ]
        self.assertEqual(produced_neighbours, expected_neighbours)
        #mid map case
        the_cell = (5,5)
        produced_neighbours = self.board.return_neighbours(the_cell[0], the_cell[1])
        expected_neighbours = [
        (4, 4),
        (4, 5),
        (4, 6),
        (5, 4),
        (5, 6),
        (6, 4),
        (6, 5),
        (6, 6)
        ]
        self.assertEqual(produced_neighbours, expected_neighbours)

    def test_number_of_neigbours(self):
        #middle case - dead cell
        the_cell = (5,5)
        produced_sum = self.board.number_of_neigbours(the_cell[0], the_cell[1])
        expected_sum = 3
        self.assertEqual(produced_sum, expected_sum)

        #middle case 2 - zero neigbours
        the_cell = (1,1)
        produced_sum = self.board.number_of_neigbours(the_cell[0], the_cell[1])
        expected_sum = 0
        self.assertEqual(produced_sum, expected_sum)

        #middle case 3 - alive cell
        the_cell = (5,7)
        produced_sum = self.board.number_of_neigbours(the_cell[0], the_cell[1])
        expected_sum = 3
        self.assertEqual(produced_sum, expected_sum)

        #corner case - sum over board
        the_cell = (9,8)
        produced_sum = self.board.number_of_neigbours(the_cell[0], the_cell[1])
        expected_sum = 3
        self.assertEqual(produced_sum, expected_sum)

    def test_populate_or_die(self):
        #middle case - a dead cell gonna be born
        the_cell = (5,5)
        produced_result = self.board.populate_or_die(the_cell[0], the_cell[1])
        expected_result = 1
        self.assertEqual(produced_result, expected_result)

        #middle case - a dead cell gonna be dead
        the_cell = (1,1)
        produced_result = self.board.populate_or_die(the_cell[0], the_cell[1])
        expected_result = 0
        self.assertEqual(produced_result, expected_result)

        #middle case - an alive cell gonna live
        the_cell = (5,7)
        produced_result = self.board.populate_or_die(the_cell[0], the_cell[1])
        expected_result = 1
        self.assertEqual(produced_result, expected_result)

        #middle case - an alive cell gonna die (overpopulation)
        the_cell = (5,6)
        produced_result = self.board.populate_or_die(the_cell[0], the_cell[1])
        expected_result = 0
        self.assertEqual(produced_result, expected_result)

        #middle case - an alive cell gonna die (solitude)
        the_cell = (8,9)
        produced_result = self.board.populate_or_die(the_cell[0], the_cell[1])
        expected_result = 0
        self.assertEqual(produced_result, expected_result)

    def test_calculate_next_state(self):
        produced_result = self.board.calculate_next_state()
        expected_result = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        ])

        self.assertTrue((produced_result == expected_result).all())


if __name__ == '__main__':
    unittest.main()
