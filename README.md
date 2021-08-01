# simulator
full version simulator that tracks cycle-by-cycle process (instruction-by-instruction version available in disassembler repository)


cycle-by-cycle ARM instruction simulator 

loads and executes binary ARM file. Produces disassembled program code and produces cycle-by-cycle simulation showing the processor state at each cycle. The processor state includes the contents of registers, buffers, cache, and data memory at each cycle.

program supports command line arguments for exectuion: Following argument supported:

  $python team23_project3.py -i branchtest_bin.txt -o team23_out\
  NOTE: can change input or output file name using -i or -o argument respectively
 


# Below is a sample run of the program 
(showing the contents of the text input file branchtest_bin.txt as well as the 2 produced output files team23_out_dis.txt and team23_out_pipeline.txt)
  

branchtest_bin.txt (input ARM machine code):

10010001000000000001000000100001\
10010001000000000001010001000010\
10001011000001000000000010100011\
11001011000001110000000110000100\
10001010000000100000000000100101\
10101010000000100000000001000110\
11101010000000100000000000100111\
11111110110111101111111111100111

team23_out_dis.txt (disassembled program code):
1001000100 000000000100 00001 00001	96	ADDI	R1, R1, #4\
1001000100 000000000101 00010 00010	100	ADDI	R2, R2, #5\
10001011000 00100 000000 00101 00011	104	ADD	R3, R5, R4\
11001011000 00111 000000 01100 00100	108	SUB	R4, R12, R7\
10001010000 00010 000000 00001 00101	112	AND	R5, R1, R2\
10101010000 00010 000000 00010 00110	116	ORR	R6, R2, R2\
11101010000 00010 000000 00001 00111	120	EOR	R7, R1, R2\
11111110 110 11110 11111 11111 100111	124	BREAK


team23_out_pipeline.txt(cycle-by-cycle simulation showing the processor state at each cycle) :

---------------------
cycle:1	

Pre-Issue Buffer:\
	Entry 0:	ADDI	R1, R1, #4\
	Entry 1:	ADDI	R2, R2, #5\
	Entry 2:\
	Entry 3:\
Pre_ALU Queue:\
	Entry 0:\
	Entry 1:\
Post_ALU Queue:\
	Entry 0:\
Pre_MEM Queue:\
	Entry 0:\
	Entry 1:\
Post_MEM Queue:\
	Entry 0:\
registers:\
r00:	0	0	0	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\

Cache

Set 0: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:

---------------------
cycle:2

Pre-Issue Buffer:\
	Entry 0:	ADD	R3, R5, R4\
	Entry 1:	SUB	R4, R12, R7\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	ADDI	R1, R1, #4\
	Entry 1:	ADDI	R2, R2, #5\
Post_ALU Queue:\
	Entry 0:	\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	0	0	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\

Cache

Set 0: LRU = 1	\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:
---------------------
cycle:3	

Pre-Issue Buffer:\
	Entry 0:	AND	R5, R1, R2\
	Entry 1:	SUB	R4, R12, R7\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	ADDI	R2, R2, #5\
	Entry 1:	ADD	R3, R5, R4\
Post_ALU Queue:\
	Entry 0:	ADDI	R1, R1, #4\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	0	0	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:\
---------------------
cycle:4	\
Pre-Issue Buffer:\
	Entry 0:	AND	R5, R1, R2\
	Entry 1:	ORR	R6, R2, R2\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	ADD	R3, R5, R4\
	Entry 1:	SUB	R4, R12, R7\
Post_ALU Queue:\
	Entry 0:	ADDI	R2, R2, #5\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	0	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:\
---------------------
cycle:5	\
Pre-Issue Buffer:\
	Entry 0:	EOR	R7, R1, R2\
	Entry 1:	ORR	R6, R2, R2\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	SUB	R4, R12, R7\
	Entry 1:	AND	R5, R1, R2\
Post_ALU Queue:\
	Entry 0:	ADD	R3, R5, R4\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	5	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:\
---------------------
cycle:6	\
Pre-Issue Buffer:\
	Entry 0:	EOR	R7, R1, R2\
	Entry 1:	\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	AND	R5, R1, R2\
	Entry 1:	ORR	R6, R2, R2\
Post_ALU Queue:\
	Entry 0:	SUB	R4, R12, R7\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	5	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 1\
	Entry 0:[1, 0, 3, '10001010000000100000000000100101', '10101010000000100000000001000110']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:\
---------------------
cycle:7	\
Pre-Issue Buffer:\
	Entry 0:	\
	Entry 1:	\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	ORR	R6, R2, R2\
	Entry 1:	EOR	R7, R1, R2\
Post_ALU Queue:\
	Entry 0:	AND	R5, R1, R2\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	5	0	0	0	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 1\
	Entry 0:[1, 0, 3, '10001010000000100000000000100101', '10101010000000100000000001000110']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 0\
	Entry 0:[0, 0, 0, 0, 0]\
	Entry 1:[0, 0, 0, 0, 0]\
data:
---------------------

cycle:8	\

Pre-Issue Buffer:\
	Entry 0:	\
	Entry 1:	\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	EOR	R7, R1, R2\
	Entry 1:	\
Post_ALU Queue:\
	Entry 0:	ORR	R6, R2, R2\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	5	0	0	4	0	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 1\
	Entry 0:[1, 0, 3, '10001010000000100000000000100101', '10101010000000100000000001000110']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 1\
	Entry 0:[1, 0, 3, '11101010000000100000000000100111', '11111110110111101111111111100111']\
	Entry 1:[0, 0, 0, 0, 0]\
data:\
---------------------\

cycle:9	

Pre-Issue Buffer:\
	Entry 0:	\
	Entry 1:	\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	\
	Entry 1:	\
Post_ALU Queue:\
	Entry 0:	EOR	R7, R1, R2\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	5	0	0	4	5	0\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 1\
	Entry 0:[1, 0, 3, '10001010000000100000000000100101', '10101010000000100000000001000110']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 1\
	Entry 0:[1, 0, 3, '11101010000000100000000000100111', '11111110110111101111111111100111']\
	Entry 1:[0, 0, 0, 0, 0]\
data:\
---------------------

cycle:10	

Pre-Issue Buffer:\
	Entry 0:	\
	Entry 1:	\
	Entry 2:	\
	Entry 3:	\
Pre_ALU Queue:\
	Entry 0:	\
	Entry 1:	\
Post_ALU Queue:\
	Entry 0:	\
Pre_MEM Queue:\
	Entry 0:	\
	Entry 1:	\
Post_MEM Queue:\
	Entry 0:	\
registers:\
r00:	0	4	5	0	0	4	5	1\
r08: 	0	0	0	0	0	0	0	0\
r16: 	0	0	0	0	0	0	0	0\
r24: 	0	0	0	0	0	0	0	0\
Cache\
Set 0: LRU = 1\
	Entry 0:[1, 0, 3, '10010001000000000001000000100001', '10010001000000000001010001000010']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 1: LRU = 1\
	Entry 0:[1, 0, 3, '10001011000001000000000010100011', '11001011000001110000000110000100']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 2: LRU = 1\
	Entry 0:[1, 0, 3, '10001010000000100000000000100101', '10101010000000100000000001000110']\
	Entry 1:[0, 0, 0, 0, 0]\
Set 3: LRU = 1\
	Entry 0:[1, 0, 3, '11101010000000100000000000100111', '11111110110111101111111111100111']\
	Entry 1:[0, 0, 0, 0, 0]\
data:
