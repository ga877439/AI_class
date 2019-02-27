# python 2.7 version
#AI HW 0
class Solution(object):
	def numIslands(self,grid):
		'''
		type grid: List[List[str]]
		return type: int
		'''

		count = 0
		n = len(grid)
		try:
			m = len(grid[0])
		except:
			pass #just for in case
		
		
		
		def algorithm(row, coloum):
			
			grid[row][coloum] = '0'	#we should mark it as 'past' and move to other locations adjacent to 'the neighbor'.
			difference = [(1,0), (-1,0), (0,-1), (0,1)] #shift to the neighbor area
			# we need to first identify which neighbor is land 

			for i,j in difference:
				new_row, new_column = row+i,coloum+j

				if 0 <= new_row <= n-1 and 0 <= new_column <= m-1:	#if the new location is valid, then ...
					if	grid[new_row][new_column] == '1':		#if the new neighbor is land, keep doing the same thing
						algorithm(new_row,new_column)


						
		for i in range(n):
			for j in range(m):
				if grid[i][j] == '1':
					count += 1	
					grid[i][j] == '0' #marked as 'already past'
					algorithm(i,j)
		
		return count

		




if __name__ == "__main__":
	'''
	generated input
	'''
	grid = [['1','1','1'],['1','1','0']]
	sol = Solution()
	answer = sol.numIslands(grid)
	print answer





