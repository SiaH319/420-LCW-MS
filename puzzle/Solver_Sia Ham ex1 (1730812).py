'''
Sia Ham, 17308123
Tuesday, February 19
R. Vincent, instructor
Assignment 2
'''

# Main program for assignment 2. Your job here is to finish the
# Solver class's __init__ method to solve the puzzle as described
# in the handout.
#
from MinPQ import MinPQ
from Board import Board

import functools
@functools.total_ordering
class Node(object):
    def __init__(self, bd, moves, node):
        '''Construct a new node object.'''
        self.board = bd         # save the board
        self.moves = moves      # number of moves to reach this board.
        self.cost = bd.distance() # save the mdistance metric.
        self.previous = node      # save the previous node.
    def __gt__(self, other):
        '''A node is 'greater' than another if the cost plus the
        number of moves is larger. Note that this code will fail
        if 'other' is None.'''
        return (self.cost + self.moves) > (other.cost + other.moves)
    def __eq__(self, other):
        '''Two nodes are equal if the sum of the cost and moves are
        the same. The board itself is ignored.'''
        if self is other:       # comparing to itself?
            return True
        if other is None:       # comparing to None
            return False
        return (self.cost + self.moves) == (other.cost + other.moves)

class Solver(object):
    def __init__(self, initial):
        '''Initialize the object by finding the solution for the
        puzzle.'''

        self.__solvable = False
        self.__trace = []

        puzzle_Node = Node(initial,0,None) #initial node
        puzzle_MinPQ = MinPQ() #initial priority queue
        puzzle_MinPQ.insert(puzzle_Node) #insert the inital node to the priority queue
        while not puzzle_MinPQ.isEmpty(): #as long as the priority queue is not empty
            current_node = puzzle_MinPQ.delMin() #remove the “best” Node (current_node) from the priority queue
            if not current_node.board.solved():  #if the current board is not solved 
                if current_node.previous == None: # if the parent node of the current node refers to None
                    n_board = current_node.board.neighbors() #neighbor boards of the current node
                    for n in n_board: 
                        nd = Node(n,current_node.moves + 1, current_node) #create new nodes
                        puzzle_MinPQ.insert(nd) #insert newly-created nodes into the priority queue.
                        
                else: # if the parent node of the current node does not refer to None
                    n_board = current_node.board.neighbors() #neighbor boards of the current node
                    for n in n_board:
                        if n != current_node.previous.board: # as long as it is not the samae as its parent board, insert onto the priority queue
                            nd = Node(n,current_node.moves+1,current_node) #create new nodes
                            puzzle_MinPQ.insert(nd) #insert newly-created nodes into the priority queue
                            
            else: #if the current board is the solved board
                while current_node.previous:
                    self.__trace = [current_node.board] + self.__trace #insert the current board as a list for tracing
                    current_node = current_node.previous
                self.__trace = [current_node.board] + self.__trace
                self.__solvable = True #solvable board
                print ("Minimum number of moves = ", min_move)
                break
                
    def solvable(self):
        '''Returns True if this puzzle can be solved.'''
        return self.__solvable;
  
    def moves(self):
        '''Returns the number of moves in the solution, or -1 if
        not solvable.'''
        return len(self.__trace) - 1 if self.__solvable else -1
  
    def solution(self):
        '''Returns the list of board positions in the solution.'''
        return self.__trace.copy()

B_initial =[]
arg = []
f_name = []
file = input("Please enter the name of the file to solve puzzle:")
fp = open('puzzles//' + file) #opend the selected file


while True: # keep reading
    line = fp.readline()
    if not line: break
    line=line.strip('\n') # remove EOLine
    data = line.split( )
    for tile in data:
        arg.append(int(tile)) #add each tile (number) in a list
arg.pop(0)

for char in file:
    f_name.append(char)
min_move = ''.join(f_name[10:12])    
    
B_initial = Board(arg) #create a Board object
s = Solver (B_initial)
result = s.solution() #all the boards and their movements are in a list
for i,j in enumerate(result):
    print('Move #' + str(i))
    print (str(j) + '\n') #__str__ from class Board 
