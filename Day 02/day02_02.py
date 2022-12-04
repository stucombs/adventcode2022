INPUT_FILE = './input.txt';
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE,'r');

POINTS = {
	'ROCK':1,
	'PAPER':2,
	'SCISSORS':3,
	'L':0,
	'D':3,
	'W':6
};

HANDS = {
	'A':'ROCK',
	'B':'PAPER',
	'C':'SCISSORS',
	'X':'ROCK',
	'Y':'PAPER',
	'Z':'SCISSORS'
};

game_total = 0;
round_total = 0;

def convertHand(hand):
	"""
		Converts hand to symbol equivalent

		:param hand: str

		:return str
	"""

	return HANDS[hand];

def checkPlay(opp, outcome):
	# CASE DRAW
	if outcome == 'Y':
		return POINTS[opp] + POINTS['D'];

	# CASE LOSE	
	if outcome == 'X':
		# must lose
		player_points = POINTS['L'];
		if opp == 'ROCK':
			return POINTS['SCISSORS'] + player_points;
		if opp == 'SCISSORS':
			return POINTS['PAPER'] + player_points;
		if opp == 'PAPER':
			return POINTS['ROCK'] + player_points;

	# CASE WIN
	if outcome == 'Z':
		player_points = POINTS['W'];
		if opp == 'ROCK':
			return POINTS['PAPER'] + player_points;
		if opp == 'PAPER':
			return POINTS['SCISSORS'] + player_points;
		if opp == 'SCISSORS':
			return POINTS['ROCK'] + player_points;

for line in rf.read().splitlines():
	play = line.split(' ');
	round_total = checkPlay(convertHand(play[0]),play[1]);
	game_total += round_total;
	round_total = 0;

rf.close();
print(f"GAME TOTAL: {game_total}");