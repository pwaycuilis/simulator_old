
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

        # print(f"preIssueBuff in issue{self.preIssueBuff}")
        for i in range(len(self.preIssueBuff)):
            if self.preIssueBuff[i] != -1:          #if preIssueBuff has valid instr
                numInIssueAtClockCycleBegin += 1

                # print (f"numInIssue unit{numInIssueAtClockCycleBegin}")

                if self.opcodeStr[self.preIssueBuff[i]] == "ADDI" or self.opcodeStr[self.preIssueBuff[i]] == "ADD"\
                        or self.opcodeStr[self.preIssueBuff[i]] == "SUB" or self.opcodeStr[self.preIssueBuff[i]] == "SUBI"\
                        or self.opcodeStr[self.preIssueBuff[i]] == "AND" or self.opcodeStr[self.preIssueBuff[i]] == "ORR"\
                        or self.opcodeStr[self.preIssueBuff[i]] == "EOR":
                    if self.preALUBuff[0] == -1 and self.preIssueBuff[i] == self.currIndex:# and self.address[i] == self.memIndexOfNext:            #and if preALUBuff has open slot
                        self.preALUBuff[0] = self.preIssueBuff[i]
                        self.preIssueBuff[i] = -1           #set preissuebuff back to -1
                        self.currIndex += 1
                        # self.memIndexOfNext += 4

                    elif self.preALUBuff[1] == -1 and self.preIssueBuff[i] == self.currIndex:# and self.address[i] == self.memIndexOfNext:
                        self.preALUBuff[1] = self.preIssueBuff[i]
                        self.preIssueBuff[i] = -1       #set preissuebuff back to -1
                        self.currIndex += 1
                        # self.memIndexOfNext += 4


        #print(f"num at end{numInIssueAtClockCycleBegin}")

        # print(f"pre")

        # return Issue(self.preIssueBuff, self.preMemBuff, self.preALUBuff, self.instruction, self.opcode, self.opcodeStr,
        #          self.dataval, self.address, self.arg1, self.arg2, self.arg3, self.numInstructions, self.destReg, self.src1Reg, self.src2Reg)


        return [self.preMemBuff, self.preALUBuff, self.preIssueBuff]

        # curr = self.preIssueBuff[0]


