

#The ALU handles all non-memory instructions (everything except LDUR and STUR and branch instructions that are handled in the IF stage). 
#All ALU operations take one clock cycle.
#When the ALU finishes, the instruction is moved from the pre-ALU buffer to the post-ALU buffe. The ALU can only fetch one istruction from the pre-ALU buffer per clock cycle.

class ALU:

    def __init__(self, R, postALUBuff, preALUBuff, opcodeStr, arg1, arg2, arg3):
        self.R = R

        self.postALUBuff = postALUBuff
        self.preALUBuff = preALUBuff
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3





    def run(self):

        i = self.preALUBuff[0]


        # armState.R[self.arg3[i]] = armState.R[self.arg1[i]] + armState.R[self.arg2[i]]


        ##############
        #self.preALUBuff[0] and self.postALUBuff[1] both incrementing by 1 each cycle
        self.postALUBuff = [-1, -1]

        if self.opcodeStr[i] == "ADD":
            self.postALUBuff = [self.R[self.arg1[i]] + self.R[self.arg2[i]], i]

            #ADD R3, R1, R2
            #   arg3 arg1 arg2

            #postALUBuff = [[self.R[1] + self.R[2], i]
            #            = [[R1 + R2], i]


        elif self.opcodeStr[i] == "ADDI":
            self.postALUBuff = [self.R[self.arg2[i]] + self.arg3[i], i]


        elif self.opcodeStr[i] == "SUB":
            self.postALUBuff = [self.R[self.arg1[i]] - self.R[self.arg2[i]], i]

            # SUBI
            #elif (1672 <= self.opcode[i] <= 1673):
            #armState.R[self.arg1[i]] = armState.R[self.arg2[i]] - self.arg3[i]

        elif self.opcodeStr[i] == "SUBI":
            self.postALUBuff = [self.R[self.arg2[i]] - self.arg3[i], i]

           # armState.R[self.arg1[i]] = armState.R[self.arg2[i]] - self.arg3[i]

        elif self.opcodeStr[i] == "AND":
            self.postALUBuff = [self.R[self.arg1[i]] & self.R[self.arg2[i]], i]

        elif self.opcodeStr[i] == "ORR":
            self.postALUBuff = [self.R[self.arg1[i]] | self.R[self.arg2[i]], i]

        elif self.opcodeStr[i] == "EOR":
            self.postALUBuff = [self.R[self.arg1[i]] ^ self.R[self.arg2[i]], i]

        elif self.opcodeStr[i] == "LSL":
            self.postALUBuff = [self.R[self.arg2[i]] << self.arg1[i], i]



        #move instruction in entry 1 to entry 0 and then clear entry 1
        #just do if not stalled
        self.preALUBuff[0] = self.preALUBuff[1]
        self.preALUBuff[1] = -1



          
        return [self.preALUBuff, self.postALUBuff]

