INPUT_FILE = './input.txt';
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE,'r');

totals_array = [];
running_total = 0;

for cal in rf.read().splitlines():
	if cal != '':
		running_total += int(cal);
	else:
		totals_array.append(running_total);
		running_total = 0;

totals_array.sort(reverse=True);
print(f"ANSWER: {sum([totals_array[0],totals_array[1],totals_array[2]])}");
rf.close();