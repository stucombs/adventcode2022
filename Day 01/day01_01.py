INPUT_FILE = './input.txt';
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE);

max_total = 0;
running_total = 0;
for cal in rf.read().splitlines():
	if cal != '':
		running_total += int(cal);
	else:
		if running_total > max_total:
			max_total = running_total;
		running_total = 0;
rf.close();

print(f'MAX: {max_total}');