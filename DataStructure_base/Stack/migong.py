
#深度优先
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

dirs = [
	lambda x, y: (x + 1, y),
	lambda x, y: (x - 1, y),
	lambda x, y: (x, y - 1),
	lambda x, y: (x, y + 1)
]
#路径函数

#上右下左
def maze_path(x1, y1, x2, y2):
	stack = []
	stack.append((x1, y1))
	while (len(stack) > 0):
		curNode = stack[-1]  # 当前的节点,stack最后一个 坐标
		if curNode[0] == x2 and curNode[1] == y2:
			for p in stack:
				print(p)
			return True

		# x,y,四个方向，左： x-1,y右：x+1，上：x,y-1,下:x,y+1
		for dir in dirs:

			nextNode = dir(curNode[0], curNode[1])
			# 如果下一个节点能走
			if maze[nextNode[0]][nextNode[1]] == 0:
				stack.append(nextNode)
				maze[nextNode[0]][nextNode[1]] = 2  # 表示已经走过
				break

		else:
			maze[nextNode[0]][nextNode[1]] = 2
			stack.pop()
	else:
		print('++++++++++++++')
		print('没有路')
		return False


maze_path(1, 1, 8, 8)

#广度优先搜索：
def print_r(path):
	curNode = path[-1]
	realpath = []
	while curNode[2] != -1:
		realpath.append(curNode[0:2])
		# print(curNode[2])
		curNode = path[curNode[2]]
	realpath.append(curNode[0:2])
	realpath.reverse()
	
	for node in realpath:
		print(node)
		
		
		# print(node)



from collections import deque
def maze_path_queue(x1,y1,x2,y2):
	queue = deque()##创建队列
	queue.append((x1,y1,-1))#在队列中添加起点，并赋予起点在路径中的位置索引
	path =[]
	while len(queue)>0:
		curNode = queue.popleft()  #默认
		path.append(curNode)
		if curNode[0] == x2 and curNode[1] == y2:
			print_r(path)
			return True
		for dir in dirs:
			nextNode = dir(curNode[0],curNode[1])
			if maze[nextNode[0]][nextNode[1]] == 0:
				queue.append((nextNode[0],nextNode[1],len(path)-1))
				maze[nextNode[0]][nextNode[1]] =2
	else:
		print('+++++++++++++++++++++')
		print("没有路")
		return False
maze_path_queue(1,1,8,8)
# maze_path(1, 1, 8, 8)
			
		
	
			

	
	



