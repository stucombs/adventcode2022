# INPUT_FILE = './test.txt';
INPUT_FILE = './input.txt';
rf = open(INPUT_FILE, 'r');

dict_structure = {};
dict_content = {};

def isCommand(line):
	if '$' in line:
		return True;
	return False;

def getCommand(line):
	if isCommand(line):
		line = line.split(' ');
		return line[1];
	return False;

def getDirName(diry):
	return diry.split(' ')[1];

def changeDirectory(command):
	command = command.split(' ');
	return command[2];

def getFileSize(line):
	line = line.split(' ');
	return int(line[0]);

def getParent(direc):
	for key,value in dict_structure.items():
		if direc in value:
			return key;
	return '';

def isChild(parent,child):
	if child in dict_structure[parent]:
		return True;
	return False;

# FIRST LOOP TO DETERMINE DIRECTORY STRUCTURE
current_dir = '';
for line in rf.read().splitlines():
	if isCommand(line):
		command = getCommand(line);
		if command == 'ls':
			continue
		elif command == 'cd':
			new_directory = changeDirectory(line);
			if new_directory == '..':
				current_dir = getParent(current_dir);
			else:
				if new_directory not in dict_structure.keys():
					dict_structure[new_directory] = [];
				current_dir = new_directory;
	elif not isCommand(line):
		dict_structure[current_dir].append(line);
rf.close();

# NOW LOOP THROUGH STRUCTURE WE CREATED TO FIND TOTAL FILE SIZES IN EACH INDIVIDUAL DIRECTORY
def getDirSize(diry):
	total_size = 0;
	for item in dict_structure[diry]:
		if 'dir' not in item:
			total_size += getFileSize(item);
		else:
			item = item.split(' ')[1];
			total_size += getDirSize(item);
	return total_size;

# NOW LOOP THROUGH AND FIND SIZE OF EACH DIR INCLUDING SUB DIRS, FILTER FOR THOSE <= 100000
include_totals = [];
# for i in dict_structure:
# 	dict_content[i] = 0;
# 	dict_content[i] += getDirSize(i);

# 	if dict_content[i] <= 100000:
# 		include_totals.append(dict_content[i]);
print(getDirSize('jtbh'));

# print(sum(include_totals));
# NOT 864783