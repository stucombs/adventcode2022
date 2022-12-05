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

	counter = 0;
	while counter < moves:
		crate = starting_stack[from_stack].pop();
		starting_stack[to_stack].append(crate);
		# print(f"FROM STACK: {from_stack}");
		# print(f"TO STACK: {to_stack}");
		counter += 1;

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