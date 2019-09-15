from game.core import Game

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
