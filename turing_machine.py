#############################################
# Simple Turing Machine
# Author: 	Samuel Jackson (slj11@aber.ac.uk)
# Date:		11/2/13
#############################################

from argparse import ArgumentParser
import re

pointer = 0		#instruction pointer
tape = None		#tape of symbols
program = []	#the program to run (states)

#read in the tape of symbols
def read_tape(filename):
	global tape
	with open(filename) as f:
		tape = list(f.read())

#read in the program file
def read_prog(filename):
	global program

	comment, whitespace= re.compile(r"//.*?\n"), re.compile(r'(\s+|^$)')

	for i, line in enumerate(open(filename).readlines()):
		line = re.sub(comment, '', line).strip().split(',')
		if not re.match(whitespace, ''.join(line)):
			if not re.match(re.compile(r"^(\d(R|L)..\d|\dH)$"), ''.join(line)):
				print "Bad Program at line %d" % (i+1)
				exit(-1)
			else:
				program.append(line)

#set the direction we are looking
def set_direction(d):
	return 1 if d == 'R' else -1

#Output the current state of the tape and pointer
def output_tape():
	global tape, pointer
	print "%s" % ''.join(tape)
	print ''.join(' ' * pointer) + '^'

def read_instruction(instructions):
	global pointer
	for i in instructions:
		state, direct, symbol, new_symbol, new_state = i
		direct = set_direction(direct)

		#add more tape as required
		if pointer+direct >= len(tape)-1:
			tape.append('#')
		elif pointer+direct < 0:
			tape.insert(0,'#')
			pointer += 1

		#next symbol in direction we're looking
		if tape[pointer+direct] == symbol:
			pointer += direct
			tape[pointer] = new_symbol

			return int(new_state) #return the next state

	pointer+=direct
	return -1

if __name__ == "__main__":
	#Get filenames from command line options
	parser = ArgumentParser(description="Simple Turing Machine Simulator")
	parser.add_argument('-i', '--input', type=str, nargs=1, required=True, help='Tape input file.')
	parser.add_argument('-p', '--program', type=str, nargs=1, required=True, help='Program file.')
	args = parser.parse_args()

	#Read in tape and program
	read_tape(args.input[0])
	read_prog(args.program[0])

	#Output un-processed tape
	print "\nSTART STATE:"
	output_tape()
	print "---------------------------------------"

	#Read first instruction for program
	current = [program[0]]

	while current[0][1] != 'H':
		#keep moving while we haven't found the next symbol
		new_state = -1
		while new_state == -1:
			new_state = read_instruction(current) #process instruction

		#find next state
		current = [instruction for instruction in program if int(instruction[0]) == new_state]

		#output state of tape and pointer
		output_tape()

	print "---------------------------------------"
	print "END STATE:"
	output_tape()