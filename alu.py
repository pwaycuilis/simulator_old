import writeBack
import simClass
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

        #self.preALUBuff = [0, 1]

        #sim = simClass.simClass()
        i = self.preALUBuff[0]


        # armState.R[self.arg3[i]] = armState.R[self.arg1[i]] + armState.R[self.arg2[i]]

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


        elif self.opcodeStr[i] == "SUBI":
            self.postALUBuff = [self.R[self.arg2[i]] - self.arg3[i], i]

           # armState.R[self.arg1[i]] = armState.R[self.arg2[i]] - self.arg3[i]

        elif self.opcodeStr[i] == "AND":
            self.postALUBuff = [self.R[self.arg1[i]] & self.R[self.arg2[i]], i]

        elif self.opcodeStr[i] == "ORR":
            self.postALUBuff = [self.R[self.arg1[i]] | self.R[self.arg2[i]], i]

        elif self.opcodeStr[i] == "EOR":
            self.postALUBuff = [self.R[self.arg1[i]] ^ self.R[self.arg2[i]], i]


            # elif self.opcode[i] == 1360:
            #     armState.R[self.arg3[i]] = armState.R[self.arg1[i]] | armState.R[self.arg2[i]]

            # EOR
            # elif self.opcode[i] == 1872:
            #     armState.R[self.arg3[i]] = armState.R[self.arg1[i]] ^ armState.R[self.arg2[i]]



        #rmState.R[self.arg3[i]] = armState.R[self.arg1[i]] & armState.R[self.arg2[i]]


        self.preALUBuff[0] = self.preALUBuff[1]
        self.preALUBuff[1] = -1



            #armState.R[self.arg1[i]] = armState.R[self.arg2[i]] + self.arg3[i]


        # return ALU(self.R, self.postALUBuff, self.preALUBuff,self.opcodeStr,
        #             self.arg1, self.arg2, self.arg3)

        return [self.preALUBuff, self.postALUBuff]

        # (self, R, postALUBuff, preALUBuff, opcodeStr, arg1, arg2, arg3):

        # return ALU(self.R, self.postALUBuff, self.preALUBuff, self.opcodeStr, self.arg1,
        #            self.arg2, self.arg3)




    # def updateBuffer(self):
    #     return [self.preALUBuff, self.postALUBuff]