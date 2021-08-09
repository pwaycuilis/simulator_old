#The issue unit follows the basic scoreboarding algorithm to issue instructions. It can issue up to two instructions, out of order, per clock cycle.
#When an instruction is issued, it moves out of the pre-issue buffer and into either the pre-mem buffer or the pre-ALU buffer. 
#The issue unit searches from entry 0 to entry 3 (in that order) of the pre-issue buffer.
class Issue:

    memIndexOfNext = 96
    currIndex = 0
    def __init__(self, preIssueBuff,preMemBuff, preALUBuff, instructions, opcode, opcodeStr,
                 dataval, address, arg1, arg2, arg3, numInstructs, destReg, src1Reg, src2Reg):
        self.instruction = instructions
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructions = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.opcodeStr = opcodeStr
        self.PC = 96
        self.cycle = 1

        self.preIssueBuff = preIssueBuff
        self.preMemBuff = preMemBuff
        self.preALUBuff = preALUBuff

    def run(self):

        numInIssueAtClockCycleBegin = 0
        ##do iso loop first to determine this, then while pre, post diff is < 2, keep going (while loop)
        for i in range(len(self.preIssueBuff)):
            if self.preIssueBuff[i] != -1:
                numInIssueAtClockCycleBegin += 1
                print(f"(issue34)numInIssue = {numInIssueAtClockCycleBegin}")


            ##if current index instr = "ADDI" (or some other valid instr)
            ## and if preALUBuff[0] is empty and preissuebuff[i] == currIndex:
            ##   move contents from preIssueBuff[i] to preALUBuff[0], clear preIssueBuff[i] and currAddr++
            ##elif preALUBuff[1] is empty and preIssueBuff[i] = currIndex:
            ##   move contents from preIssueBuff[i] to preALUBuff[1], clear preIssueBuff[i] and currAddr++

                if self.opcodeStr[self.preIssueBuff[i]] == "ADDI" or self.opcodeStr[self.preIssueBuff[i]] == "ADD"\
                        or self.opcodeStr[self.preIssueBuff[i]] == "SUB" or self.opcodeStr[self.preIssueBuff[i]] == "SUBI"\
                        or self.opcodeStr[self.preIssueBuff[i]] == "AND" or self.opcodeStr[self.preIssueBuff[i]] == "ORR"\
                        or self.opcodeStr[self.preIssueBuff[i]] == "EOR" or self.opcodeStr[self.preIssueBuff[i]] == "LSL":
                    if self.preALUBuff[0] == -1 and self.preIssueBuff[i] == self.currIndex:# and self.address[i] == self.memIndexOfNext:    #and if preALUBuff has open slot
                        self.preALUBuff[0] = self.preIssueBuff[i]
                        self.preIssueBuff[i] = -1           #set preissuebuff back to -1
                        self.currIndex += 1
                        ## self.memIndexOfNext += 4

                    elif self.preALUBuff[1] == -1 and self.preIssueBuff[i] == self.currIndex:# and self.address[i] == self.memIndexOfNext:
                        self.preALUBuff[1] = self.preIssueBuff[i]
                        self.preIssueBuff[i] = -1       #set preissuebuff back to -1
                        self.currIndex += 1
                        ## self.memIndexOfNext += 4

                ## for STUR/LDUR instructions
                if self.opcodeStr[self.preIssueBuff[i]] == "STUR":
                    if self.preMemBuff[0] == -1 and self.preIssueBuff[i] == self.currIndex:
                        self.preMemBuff[0] = self.preIssueBuff[i]
                        self.preIssueBuff[i] = -1
                        self.currIndex += 1

                    elif self.preMemBuff[1] == -1 and self.preIssueBuff[i] == self.currIndex:
                        self.preMemBuff[1] = self.preIssueBuff[i]
                        self.preIssueBuff[i] = -1
                        self.currIndex += 1
                ###***
                #if self.opcodedStr[self.preIssueBuff[i]]



        # return Issue(self.preIssueBuff, self.preMemBuff, self.preALUBuff, self.instruction, self.opcode, self.opcodeStr,
        #          self.dataval, self.address, self.arg1, self.arg2, self.arg3, self.numInstructions, self.destReg, self.src1Reg, self.src2Reg)


        return [self.preMemBuff, self.preALUBuff, self.preIssueBuff]

        # curr = self.preIssueBuff[0]


