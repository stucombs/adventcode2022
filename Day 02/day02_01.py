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

def checkPlay(opp, player):
	"""
		Returns the round total

		:param opp: str
		:param player: str

		:return str
	"""

	player_points = POINTS[player];
	# case DRAW
	if opp == player:
		return POINTS['D'] + player_points;

	# case opp ROCK
	if opp == 'ROCK':
		if player == 'SCISSORS':
			return POINTS['L'] + player_points;

	# case opp PAPER
	if opp == 'PAPER':
		if player == 'ROCK':
			return POINTS['L'] + player_points;

	# case opp SCISSORS
	if opp == 'SCISSORS':
		if player == 'PAPER':
			return POINTS['L'] + player_points;

	return POINTS['W'] + player_points;

for line in rf.read().splitlines():
	play = line.split(' ');
	round_total = checkPlay(convertHand(play[0]),convertHand(play[1]));
	# print(f"HAND TOTAL: {round_total}");
	game_total += round_total;
	round_total = 0;

rf.close();
print(f"GAME TOTAL: {game_total}");