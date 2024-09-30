class Logger:
    def __init__(self, program):
        self.current_line = 1
        self.output = []
        self.program = program
    
    def raiseError(self,):
        self.output.append(f'ERROR at line {self.current_line}')
        self.program.terminate()
    
    def print(self, output_str):
        self.output.append(output_str)