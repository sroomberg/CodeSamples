
class CGOL:

	def __init__(self, size):
		self.size = size
		self.cells = []
		for i in range(0, self.size):
			self.cells.append([])
			for j in range(0, self.size):
				self.cells[i][j].append(Cell(j,i,0)) # init all cells to off

	def set_pieces(self):
		print('HINT: You may only turn pieces on. The lifecycle will turn them off.')

		ran_once = False
		while 1:
			if ran_once:
				cont = input('Would you like to add a piece? (y or n) ')
				if cont.strip() == 'n':
					break
			else:
				ran_once = True

			x = int(input('X value (0-' + self.size - 1 + '): '))
			y = int(input('Y value (0-' + self.size - 1 + '): '))

			if x >= self.size or y >= self.size:
				print('Invalid Coordinates!')
			else:
				self.cells[y][x].set_state(1)

	def run_once(self):
		for i in range(0, self.size):
			for j in range(0, self.size):
				current_cell = self.cells[i][j]
				num_neighbors = get_neighbors(current_cell)
				current_state = current_cell.get_state()
				if current_state == 0:
					if num_neighbors == 3:
						current_cell.set_state(1)
				else:
					if num_neighbors < 2:
						current_cell.set_state(0)
					elif num_neighbors > 3:
						current_cell.set_state(0)

	def run_multiple(self, iterations):
		for i in range(0, iterations):
			run_once()

	def get_neighbors(self, cell):
		neighbor_count = 0
		x = cell.get_x()
		y = cell.get_y()
		if x == 0:
			if y == 0:
				if self.cells[self.size-1][self.size-1].get_state(): neighbor_count += 1
				if self.cells[self.size-1][x].get_state(): neighbor_count += 1
				if self.cells[self.size-1][x+1].get_state(): neighbor_count += 1
				if self.cells[y][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y][x+1].get_state(): neighbor_count += 1
				if self.cells[y+1][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y+1][x].get_state(): neighbor_count += 1
				if self.cells[y+1][x+1],get_state(): neighbor_count += 1
			elif y == self.size - 1:
				if self.cells[y-1][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y-1][x].get_state(): neighbor_count += 1
				if self.cells[y-1][x+1].get_state(): neighbor_count += 1
				if self.cells[y][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y][x+1].get_state(): neighbor_count += 1
				if self.cells[0][self.size-1].get_state(): neighbor_count += 1
				if self.cells[0][x].get_state(): neighbor_count += 1
				if self.cells[0][x+1].get_state(): neighbor_count += 1
			else:
				if self.cells[y-1][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y-1][x].get_state(): neighbor_count += 1
				if self.cells[y-1][x+1].get_state(): neighbor_count += 1
				if self.cells[y][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y][x+1].get_state(): neighbor_count += 1
				if self.cells[y+1][self.size-1].get_state(): neighbor_count += 1
				if self.cells[y+1][x].get_state(): neighbor_count += 1
				if self.cells[y+1][x+1].get_state(): neighbor_count += 1
		elif x == self.size - 1:
			if y == 0:
				if self.cells[self.size-1][x-1].get_state(): neighbor_count += 1
				if self.cells[self.size-1][x].get_state(): neighbor_count += 1
				if self.cells[self.size-1][0].get_state(): neighbor_count += 1
				if self.cells[y][x-1].get_state(): neighbor_count += 1
				if self.cells[y][0].get_state(): neighbor_count += 1
				if self.cells[y+1][x-1].get_state(): neighbor_count += 1
				if self.cells[y+1][x].get_state(): neighbor_count += 1
				if self.cells[y+1][0].get_state(): neighbor_count += 1
			elif y == self.size - 1:
				if self.cells[y-1][x-1].get_state(): neighbor_count += 1
				if self.cells[y-1][x].get_state(): neighbor_count += 1
				if self.cells[y-1][0].get_state(): neighbor_count += 1
				if self.cells[y][x-1].get_state(): neighbor_count += 1
				if self.cells[y][0].get_state(): neighbor_count += 1
				if self.cells[0][x-1].get_state(): neighbor_count += 1
				if self.cells[0][x].get_state(): neighbor_count += 1
				if self.cells[0][0].get_state(): neighbor_count += 1
			else:
				if self.cells[y-1][x-1].get_state(): neighbor_count += 1
				if self.cells[y-1][x].get_state(): neighbor_count += 1
				if self.cells[y-1][0].get_state(): neighbor_count += 1
				if self.cells[y][x-1].get_state(): neighbor_count += 1
				if self.cells[y][0].get_state(): neighbor_count += 1
				if self.cells[y+1][x-1].get_state(): neighbor_count += 1
				if self.cells[y+1][x].get_state(): neighbor_count += 1
				if self.cells[y+1][0].get_state(): neighbor_count += 1
		else:
			if y == 0:
				if self.cells[self.size-1][x-1].get_state(): neighbor_count += 1
				if self.cells[self.size-1][x].get_state(): neighbor_count += 1
				if self.cells[self.size-1][x+1].get_state(): neighbor_count += 1
				if self.cells[y][x-1].get_state(): neighbor_count += 1
				if self.cells[y][x+1].get_state(): neighbor_count += 1
				if self.cells[y+1][x-1].get_state(): neighbor_count += 1
				if self.cells[y+1][x].get_state(): neighbor_count += 1
				if self.cells[y+1][x+1].get_state(): neighbor_count += 1
			elif y == self.size - 1:
				if self.cells[y-1][x-1].get_state(): neighbor_count += 1
				if self.cells[y-1][x].get_state(): neighbor_count += 1
				if self.cells[y-1][x+1].get_state(): neighbor_count += 1
				if self.cells[y][x-1].get_state(): neighbor_count += 1
				if self.cells[y][x+1].get_state(): neighbor_count += 1
				if self.cells[0][x-1].get_state(): neighbor_count += 1
				if self.cells[0][x].get_state(): neighbor_count += 1
				if self.cells[0][x+1].get_state(): neighbor_count += 1
			else:
				if self.cells[y-1][x-1].get_state(): neighbor_count += 1
				if self.cells[y-1][x].get_state(): neighbor_count += 1
				if self.cells[y-1][x+1].get_state(): neighbor_count += 1
				if self.cells[y][x-1].get_state(): neighbor_count += 1
				if self.cells[y][x+1].get_state(): neighbor_count += 1
				if self.cells[y+1][x-1].get_state(): neighbor_count += 1
				if self.cells[y+1][x].get_state(): neighbor_count += 1
				if self.cells[y+1][x+1].get_state(): neighbor_count += 1

		return neighbor_count


class Cell:

	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.state = state

	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y



# main
while 1:
	print('Menu:')
	print('\t1) Set pieces')
	print('\t2) Run once')
	print('\t3) Run multiple')
	print('\t4) Quit')
	user_in = input('Please select an option from the menu')

	if int(user_in) == 1:

	elif int(user_in) == 2:

	elif int(user_in) == 3:

	elif int(user_in) == 4:
		break