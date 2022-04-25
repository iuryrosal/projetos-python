class LogicGate:
    def __init__(self, gate_name):
        self.name = gate_name
        self.output = None 
    
    def getName(self):
        return self.name 
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None 
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            return self.putPinA()
        else:
            return self.pinA
    
    def getPinB(self):
        if self.pinB == None:
            return self.putPinB()
        else:
            return self.pinB
    
    def putPinA(self):
        return int(input("Digite a entrada do Pino A para a porta " + self.getName() + " : "))
    
    def putPinB(self):
        return int(input("Digite a entrada do Pino B para a porta " + self.getName() + " : "))

class UnaryGate(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None 
    
    def getPinA(self):
        if self.pinA == None:
            return self.putPinA()
        else:
            return self.pinA
    
    def putPinA(self):
        return int(input("Digite a entrada do Pino A para a porta " + self.getName() + " : "))

class ANDGate(BinaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class ORGate(BinaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NOTGate(UnaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
    
    def performGateLogic(self):
        a = self.getPinA()

        if a == 1:
            return 0
        else:
            return 1