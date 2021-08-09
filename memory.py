from helpers import SetUp

#self.MEM = memory.Memory(self.R, self.postMemBuff, self.preMemBuff, opcodeStr, arg1, arg2,
        #                         arg3, dataval, address, self.numInstructions, self.cache, self.cycleList)

class Memory:

    def __init__(self, R, postMemBuff, preMemBuff, opcodeStr, arg1, arg2, arg3,
                 dataval, address, numInstructions, cache, cycleList):
        self.R = R
        self.postMemBuff = postMemBuff
        self.preMemBuff = preMemBuff
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.dataval = dataval
        self.address = address
        self.numInstructions = numInstructions
        self.cache = cache
        self.cycleList = cycleList

    def run(self):
        """
        mem unit handles LDUR and STUR operations. Calculate the memory addresses in this unit
        STUR instructions never goes into the post-mem buffer. it just disappears
        :return:
        """
        # def checkCache(self, dataIndex, instructionIndex, isWriteToMem, dataToWrite):
        i = self.preMemBuff[0]


        print(f"self.preMemBuff[0] = {self.preMemBuff[0]}")

        #from fetch
        #if self.cache.checkCache(-1, i, 0, 0):

        #some operation needed to check if there is any operations using needed register still in pipeline
        """
        if self.opcodeStr[i] == "STUR":
            if (self.R[self.arg2[i]] + self.arg3[i] * 4) > self.address[-1]:
                numAppend = ((self.R[self.arg2[i]] + self.arg3[i] * 4) - self.address[-1]) // 4

                for z in range(numAppend):
                    self.address.append(self.address[-1] + 4)
                    self.dataval.append(0)

                self.dataval[-1] = self.R[self.arg1[i]]

                while (len(self.dataval) % 8 != 0):
                    self.address.append(self.address[-1] + 4)
                    self.dataval.append(0)
        """

        print(f"(mem55)self.R[self.arg2[i] : {self.R[self.arg2[i]]}")
        print(f"(mem56)self.arg3[i]")


        if self.opcodeStr[i] == "STUR":
            #if self.cache.checkCache(i, i, 1, self.R[self.arg1[i]]):
            if (self.R[self.arg2[i]] + self.arg3[i] * 4) > self.address[-1]:
                print(f"(mem62)appending if condition = true")
                numAppend = ((self.R[self.arg2[i]] + self.arg3[i] * 4) - self.address[-1]) // 4

                for z in range(numAppend):
                    self.address.append(self.address[-1] + 4)
                    self.dataval.append(0)

                self.dataval[-1] = self.R[self.arg1[i]]

                while (len(self.dataval) % 8 != 0):
                    self.address.append(self.address[-1] + 4)
                    self.dataval.append(0)
                #added
                if self.cache.checkCache(i,i, 1, self.R[self.arg1[i]]):
                    self.preMemBuff[0] = self.preMemBuff[1]
                    self.preMemBuff[1] = -1

        #*********testing
        #print(f"(memory75)i = {i}")
        #if self.opcodeStr[i] == "STUR" and self.cache.checkCache(i, i, 1, self.R[self.arg1[i]]):
            #self.preMemBuff[0] = self.preMemBuff[1]
            #self.preMemBuff[1] = -1
        #*****testing

        return [self.preMemBuff, self.postMemBuff]






            #if self.cache.checkCache(i, i, 1, self.dataval[i]):
                #numAppend = ()

        #how STUR is calculated in simulator.py (for reference)
        """
        if (armState.R[self.arg2[i]] + (self.arg3[i]) * 4) > self.address[-1]:

            numAppend = ((armState.R[self.arg2[i]] + self.arg3[i] * 4) - self.address[-1]) // 4
            # print(armState.R[self.arg2[i]] + (self.arg3[i]*4))
            # print(self.address[-1])
            # print(numAppend)

            for z in range(numAppend):
                self.address.append(self.address[-1] + 4)
                self.dataval.append(0)

            self.dataval[-1] = armState.R[self.arg1[i]]

            while (len(self.dataval) % 8 != 0):
                self.address.append(self.address[-1] + 4)
                self.dataval.append(0)

        elif (armState.R[self.arg2[i]] + self.arg3[i] * 4) <= self.address[-1]:
            for n in range(len(self.address)):
                if armState.R[self.arg2[i]] + (self.arg3[i] * 4) == self.address[n]:
                    self.dataval[n - self.numInstructs] = armState.R[self.arg1[i]]
        """