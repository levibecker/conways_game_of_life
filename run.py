import numpy as np
import logging

logging.basicConfig(level=logging.ERROR)

class Game:
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width
        self.instantiate_map()

    def instantiate_map(self):
        self.map = np.zeros((self.heigth, self.width), dtype=int)
        logging.debug("map instantieted")

    def set_entity(self, y, x):
        self.map[y][x] = 1
        logging.debug(f"entity set on y = {y}, x = {x}")

    def kill_entity(self, y, x):
        self.map[y][x] = 0
        logging.debug(f"entity killed on y = {y}, x = {x}")

    def return_neighbours(self, y, x):
        """
        return indexes of the neigbours of the choosen cell
        every cell has eight neighbours, which are the cells that are
        horizontally, vertically, or diagonally adjacent
        """
        neighbours = [(a % self.heigth, b % self.width) for a in (y-1, y, y+1) for b in (x-1, x, x+1)]
        neighbours.remove((y % self.heigth, x % self.width))
        logging.debug(f"point {y}, x = {x} has 8 neigbours which are: {neighbours}")
        return neighbours

    def number_of_neigbours(self, y, x):
        """
        calculate how many cells are populated in the nearest neighbour of the choosen cell
        """
        neighbours = self.return_neighbours(y, x)
        values = []
        for neighbour in neighbours:
            y, x = neighbour
            values.append(self.map[y][x])
        number_of_neighbours = sum(values)
        logging.debug(f"point y = {y}, x = {x} has sum of neigbours equal to {number_of_neighbours}")
        return number_of_neighbours

    def populate_or_die(self, y, x):
        """
        Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        sum_of_neighbours = self.number_of_neigbours(y, x)
        is_alive = self.map[y][x]

        if is_alive:
            if sum_of_neighbours not in (2,3):
                logging.debug(f"cell y = {y}, x = {x} has died")
                return 0
            else:
                logging.debug(f"cell y = {y}, x = {x} stayed alive")
                return 1
        else:
            if sum_of_neighbours == 3:
                logging.debug(f"cell y = {y}, x = {x} has been born")
                return 1
            else:
                logging.debug(f"cell y = {y}, x = {x} is still dead")
                return 0

    def calculate_next_state(self):
        """
        checking every cell of the map to determine if it should
        be populated or killed in the next state of map
        and return new state based on that information
        """
        xs = range(self.width)
        ys = range(self.heigth)
        new_map = np.array([
        [self.populate_or_die(y,x) for x in xs] for y in ys
        ])
        return new_map

    def print_map(self):
        """
        printing current state of the game to the console
        """
        for row in self.map:
            print(" ".join([str(value) for value in row]))
        print("---")

if __name__ == "__main__":
    game = Game(7, 7)
    game.set_entity(6, 5)
    game.set_entity(4, 6)
    game.set_entity(5, 6)
    game.set_entity(5, 5)
    game.set_entity(6, 4)
    game.set_entity(3, 2)
    game.set_entity(0, 3)
    game.set_entity(2, 4)
    game.print_map()
    for _ in range(20):
        game.map = game.calculate_next_state()
        game.print_map()
