from models import *

if __name__ == "__main__":
    game = LocalGame()
    josue = game.add_player("Josue")
    marleoni = game.add_player("Marleoni")

    game.start_game()
    print game.launch_dices()
    # game.run_simulation()
    # xjosue = Player('Josue')
    # game.buy_property('ventnor', josue)
    # print game.players

    # print josue
    # game.buy_property('ventnor', roberto)
    # josue.buy_property('ventnor')
    # josue.buy_property('atlantico')
    # josue.buy_property('marvin')

    # josue.add_house('ventnor')
