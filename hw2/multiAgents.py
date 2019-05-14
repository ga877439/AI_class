# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
	"""
	  A reflex agent chooses an action at each choice point by examining
	  its alternatives via a state evaluation function.

	  The code below is provided as a guide.  You are welcome to change
	  it in any way you see fit, so long as you don't touch our method
	  headers.
	"""


	def getAction(self, gameState):
		"""
		You do not need to change this method, but you're welcome to.

		getAction chooses among the best options according to the evaluation function.

		Just like in the previous project, getAction takes a GameState and returns
		some Directions.X for some X in the set {North, South, West, East, Stop}
		"""
		# Collect legal moves and successor states
		legalMoves = gameState.getLegalActions()

		# Choose one of the best actions
		scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		"Add more of your code here if you want to"

		return legalMoves[chosenIndex]

	def evaluationFunction(self, currentGameState, action):
		"""
		Design a better evaluation function here.

		The evaluation function takes in the current and proposed successor
		GameStates (pacman.py) and returns a number, where higher numbers are better.

		The code below extracts some useful information from the state, like the
		remaining food (newFood) and Pacman position after moving (newPos).
		newScaredTimes holds the number of moves that each ghost will remain
		scared because of Pacman having eaten a power pellet.

		Print out these variables to see what you're getting, then combine them
		to create a masterful evaluation function.
		"""
		# Useful information you can extract from a GameState (pacman.py)
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()
		newGhostStates = successorGameState.getGhostStates()
		newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
		
		
		"*** YOUR CODE HERE ***"
		if action == 'Stop':	#never stop
			
			return -1000000
		score = 0	#the score that will be returned
		
		#if now_pos has food plus many score:
		currentFood = currentGameState.getFood()

		if currentFood[newPos[0]][newPos[1]] == True :	#if we can eat the food next to us, we should eat it, unless it will lead to lose
			score += 10000
		 

		
		#find the nearest food location
		min_food_distance = 1000000	
		food_list = newFood.asList()
		if len(food_list) > 0:
			for food in food_list:
				distance =  abs(food[0] - newPos[0]) + abs(food[1] - newPos[1])
				if distance < min_food_distance:
					min_food_distance = distance
		else:
			min_food_distance = 0
		
		#find the nearest ghost location		
		min_ghost_distance = 100000
		for ghost_state in newGhostStates:
			ghost_position = ghost_state.getPosition()
			distance = abs(ghost_position[0] - newPos[0]) + abs(ghost_position[1] - newPos[1])
			if distance < min_ghost_distance:
				min_ghost_distance = distance
				
			
		
		return  score - float(min_food_distance) / ( min_ghost_distance + 0.0000001)	#it means that we should approach the place where there is a food or minimizing the fraction of food to ghost

		
		
def scoreEvaluationFunction(currentGameState):
	"""
	  This default evaluation function just returns the score of the state.
	  The score is the same one displayed in the Pacman GUI.

	  This evaluation function is meant for use with adversarial search agents
	  (not reflex agents).
	"""
	return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
	"""
	  This class provides some common elements to all of your
	  multi-agent searchers.  Any methods defined here will be available
	  to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

	  You *do not* need to make any changes here, but you can if you want to
	  add functionality to all your adversarial search agents.  Please do not
	  remove anything, however.

	  Note: this is an abstract class: one that should not be instantiated.  It's
	  only partially specified, and designed to be extended.  Agent (game.py)
	  is another abstract class.
	"""

	def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
		self.index = 0 # Pacman is always agent index 0
		self.evaluationFunction = util.lookup(evalFn, globals())
		self.depth = int(depth)

		
	def get_all_successor_of_legal_moves(self, state, play_id):
		actions = state.getLegalActions(play_id)
		successors = []
		for action in actions:
			successors.append(	state.generateSuccessor(play_id, action)	)
		return successors		
		
class MinimaxAgent(MultiAgentSearchAgent):			#problem :don't know how to inplement depth control
													#maybe everytime I should notice whether three are some actions to expand  
	"""
	  Your minimax agent (question 2)
	"""

	
	def value(self, state, is_terminal, depth, next_agent_to_move ):
		if is_terminal or depth >= self.depth:
			return self.evaluationFunction(state)		#self.value(gameState, True)
	
		if next_agent_to_move == 0:
			return self.max_value(state, depth, next_agent_to_move)
		else:
			return self.min_value(state, depth, next_agent_to_move)
		
	def max_value(self,state, depth, agent_to_move):
		#basic calculation
		successors = self.get_all_successor_of_legal_moves(state, agent_to_move)	
		
		next_agent_to_move = agent_to_move + 1
		#find the max value
		v = -100000000
		for successor in successors:
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			
			successor_value = self.value(successor, is_terminal, depth, next_agent_to_move)
			if successor_value > v:
				v = successor_value

		return v
		
	def min_value(self,state,  depth, agent_to_move):
			
		#basic calculation
		successors = self.get_all_successor_of_legal_moves(state, agent_to_move)	#e.g.  agent_to_move = 1 
		
		
		
		#determine which player to move, and the depth and the next agent(which decides which function to call: Min or Max)
		if agent_to_move < self.total_agent - 1:	#if there are second ghosts
			next_agent_to_move = agent_to_move + 1  	#update id

		elif agent_to_move == self.total_agent - 1:	#but if this agent is last ghost
			depth += 1	#all ghost have played once => add one depth
			next_agent_to_move = 0		#next agent to move = pacman

		
		
		
		#find the min value
		v = 100000000
		for successor in successors:
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			
			successor_value = self.value(successor, is_terminal, depth, next_agent_to_move)
			if successor_value < v:
				v = successor_value
	
		return v
		
	
	def getAction(self, gameState):
		"""
		  Returns the minimax action from the current gameState using self.depth
		  and self.evaluationFunction.

		  Here are some method calls that might be useful when implementing minimax.

		  gameState.getLegalActions(agentIndex):
			Returns a list of legal actions for an agent
			agentIndex=0 means Pacman, ghosts are >= 1

		  gameState.generateSuccessor(agentIndex, action):
			Returns the successor game state after an agent takes an action

		  gameState.getNumAgents():
			Returns the total number of agents in the game
		"""


		self.total_agent = gameState.getNumAgents()
		
		
		actions = gameState.getLegalActions(0)
		successors = []
		for action in actions:
			successors.append(	gameState.generateSuccessor(0, action)	)
			
		scores = []
		for successor in successors:
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			
			successor_value = self.value(successor, is_terminal, 0, 1)
			scores.append(successor_value)
		
		
		# Choose one of the best actions

		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		return actions[chosenIndex]		
		 
		


class AlphaBetaAgent(MultiAgentSearchAgent):
	"""
	  Your minimax agent with alpha-beta pruning (question 3)
	"""
	def value(self, state, is_terminal, depth, next_agent_to_move, alpha, beta ):
		if is_terminal or depth >= self.depth:
			return self.evaluationFunction(state)		#self.value(gameState, True)
	
		if next_agent_to_move == 0:
			return self.max_value(state, depth, next_agent_to_move, alpha, beta )
		else:
			return self.min_value(state, depth, next_agent_to_move, alpha, beta )
		
	def max_value(self,state, depth, agent_to_move, alpha, beta):
		#basic calculation
		actions = state.getLegalActions(agent_to_move)	
		
		next_agent_to_move = agent_to_move + 1
		#find the max value
		v = -100000000
		for action in actions:
			successor = state.generateSuccessor(agent_to_move, action)
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			#get value
			successor_value = self.value(successor, is_terminal, depth, next_agent_to_move, alpha, beta)
			if successor_value > v:
				v = successor_value
				if v > beta:
					return v
			alpha  = max( alpha, v)	#update alpha
			if alpha > beta :
				return alpha
		return v
		
	def min_value(self,state,  depth, agent_to_move, alpha, beta):
			
		#basic calculation
		actions = state.getLegalActions(agent_to_move)	
		
		
		
		#determine which player to move, and the depth and the next agent(which decides which function to call: Min or Max)
		if agent_to_move < self.total_agent - 1:	#if there are second ghosts
			next_agent_to_move = agent_to_move + 1  	#update id

		elif agent_to_move == self.total_agent - 1:	#but if this agent is last ghost
			depth += 1	#all ghost have played once => add one depth
			next_agent_to_move = 0		#next agent to move = pacman

		
		
		
		#find the min value
		v = 100000000
		for action in actions:
			successor = state.generateSuccessor(agent_to_move, action)
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			#get value
			successor_value = self.value(successor, is_terminal, depth, next_agent_to_move, alpha, beta)
			
			
			if successor_value < v:
				v = successor_value
				if v < alpha:	
					return v
			beta  = min( beta, v)	#update beta
			if alpha > beta :
				return beta
		return v	
		
	def getAction(self, gameState):
		"""
		  Returns the minimax action using self.depth and self.evaluationFunction
		"""

		self.total_agent = gameState.getNumAgents()
		alpha = -10000000
		beta = 100000000
		
		actions = gameState.getLegalActions(0)

			
		scores = []
		for action in actions:
			successor = gameState.generateSuccessor(0, action)
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			#get value
			successor_value = self.value(successor, is_terminal, 0, 1, alpha, beta)
			
			
			scores.append(successor_value)						
			alpha  = max( alpha, successor_value)	#update alpha

		# Choose one of the best actions

		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best



		return actions[chosenIndex]		
		 

class ExpectimaxAgent(MultiAgentSearchAgent):
	"""
	  Your expectimax agent (question 4)
	"""
	def value(self, state, is_terminal, depth, next_agent_to_move ):
		if is_terminal or depth >= self.depth:
			return self.evaluationFunction(state)		#self.value(gameState, True)
	
		if next_agent_to_move == 0:
			return self.max_value(state, depth, next_agent_to_move)
		else:
			return self.expect_value(state, depth, next_agent_to_move)
		
	def max_value(self,state, depth, agent_to_move):
		#basic calculation
		successors = self.get_all_successor_of_legal_moves(state, agent_to_move)	
		
		next_agent_to_move = agent_to_move + 1
		#find the max value
		v = -100000000
		for successor in successors:
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			
			successor_value = self.value(successor, is_terminal, depth, next_agent_to_move)
			if successor_value > v:
				v = successor_value

		return v
		
	def expect_value(self,state,  depth, agent_to_move):
		
		#basic calculation
		successors = self.get_all_successor_of_legal_moves(state, agent_to_move)	#e.g.  agent_to_move = 1 
		
		
		
		#determine which player to move, and the depth and the next agent(which decides which function to call: Min or Max)
		if agent_to_move < self.total_agent - 1:	#if there are second ghosts
			next_agent_to_move = agent_to_move + 1  	#update id

		elif agent_to_move == self.total_agent - 1:	#but if this agent is last ghost
			depth += 1	#all ghost have played once => add one depth
			next_agent_to_move = 0		#next agent to move = pacman

		
		
		
		#find the min value
		v = 0
		total_outcome = len(successors)
		for successor in successors:
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			
			successor_value = self.value(successor, is_terminal, depth, next_agent_to_move)
			v += (1. / total_outcome) * successor_value
	
		return v
	
	
	
	
	def getAction(self, gameState):
		"""
		  Returns the expectimax action using self.depth and self.evaluationFunction

		  All ghosts should be modeled as choosing uniformly at random from their
		  legal moves.
		"""
		self.total_agent = gameState.getNumAgents()
		
		
		actions = gameState.getLegalActions(0)
		successors = []
		for action in actions:
			successors.append(	gameState.generateSuccessor(0, action)	)
			
		scores = []
		for successor in successors:
			if not successor.isLose() and not successor.isWin():
				is_terminal = False
			else:
				is_terminal = True
			
			successor_value = self.value(successor, is_terminal, 0, 1)
			scores.append(successor_value)
		
		
		# Choose one of the best actions

		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		return actions[chosenIndex]		
		 

def betterEvaluationFunction(currentGameState):
	"""
	  Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
	  evaluation function (question 5).

	  DESCRIPTION: <write something here so we know what you did>
	"""
	"*** YOUR CODE HERE ***"
	util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

