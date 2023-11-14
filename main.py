# ('ADD', 'Ra', 'Rb', 'Rc')
# ('SUB', 'Ra', 'Rb', 'Rc')
# ('MUL', 'Ra', 'Rb', 'Rc')
# ('DIV', 'Ra', 'Rb', 'Rc')
# ('INC', 'Ra')
# ('DEC', 'Ra')
# ('CMP', 'op', 'Ra', 'Rb', 'Rc') op = {<, >, <=, >=, ==, !=}
# ('CONST', 'Ra', value)
# ('LOAD', 'Rs', 'Rd', offset) RAM
# ('STORE', 'Rs', 'Rd', offset) RAM
# ('JMP', 'label')
# ('HALT')

class CPU:

    def run(self, instructions):
        self.registers = {'Ra': 0, 'Rb': 0, 'Rc': 0, 'Rd': 0, 'Re': 0, 'Rf': 0, 'Rg': 0, 'Rh': 0}  # 8 registers
        self.memory = [0] * 1024
        self.registers['IP'] = 0
        self.registers['SP'] = 0

        # read the instructions until the end and print results

        while True:

            instruction = instructions[self.registers['IP']]
            self.registers['IP'] += 1

            command = instruction[0]

            if command == 'ADD':
                self.ADD(instruction[1], instruction[2], instruction[3])
            elif command == 'SUB':
                self.SUB(instruction[1], instruction[2], instruction[3])
            elif command == 'MUL':
                self.MUL(instruction[1], instruction[2], instruction[3])
            elif command == 'DIV':
                self.DIV(instruction[1], instruction[2], instruction[3])
            elif command == 'INC':
                self.INC(instruction[1])
            elif command == 'DEC':
                self.DEC(instruction[1])
            elif command == 'CMP':
                self.CMP(instruction[1], instruction[2], instruction[3], instruction[4])
            elif command == 'CONST':
                self.CONST(instruction[1], instruction[2])
            elif command == 'LOAD':
                self.LOAD(instruction[1], instruction[2], instruction[3])
            elif command == 'STORE':
                self.STORE(instruction[1], instruction[2], instruction[3])
            elif command == 'JMP':
                self.JMP(instruction[1], instruction[2])
            elif instruction == 'HALT':
                break

        self.print_results()

    def ADD(self, Ra, Rb, Rc):
        self.registers[Rc] = self.registers[Ra] + self.registers[Rb]

    def SUB(self, Ra, Rb, Rc):
        self.registers[Rc] = self.registers[Ra] - self.registers[Rb]

    def MUL(self, Ra, Rb, Rc):
        self.registers[Rc] = self.registers[Ra] * self.registers[Rb]

    def DIV(self, Ra, Rb, Rc):
        self.registers[Rc] = self.registers[Ra] / self.registers[Rb]

    def INC(self, Ra):
        self.registers[Ra] += 1

    def DEC(self, Ra):
        self.registers[Ra] -= 1

    def CMP(self, op, Ra, Rb, Rc):
        if op == '<':
            self.registers[Rc] = self.registers[Ra] < self.registers[Rb]
        elif op == '>':
            self.registers[Rc] = self.registers[Ra] > self.registers[Rb]
        elif op == '<=':
            self.registers[Rc] = self.registers[Ra] <= self.registers[Rb]
        elif op == '>=':
            self.registers[Rc] = self.registers[Ra] >= self.registers[Rb]
        elif op == '==':
            self.registers[Rc] = self.registers[Ra] == self.registers[Rb]
        elif op == '!=':
            self.registers[Rc] = self.registers[Ra] != self.registers[Rb]

    def CONST(self, Ra, value):
        self.registers[Ra] = value

    def LOAD(self, Rs, Rd, offset):
        self.registers[Rd] = self.memory[Rs + offset]

    def STORE(self, Rs, Rd, offset):
        self.memory[Rs + offset] = self.registers[Rd]

    def JMP(self, arg1, offset):
        self.registers['IP'] = self.registers[arg1] + offset

    def print_results(self):
        print(self.registers)
        print(self.memory)


if __name__ == '__main__':
    machine = CPU()

    code = [
        ('CONST', 'Ra', 10),
        ('CONST', 'Rb', 20),
        ('ADD', 'Ra', 'Rb', 'Rc'),
        ('DEC', 'Rc'),
        ('DEC', 'Rc'),
        ('DEC', 'Rc'),
        ('STORE', 1, 'Rc', 3),
        ('HALT')
    ]

    machine.run(code)
