INPUT_FILE = './input.txt';
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE,'r');

# Create dictionary for alpha character and point value
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
ALPHA_POINTS = {};
for pos,char in enumerate(alpha):
	ALPHA_POINTS[char] = pos + 1;

# Now process data
ruck_total = 0;

def findCommon(left, right):
	"""
		Returns the common character in two lists as a single character string
	"""
	left = set(left);
	right = set(right);
	return ''.join(left & right);

def pointConversion(char):
	"""
		Returns the point value of an alpha character a-z A-Z
	"""
	return ALPHA_POINTS[char];


# MAIN SCRIPT
for line in rf.read().splitlines():
	index_split = int(len(line) / 2);
	left, right = line[:index_split], line[index_split:];
	commonChar = findCommon(left, right);
	ruck_total += pointConversion(commonChar);

rf.close();
print(f"ANSWER: {ruck_total}");