import queue

# exist or not
def safe(row, col):
	# debug
	#print("row:{}, col:{}".format(row, col), end=" ")
	if row >= 0 and row < mapsRow and col >=0 and col < mapsCol:
		if visited[row][col] == 0:
			visited[row][col] = 1
			#print("is safe!\n")
			return 1
		else:
			#print("has visited!\n");	
			return 0	
	else:
		#print("is not exist!\n");
		return 0	

# breadth first search
def BFS(row, col):
	q = queue.Queue()
	
	q.put((row,col))

	while not q.empty():
		loc = q.get()
		
		# debug
		print("loc: ({}, {})".format(loc[0], loc[1]), end="\n")
		
		# new location
		newRow = loc[0]
		newCol = loc[1]

		#visited[newRow][newCol] = 1
	
		# search neighbor
		for i in range (0,len(x)):
			# exist and have not visited yet
			if safe(newRow + x[i], newCol + y[i]) and maps[newRow + x[i]][newCol + y[i]] == 1: 
				# put into queue
				q.put((newRow + x[i], newCol + y[i]))
				# debug
				print("put ({}, {})".format(newRow + x[i], newCol + y[i]), end="\n");
		
		# debug			
		#print("visited: {}".format(visited), end="\n")						

# deep first search
def DFS(row, col):
	
	# debug
	print("loc: ({}, {})".format(row, col), end="\n")

	# search neighbor
	for i in range (0,len(x)):
	# exist and have not visited yet
		if safe(row + x[i], col + y[i]) and maps[row + x[i]][col + y[i]] == 1: 
			DFS(row + x[i], col + y[i])

def countIslands(row, col, maps):
	count = 0

	for row in range (mapsRow):
		for col in range (mapsCol):
			if visited[row][col] == 0:
				visited[row][col] = 1
				if maps[row][col] == 1:
					count += 1		
					# breadth first search
					BFS(row, col)
					# deep first search
					# DFS(row, col)

	return count

# map
#maps = [[1,0,1],[1,1,1]]
#maps = [[1, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 0]]
maps = [[1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0]]
print("maps:{}\n".format(maps))

mapsRow = len(maps)
mapsCol = len(maps[0])

# init 
visited = [[0 for col in range (mapsCol)] for row in range (mapsRow)]

# neighbors
x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]

# result
print(countIslands(mapsRow, mapsCol, maps))



