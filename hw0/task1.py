#hw0 task1

class Node(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def sumOfLeftLeaves(self, root):
		'''
		type root: Node
		return type: int
		'''
		#the following is my code. My intuition is that given the location of a layer, I add all of the Node into a list, from which I extract the Node info.

		count = 0
		list = [root]
		if root != None:
			list = [root]

			while True:
				if len(list) == 0:
					break
				tem_list = []
				for nodes in list:
					if nodes.left != None:
						if nodes.left.left == None and nodes.left.right == None:		#if a left node has not other branches, we call it the last left node, which is needed to be caculated
							count += nodes.left.val
						else:	
							tem_list.append(nodes.left)

					if nodes.right != None:
						tem_list.append(nodes.right)
				list = tem_list

		return count
			
		

if __name__ == '__main__':
	#built tree
	root = Node(3)
	root.left = Node(9)
	root.right = Node(20)
	root.right.left = Node(15)
	root.right.right = Node(7)
	sol = Solution()
	print (sol.sumOfLeftLeaves(root))