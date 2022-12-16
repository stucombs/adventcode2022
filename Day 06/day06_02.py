# MESSAGES
# == 14 distinct characters

INPUT_FILE = './input.txt';
rf = open(INPUT_FILE,'r');
signal = rf.read();

# TEST INPUT
# signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'; # 19
# signal = 'bvwbjplbgvbhsrlpgdmjqwftvncz'; # 23
# signal = 'nppdvjthqldpwncqszvftbrmjlhg' # 23
# signal = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # 29
# signal = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # 26

parse_signal = list(signal);
prev_chars = []; # Track last character parsed
pos = 0;
starter = 0;

while pos < len(signal):
	if len(prev_chars) == 14:
		break;
	elif signal[pos] in prev_chars:
		prev_chars = [signal[starter]];
		starter += 1;
		pos = starter;
	else:
		prev_chars.append(signal[pos]);
		pos+=1;

rf.close();
print(f"ANSWER: {pos}");