# start-of-packet marker
# four characters that are all different

INPUT_FILE = './input.txt';
rf = open(INPUT_FILE,'r');
# signal = rf.read();

# TEST
signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'; # 7
signal = 'bvwbjplbgvbhsrlpgdmjqwftvncz'; # 5
# signal = 'nppdvjthqldpwncqszvftbrmjlhg' # 6
# signal = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # 10
# signal = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # 11

parse_signal = list(signal);
prev_chars = []; # Track last character parsed
answer = 0;

for pos,char in enumerate(parse_signal):
	print(f"CHAR: {char}");
	print(f"PREV: {prev_chars}");
	if len(prev_chars) == 4:
		answer = pos;
		break;
	elif char in prev_chars:
		prev_chars = [char];
		# prev_chars = prev_chars[prev_chars.index(char):]
		# prev_chars.pop(0);
	else:
		prev_chars.append(char);

rf.close();
print(f"ANSWER: {answer}");