def decide(state, alpha, beta, maxTurn):
    # determining final state
    if (sum(state) == 1 and maxTurn) or (sum(state) == 0 and not maxTurn): return (-1, [state])
    if (sum(state) == 1 and not maxTurn) or (sum(state) == 0 and maxTurn): return (1, [state])
    if maxTurn:
        res_max = -float('inf')
        res = None
        for i in find_next(state):
            # recursively search for the next possible move
            val, temp = decide(i, alpha, beta, not maxTurn)
            if val > res_max:
                res_max = val
                res = temp
            # update the upper bound
            alpha = max(alpha, val)
            # pruning
            if alpha >= beta:
                break
        return res_max, [state] + res
    else:
        res_min = float('inf')
        res = None
        for i in find_next(state):
            val, temp = decide(i, alpha, beta, not maxTurn)
            if val < res_min:
                res_min = val
                res = temp
            beta = min(beta, val)
            if alpha >= beta:
                break
        return res_min, [state] + res
    
# find all possible next moves
def find_next(state):
    visited = set()
    res = []
    for i in range(len(state)):
        for m in range(1, state[i] + 1):
            temp = list(state[:])
            temp[i] -= m
            rearranged = tuple(sorted(temp))
            if rearranged not in visited:
                res.append(temp)
                visited.add(rearranged)
    return res
class Board(object):
    def __init__(self, board):
        self.board = board
    def update(self, piles, num):
        self.board[piles] -= num
    def computerUpdate(self):
        self.board = decide(self.board, -float('inf'), float('inf'), True)[1][1]

# check whether user input is valid
def isValid(remove, board):
    if not remove or len(remove) != 2: return False
    if remove[0] > 0 and remove[1] >= 0 and remove[1] < len(board) and remove[0] <= board[remove[1]]:
        return True
    return False

if __name__ == "__main__":
    # initializing size of the game board
    ele = int(input("Enter the number of piles: "))
    lis = []

    print("Enter the number of sticks in each pile.")
    for _ in range(ele):
        lis.append(int(input()))

    game = Board(lis)
    print("Enter the number of sticks to remove, then space followed by the pile to remove them from (starting from 0)")
    print("The person who removes the last stick loses!")
    print("Example: to remove 3 sticks from pile 2, enter 3 2")

    player_win = True
    while True:
       
        print("Pile state %s" % (game.board))

        # player's turn
        user = str(input("Player turn: "))
        player_remove = [int(i) for i in user.split(' ')]

        while not isValid(player_remove, game.board):
            print("Invalid move! Please input again.")
            user = str(input("Player turn: "))
            player_remove = [int(i) for i in user.split(' ')]

        game.update(player_remove[1], player_remove[0])

        if sum(game.board) == 0:
            player_win = False
            break
        elif sum(game.board) == 1:
            break

        print("Computer turn")
        game.computerUpdate()

        if sum(game.board) == 0:
            break
        elif sum(game.board) == 1:
            player_win = False
            break

    if player_win:
        print(game.board)
        print("You won!")
    else:
        print(game.board)
        print("You lost!")