
import simClass
#The WB unit can execute two write-backs in one cyucle. It fetches the contents of the post-ALU and post-MEM buffers and updates the register file.

class WriteBack:

    def __init__(self, R, postMemBuff,postALUBuff, destReg):
        self.R = R

        self.postMemBuff = postMemBuff
        self.postALUBuff = postALUBuff
        self.destReg = destReg


    def run(self):

 
        if self.postMemBuff != [-1, -1]:
            self.R[self.destReg[self.postMemBuff[1]]] = self.postMemBuff[0]  #self.R[self.destReg[
            self.postMemBuff = [-1, -1]

        #if postALUBuff not empty, write value to register and then clear buff

        if self.postALUBuff != [-1, -1]:
            self.R[self.destReg[self.postALUBuff[1]]] = self.postALUBuff[0]
            self.postALUBuff = [-1, -1]


        #**********************************^^^^^^
        return [self.R, self.postMemBuff, self.postALUBuff, self.destReg]
        #return [self.R, self.postMemBuff, self.postALUBuff]

    # def updateBuffer(self):
    #     return [self.R, self.postMemBuff, self.postALUBuff]
        #print(f"in writeback self.R: {self.R}")
        #return self.R
        # print(postMemBuff)
        # print(postALUBuff)

