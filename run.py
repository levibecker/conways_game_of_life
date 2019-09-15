import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

def increment(number):
    """
    function that returns incremented number

    arguments:
        number - a whole number to incremet
    """
    if isinstance(number, int):
        return number + 1
    else:
        return 'you can only increment whole numbers!'

class Game:
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width
        self.instantiate_map()

    def instantiate_map(self):
        self.map = np.zeros((self.heigth, self.width), dtype=int)

    def set_entity(self, y, x):
        self.map[y][x] = 1

    def kill_entity(self, y, x):
        self.map[y][x] = 0

    def return_neighbours(self, y, x):
        neighbours = [(a % self.heigth, b % self.width) for a in (y-1, y, y+1) for b in (x-1, x, x+1)]
        neighbours.remove((y % self.heigth, x % self.width))
        return neighbours

    def neighbours_sum(self, y, x):
        neighbours = self.return_neighbours(y, x)
        values = []
        for neighbour in neighbours:
            y, x = neighbour
            values.append(self.map[y][x])
        return sum(values)

    def born_or_kill(self, y, x):
        sum_of_neighbours = self.neighbours_sum(y, x)
        is_alive = self.map[y][x]

        if is_alive:
            if sum_of_neighbours not in (2,3):
                return 0
            else:
                return 1
        else:
            if sum_of_neighbours == 3:
                return 1
            else:
                return 0

    def calculate_next_state(self):
        map = []
        for y in range(self.heigth):
            row = []
            for x in range(self.width):
                row.append(self.born_or_kill(y,x))
            map.append(row)
        return np.array(map)

    def print_map(self):
        for row in self.map:
            print(" ".join([str(value) for value in row]))
        print("---")

if __name__ == "__main__":
    game = Game(10,10)
    game.set_entity(6, 5)
    game.set_entity(4, 6)
    game.set_entity(5, 6)
    game.set_entity(5, 7)
    game.set_entity(6, 7)
    game.print_map()
    for _ in range(50):
        game.map = game.calculate_next_state()
        game.print_map()
