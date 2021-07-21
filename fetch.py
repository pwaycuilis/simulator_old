
import cache


class Fetch:

    totalFetched = 0
    totalChecked = 0
    #rTypeInBuff = 0
    def __init__(self, preIssueBuff, instruction, opcodes, opcodeStr, dataval, address,
                 arg1, arg2, arg3, numInstrs, destReg, src1Reg, src2Reg):

        self.instruction = instruction
        self.opcodes = opcodes
        self.opcodeStr = opcodeStr
        self.dataval = dataval
        self.address = address
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.numInstrs = numInstrs
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg

        self.cache = cache.Cache(numInstrs, instruction, dataval, address)

        # print(self.opcodeStr)

        self.preIssueBuff = preIssueBuff

    def run(self):
        foundBreak = False

        fetchesPerCycle = 0

        #while foundBreak == False
        numInBuff = 0

        readyToCycle = False

        rTypeInBuff = 0


        #cache.checkCache(0, )


        for i in range(len(self.preIssueBuff)):
            if self.preIssueBuff[i] > -1:
                numInBuff += 1
                if self.opcodeStr[self.preIssueBuff[i]] == "ADD" or self.opcodeStr[self.preIssueBuff[i]] == "ADDI" or \
                        self.opcodeStr[self.preIssueBuff[i]] == "SUB" or self.opcodeStr[self.preIssueBuff[i]] == "SUBI" or \
                        self.opcodeStr[self.preIssueBuff[i]] == "AND" or self.opcodeStr[self.preIssueBuff[i]] == "ORR" or \
                        self.opcodeStr[self.preIssueBuff[i]] == "EOR":
                    rTypeInBuff += 1

        #print(numInBuff)



        # if curr > 0:
        #     for i in range(0, curr):
        #         if self.src1Reg[index] == self.destReg[self.preIssueBuff[i]] or\
        #         self.src2Reg[index] == self.destReg[self.preIssueBuff[i]]:
        #             issueMe = False
        #             break


        if fetchesPerCycle < 2 and numInBuff < 4 and rTypeInBuff < 2:
            for i in range(self.totalFetched, (len(self.instruction))):
                if self.opcodeStr[i] == "ADDI":
                    # print(f"i = {i}")
                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    # print(f"preissbuff within loop{self.preIssueBuff}")
                    rTypeInBuff += 1
                    break

                elif self.opcodeStr[i] == "ADD":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break
                elif self.opcodeStr[i] == "SUB":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "SUBI":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "AND":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "ORR":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "EOR":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

        if fetchesPerCycle < 2 and numInBuff < 4 and rTypeInBuff < 2:       #do loop again so max entries is 2 per program call
            for i in range(self.totalFetched, (len(self.instruction))):
                if self.opcodeStr[i] == "ADDI":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "ADD":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "SUB":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "SUBI":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "AND":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "ORR":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

                elif self.opcodeStr[i] == "EOR":

                    self.addToBuff(i)
                    fetchesPerCycle += 1
                    numInBuff += 1
                    self.totalFetched += 1
                    rTypeInBuff += 1

                    break

        #dataIndex = self.preIssueBuff[0] * 4 + 96

        #cCache = cache.checkCache
        # def checkCache(self, dataIndex, instructionIndex, isWriteToMem, dataToWrite):
        #cache.checkCache( dataIndex, self.preIssueBuff[0], 0,)

        # print(f"self.address{self.address}")

        # return [True, self.cacheSets[setNum][(self.lruBit[setNum] + 1) % 2][dataWord + 3]]

        # print(self.cache.cacheSets)
        LRU = False

        # [LRU, self.cache.cacheSets] =

        # print(f"totalChecked={self.totalChecked}")
        # print(f"numInstrs={self.numInstrs}")
        if self.totalChecked <= self.numInstrs - 1:
            self.cache.checkCache(-1, self.totalChecked, 0, 0)
            self.totalChecked += 1

        # else:
        #     self.

        # print(f"cachesets from fetch{self.cache.cacheSets}")

        # print("cachesets from fetch")

        # for record in self.cache.cacheSets:
        #     print(record)

        # for a in range (len(self.cache.cacheSets)):
        #     for b in range (len(self.cache.cacheSets[a])):
        #         print(self.cache.cacheSets[a][b], end = " ")
        #     print()

        # [LRU, self.cache.cacheSets] = self.cache.checkCache(-1, self.preIssueBuff[self.totalChecked], 0, 0)



        # print(LRU)

        #self.cache.checkCache(-1, 0, 0, 0)


        #print(f"dataIndex = {dataIndex}")





        # if fetchesPerCycle < 2 and numInBuff < 4:
        #     for i in range(self.totalFetched, len(self.instruction)):
        #         if self.opcodeStr[i] == "ADDI":
        #             self.preIssueBuff = self.addToBuff(i)
        #             fetchesPerCycle += 1
        #             numInBuff += 1
        #             self.totalFetched += 1
        #             break
        #
        #
        #
        # if fetchesPerCycle < 2 and numInBuff < 4:
        #     for i in range(self.totalFetched, len(self.instruction)):
        #         print(f"i = {i}")
        #         if self.opcodeStr[i] == "ADDI":
        #             self.preIssueBuff = self.addToBuff(i)
        #             fetchesPerCycle += 1
        #             numInBuff += 1
        #             self.totalFetched += 1
        #             break


        return self.preIssueBuff



        #(instruction, opcodes, opcodeStr, dataval, address, arg1, arg2, arg3,
         #                          numInstrs, destReg, src1Reg, src2Reg)

    def addToBuff(self, n):
        for i in range(len(self.preIssueBuff)):
            # print (f"for i in addtobuff i ={i}")
            if self.preIssueBuff[i] < 0:
                # print(self.preIssueBuff)
                # print(f"in addtobuff i = {i}")
                self.preIssueBuff[i] = n
                break

    # def printState(self):


        #return self.preIssueBuff
                #self.preIssueBuff[i] = n

