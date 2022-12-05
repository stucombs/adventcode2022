from stacks import starting_stack;
INPUT_FILE = './input.txt';
# from stacks import test_stack as starting_stack;
# INPUT_FILE = './test.txt';
rf = open(INPUT_FILE,'r');

def getTopCrate(stack):
	return stack[-1];

def parseInstruction(instruction):
	numbered_instructions = [];
	instruction = instruction.split(' ');
	for part in instruction:
		if not part.isalpha():
			numbered_instructions.append(part);

	return numbered_instructions;

def moveCrate(instruction,stack):
	numbered_instructions = parseInstruction(instruction);
	from_stack 	= int(numbered_instructions[1]);
	to_stack 	= int(numbered_instructions[2]);
	moves 		= int(numbered_instructions[0]);
	# MOVES IN THIS CASE ARE THE NUMBER OF CRATES TO MOVE AT ONCE, INSTEAD OF INDIVIDUALLY

	crates = starting_stack[from_stack][-moves:];
	for c in crates: 
		starting_stack[to_stack].append(c);
	del starting_stack[from_stack][-moves:];

	return stack;

# MAIN SCRIPT
for ins in rf.read().splitlines():
	starting_stack = moveCrate(ins,starting_stack);

# GET ANSWER FROM FINAL MUTATED STACK
final_answer = '';
for stack in starting_stack:
	final_answer += getTopCrate(starting_stack[stack]);

rf.close();
print(f"ANSWER: {final_answer}");