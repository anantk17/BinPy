from BinPy.Gates import *

class SRLatch:

	def __init__(self,input1,input2):
		
		self.a = Connector()
		self.b = Connector()

		self.g1 = NOR(input1,self.b)
		self.g1.setOutput(self.a)

		self.g2 = NOR(input2,self.a)
		self.g2.setOutput(self.b)

	def setInputs(self,input1,input2):

		if len(inputs) != 2:
			raise Exception("ERROR: Latch takes two inputs!")
			return None

		self.g1.setInput(0,input1)
		self.g2.setInput(0,input2)

	def output(self):

		return [self.g1.output(), self.g2.output()]

class DFlipFlop:

	def __init__(self,input1,input2):

		self.a = Connector()
		self.b = Connector()
		self.c = Connector()
		self.d = Connector()

		self.g1 = NAND(input1,input2)
		self.g1.setOutput(self.a)

		self.g2 = NAND(self.a,input2)
		self.g2.setOutput(self.b)

		self.g3 = NAND(self.a,self.d)
		self.g3.setOutput(self.c)

		self.g4 = NAND(self.b,self.c)
		self.g4.setOutput(self.d)

	def output(self):

		return [self.g3.output(),self.g4.output()]

	def setInputs(self,input1,input2):

		self.g1.setInput(0,input1)
		self.g1.setInput(1,input2)
		self.g2.setInput(1,input2)
		
class JKFlipFlop:
	
	def __init__(self,input1,input2,input3):	#input1 = J, input2 = K, input3 = enable/CLK
		
		self.a = Connector()
		self.b = Connector()
		self.c = Connector()
		self.d = Connector()
		
		self.g1 = NAND(self.d,input1,input3)
		self.g1.setOutput(self.a)
		
		self.g2 = NAND(input3,input2,self.b)
		self.g2.setOutput(self.c)
		
		self.g3 = NAND(self.a,self.d)
		self.g3.setOutput(self.b)
		
		self.g4 = NAND(self.c,self.b)
		self.g4.setOutput(self.d)
		
	def output(self):
		
		return [self.g3.output(),self.g4.output()]
		
	def setInputs(self,input1,input2,input3):
		
		self.g1.setInput(1,input1)
		self.g1.setInput(2,input3)
		self.g2.setInput(0,input3)
		self.g2.setInput(1,input2)
