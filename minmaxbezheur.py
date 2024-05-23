import random
import copy
from exceptions import AgentException


class MinMaxAgentbez:
    def __init__(self, my_token='x', depth=4):
        self.my_token = my_token
        self.opponent_token = 'o' if my_token == 'x' else 'x'
        self.depth = depth

    def decide(self, connect4):
        _, column = self.minmax(connect4, self.depth, True)
        return column if column is not None else random.choice(connect4.possible_drops())

    def minmax(self, board, depth, maximizingPlayer):
        if board.game_over:
            if board.wins == self.my_token:
                return 1, None
            elif board.wins == self.opponent_token:
                return -1, None
            else:
                return 0, None

        if depth == 0:
            return 0, None

        if maximizingPlayer:
            maxEval = float('-inf')
            best_column = None
            for column in board.possible_drops():
                temp_board = copy.deepcopy(board)
                temp_board.drop_token(column)
                eval, _ = self.minmax(temp_board, depth - 1, False)
                if eval > maxEval:
                    maxEval = eval
                    best_column = column
            return maxEval, best_column
        else:
            minEval = float('inf')
            best_column = None
            for column in board.possible_drops():
                temp_board = copy.deepcopy(board)
                temp_board.drop_token(column)
                eval, _ = self.minmax(temp_board, depth - 1, True)
                if eval < minEval:
                    minEval = eval
                    best_column = column
            return minEval, best_column


