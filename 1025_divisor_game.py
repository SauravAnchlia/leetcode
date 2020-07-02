'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn,
that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game,
assuming both players play optimally.

'''


class solution():
    def divisor_game(self, N: int) -> bool:
        return True if N % 2 == 0 else False
