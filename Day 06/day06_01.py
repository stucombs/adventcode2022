# start-of-packet marker
# four characters that are all different

INPUT_FILE = './input.txt';
rf = open(INPUT_FILE,'r');
signal = rf.read();

# TEST INPUT
# signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'; # 7 jpqm
# signal = 'bvwbjplbgvbhsrlpgdmjqwftvncz'; # 5 vwbj
# signal = 'nppdvjthqldpwncqszvftbrmjlhg' # 6
# signal = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # 10
# signal = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # 11

parse_signal = list(signal);
prev_chars = []; # Track last character parsed
pos = 0;
starter = 0;

while pos < len(signal):
	if len(prev_chars) == 4:
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