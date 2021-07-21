# simulator
full version simulator that tracks cycle-by-cycle process (instruction-by-instruction version available in disassembler repository)

cycle-by-cycle ARM instruction simulator 

loads and executes binary ARM file. Produces disassembled program code and produces cycle-by-cycle simulation showing the processor state at each cycle. The processor state includes the contents of registers, buffers, cache, and data memory at each cycle.

program supports command line arguments for exectuion: Following argument supported:

  $python team23_project3.py -i branchtest_bin.txt -o team23_out
  NOTE: can change output file name using -o argument
          assuming branchtest_bin.txt is the input file at the moment.


**currently known issues

-only handles R-type instructions

-does not handle hazards

-cycles data quicker than sample output

-cache data output is currently 1 cycle behind other output

-issues with MEM unit, not currently fuctional.
