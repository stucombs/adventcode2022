INPUT_FILE = './test.txt';
# INPUT_FILE = './input.txt';
rf = open(INPUT_FILE,'r');

tail_total_moves = 1;
dict_coordinates = {
	'H': [0,0],
	'T': [0,0]	
};

def splitCoordinate(coordinate):
	"""
		Split coordinate into direction and integer value

		:param coordinate: str

		:return str, int
	"""
	coordinate = coordinate.split(' ');
	return coordinate[0], int(coordinate[1]);

def moveHead(instruction):
	"""
		Increase/decrease "head" position based on coordinate

		:param instruction: str

		:return void
	"""
	direction, amount = splitCoordinate(instruction);
	if direction == 'R':
		dict_coordinates['H'][1] += amount;
	elif direction == 'L':
		dict_coordinates['H'][1] -= amount;
	elif direction == 'U':
		dict_coordinates['H'][0] += amount;
	elif direction == 'D':
		dict_coordinates['H'][0] -= amount;

def moveTail(instruction):
	print();

for line in rf.read().splitlines():
	moveHead(line);

rf.close();
print(f"FINAL COORDS: {dict_coordinates}");
