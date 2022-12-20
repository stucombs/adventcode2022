INPUT_FILE = './input.txt';
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE,'r');

def compareSection(section1, section2):
	"""
		Returns True if section1 fully encompases section2
		:param section1: str
		:param section2: str

		:return boolean
	"""
	if int(section1[0]) <= int(section2[0]) and int(section1[1]) >= int(section2[1]):
		return True;

	return False;

def splitSection(section1,section2):
	"""
		Split two "section"s by hypen and return the 
		:param section1: str
		:param section2: str

		:return str, str
	"""
	section1 = section1.split('-');
	section2 = section2.split('-');
	return section1, section2;

# MAIN SCRIPT
total_overlap = 0;

for line in rf.read().splitlines():
	line = line.split(',');
	section1,section2 = line[0],line[1];
	listSection1, listSection2 = splitSection(section1,section2);

	# Need to compare section 1 to section 2 and vice versa
	if compareSection(listSection1,listSection2):
		total_overlap += 1;
	elif compareSection(listSection2,listSection1):
		total_overlap += 1;

rf.close();
print(f"ANSWER: {total_overlap}");
