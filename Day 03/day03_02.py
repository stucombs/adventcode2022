INPUT_FILE = './input.txt';
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE,'r');

# Create dictionary for alpha character and point value
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
ALPHA_POINTS = {};
for pos,char in enumerate(alpha):
	ALPHA_POINTS[char] = pos + 1;

# Now process data
badge_total = 0;

def findCommon(group_one, group_two, group_three):
	"""
		Returns the common character in three lists as a single character string
	"""
	group_one = set(group_one);
	group_two = set(group_two);
	group_three = set(group_three);

	group_one = group_one.intersection(group_two);
	result = group_one.intersection(group_three);

	return ''.join(result);

def pointConversion(char):
	"""
		Returns the point value of an alpha character a-z A-Z
	"""
	return ALPHA_POINTS[char];

# MAIN SCRIPT
counter = 0;
groups = rf.read().splitlines();
curr_group = [];

for pos,group in enumerate(groups):
	if(counter < 2):
		curr_group.append(group);
		counter = counter + 1;
	else:
		curr_group.append(group);
		common = findCommon(curr_group[0], curr_group[1], curr_group[2]);
		badge_total += pointConversion(common);
		curr_group = [];	
		counter = 0;

print(f"ANSWER: {badge_total}");
rf.close();
