import unittest
from run import Game

class TestRun(unittest.TestCase):
    def test_return_neighbours(self):
        board = Game(10,10)
        #first corner case
        the_cell = (0,0)
        produced_neighbours = board.return_neighbours(the_cell[0], the_cell[1])
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
        produced_neighbours = board.return_neighbours(the_cell[0], the_cell[1])
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



if __name__ == '__main__':
    unittest.main()
