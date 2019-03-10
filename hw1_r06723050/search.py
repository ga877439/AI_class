# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    path_for_return = []
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    w = Directions.WEST
    s = Directions.SOUTH
    PQ = util.PriorityQueue()
    
    current_location = problem.getStartState()
    
    PQ.push( ([], current_location), 0)

    
    poped_loc = [] 
    while not PQ.isEmpty():

        
        path, current_location = PQ.pop()


        if not  problem.isGoalState(current_location) :
            if current_location not in  poped_loc:
                poped_loc.append(current_location)
                nodes = problem.getSuccessors(current_location)
                for node in nodes:
                    loc, direct, cost = node
                        
                    if loc not in poped_loc:
                        
                        priority = -1 * len(path)
                        
                        PQ.push( (path+[direct],loc), priority )
                    

        else:
            
            for directions in path:
                if directions == 'North':
                    path_for_return.append(n)
                elif directions == 'East':
                    path_for_return.append(e)
                elif directions == 'West':
                    path_for_return.append(w)
                elif directions == 'South':
                    path_for_return.append(s)
                else:
                    path_for_return.append(directions)
            break
    return  path_for_return

        
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    path_for_return = []
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    w = Directions.WEST
    s = Directions.SOUTH
    PQ = util.PriorityQueue()
    
    current_location = problem.getStartState()
    
    PQ.push( ([], current_location), 0)

    
    poped_loc = [] 
    while not PQ.isEmpty():

        
        path, current_location = PQ.pop()


        if not  problem.isGoalState(current_location) :
            if current_location not in  poped_loc:
                poped_loc.append(current_location)
                nodes = problem.getSuccessors(current_location)
                for node in nodes:
                    loc, direct, cost = node
                        
                    if loc not in poped_loc:
                        
                        priority = len(path)
                        
                        PQ.push( (path+[direct],loc), priority )
                    

        else:
            
            for directions in path:
                if directions == 'North':
                    path_for_return.append(n)
                elif directions == 'East':
                    path_for_return.append(e)
                elif directions == 'West':
                    path_for_return.append(w)
                elif directions == 'South':
                    path_for_return.append(s)
                else:
                    path_for_return.append(directions)
            break
    return  path_for_return

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    path_for_return = []
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    w = Directions.WEST
    s = Directions.SOUTH
    PQ = util.PriorityQueue()
    
    current_location = problem.getStartState()
    

    total_cost_of_path = 0
    PQ.push( ([], current_location, total_cost_of_path ), total_cost_of_path )

    
    poped_loc = [] 
    while not PQ.isEmpty():

        
        path, current_location, total_cost_of_path = PQ.pop()
		
        if not  problem.isGoalState(current_location) :
            if current_location not in  poped_loc:
                poped_loc.append(current_location)
                nodes = problem.getSuccessors(current_location)
            for node in nodes:
                loc, direct, cost = node
                
                if loc not in poped_loc:

                    
                    priority = total_cost_of_path + cost 
                    
                    PQ.push( ( path+[direct],loc, total_cost_of_path + cost), priority )
                    

        else:
        
            for directions in path:
                if directions == 'North':
                    path_for_return.append(n)
                elif directions == 'East':
                    path_for_return.append(e)
                elif directions == 'West':
                    path_for_return.append(w)
                elif directions == 'South':
                    path_for_return.append(s)
                else:
                    path_for_return.append(directions)
            break    
    return  path_for_return

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    path_for_return = []
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    w = Directions.WEST
    s = Directions.SOUTH
    PQ = util.PriorityQueue()
    
    current_location = problem.getStartState()
    
    h = heuristic(current_location, problem)
    total_cost_of_path = 0
    PQ.push( ([], current_location, total_cost_of_path ), total_cost_of_path + h)

    
    poped_loc = [] 
    while not PQ.isEmpty():

        
        path, current_location, total_cost_of_path = PQ.pop()
        if not  problem.isGoalState(current_location) :
            if current_location not in  poped_loc:
                poped_loc.append(current_location)
                nodes = problem.getSuccessors(current_location)
            for node in nodes:
                loc, direct, cost = node
                
                if loc not in poped_loc:
                    h = heuristic(loc, problem)
                    
                    priority = total_cost_of_path + cost + h
                    
                    PQ.push( (path+[direct], loc, total_cost_of_path + cost), priority )
                    

        else:
        
            for directions in path:
                if directions == 'North':
                    path_for_return.append(n)
                elif directions == 'East':
                    path_for_return.append(e)
                elif directions == 'West':
                    path_for_return.append(w)
                elif directions == 'South':
                    path_for_return.append(s)
                else:
                    path_for_return.append(directions)
            break        
    return  path_for_return


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch




