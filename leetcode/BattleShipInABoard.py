'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
 

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
'''

#Time complexity = O(M*N) and space Complexity =O(1)
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        ans=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    if i == j == 0:
                        ans+=1
                    elif i==0:
                        if(board[i][j-1] != 'X'):
                            ans+=1
                    elif j==0:
                        if(board[i-1][j] != 'X'):
                            ans+=1
                    else:
                        if(board[i-1][j] != 'X' and board[i][j-1] != 'X'):
                            ans+=1
        return ans

        
n=int(input.split())
s=[input().split() for i in range(n)]
print(Solution.countBattleships(Solution,s))