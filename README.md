# simulator
full version simulator that tracks cycle-by-cycle process (instruction-by-instruction version available in disassembler repository)


cycle-by-cycle ARM instruction simulator 

loads and executes binary ARM file. Produces disassembled program code and produces cycle-by-cycle simulation showing the processor state at each cycle. The processor state includes the contents of registers, buffers, cache, and data memory at each cycle.

program supports command line arguments for execution: Following argument supported:

  $python team23_project3.py -i branchtest_bin.txt -o team23_out\
  NOTE: can change input or output file name using -i or -o argument respectively
 


Below are examples of disassembler input and simple disassembled list of commands.
(showing the contents of the text input file branchtest_bin.txt as well as the 2 produced output files team23_out_dis.txt and team23_out_pipeline.txt)


branchtest_bin.txt (input ARM machine code):

10010001000000000001000001000001\
10001011000000100000000000100011\
11001011000000100000000000100011\
10001010000000100000000000100011\
10101010000000100000000000100011\
10010001000000000001000001000100\
11010011011000000000010010000010\
10001011000000100000000000100001\
10010001000000110010000000000100\
11111000000000000001000010000010\
11111110110111101111111111100111\


team23_out_dis.txt (disassembled program code):\
1001000100 000000000100 00010 00001	96	ADDI	R1, R2, #4\
10001011000 00010 000000 00001 00011	100	ADD	R3, R1, R2\
11001011000 00010 000000 00001 00011	104	SUB	R3, R1, R2\
10001010000 00010 000000 00001 00011	108	AND	R3, R1, R2\
10101010000 00010 000000 00001 00011	112	ORR	R3, R1, R2\
1001000100 000000000100 00010 00100	116	ADDI	R4, R2, #4\
11010011011 00000 000001 00100 00010	120	LSL	R2, R4, #1\
10001011000 00010 000000 00001 00001	124	ADD	R1, R1, R2\
1001000100 000011001000 00000 00100	128	ADDI	R4, R0, #200\
11111000000 000000001 00 00100 00010	132	STUR	R2, [R4, #1]\
11111110 110 11110 11111 11111 100111	136	BREAK\


#Full cycle-by-cycle simulation output text contained in \
**team_23_out_pipeline.txt**\
(running into formatting issues trying to post here)
