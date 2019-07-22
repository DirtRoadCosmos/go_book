from dlgo import agent
from dlgo.agent import naive
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time

def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        time.sleep(.01)


        # print("selecting a move...")
        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)
        # print("selected move:", end=" ")
        print("\n" * 80) #print(chr(27) + "[2J")
        print_board(game.board)
        print_move(game.next_player, bot_move)
        # input("apply move? ")


        # print("move applied")

        # print("new board")
if __name__ == '__main__':
    main()
