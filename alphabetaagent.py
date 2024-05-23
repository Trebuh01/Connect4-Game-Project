import copy
class AlphaBetaAgent:
    def __init__(self, my_token='x', depth=4):
        self.my_token = my_token
        self.opponent_token = 'o' if my_token == 'x' else 'x'
        self.depth = depth

    def decide(self, connect4):
        _, column = self.alphabeta(connect4, self.depth, float('-inf'), float('inf'), True)
        return column

    def alphabeta(self, board, depth, alpha, beta, maximizingPlayer):
        if board.game_over:
            if board.wins == self.my_token:
                return 1, None
            elif board.wins == self.opponent_token:
                return -1, None
            else:
                return 0, None

        if depth == 0:
            return self.heuristic(board), None

        if maximizingPlayer:
            value = float('-inf')
            best_column = None
            for column in board.possible_drops():
                temp_board = copy.deepcopy(board)
                temp_board.drop_token(column)
                eval, _ = self.alphabeta(temp_board, depth-1, alpha, beta, False)
                if eval > value:
                    value = eval
                    best_column = column
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, best_column
        else:
            value = float('inf')
            best_column = None
            for column in board.possible_drops():
                temp_board = copy.deepcopy(board)
                temp_board.drop_token(column)
                eval, _ = self.alphabeta(temp_board, depth-1, alpha, beta, True)
                if eval < value:
                    value = eval
                    best_column = column
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, best_column

    def heuristic(self, board):
        score = 0

        center_column_index = board.width // 2
        center_count = sum([1 for row in range(board.height) if board.board[row][center_column_index] == self.my_token])
        score += center_count * 0.3

        for four in board.iter_fours():
            my_tokens = four.count(self.my_token)
            opp_tokens = four.count(self.opponent_token)
            if my_tokens > 0 and opp_tokens == 0:
                score += (my_tokens / 4)
            elif opp_tokens > 0 and my_tokens == 0:
                score -= (opp_tokens / 4)

        score = score / 40

        return score
