from . import Environment

class Interpreter(object):
    def __init__(self, code:str, verbose:bool = False) -> None:
        """The Interpreter to run the code"""
        self.environment = Environment()
        self.code = code
        self.index = 0
        self.verbose = verbose

    def _normal_cmd(self, command:str) -> None:
        """Execute normal commands that doesn't branch / loop"""
        try:
            self.environment.parse_command(command)
        except ValueError as exp:
            print(f"Error at {self.index + 1}: {exp}")
            self.index = len(self.code)
        self.index += 1

    def _find_closing_bracket(self, start_index:int) -> int:
        """Finds the index of the next closing bracket"""
        curr_index = start_index
        curr_token = self.code[curr_index]
        while(curr_token != ']'):
            if curr_token == ']':
                self._find_closing_bracket(curr_index)
            curr_index += 1

            if curr_index > len(self.code):
                raise ValueError('Unmatched brackets')

            curr_token = self.code[curr_index]
        return curr_index

    def loop(self, code:str) -> None:
        """
        The code fragment to loop
        Excluding the brackets
        """
        while(self.environment.array[self.environment.current_ptr] != 0):
            for cmd in code:
                self.environment.parse_command(cmd)
        self.index += len(code) + 2

    def run(self, code: str = None) -> None:
        """Run the code"""
        if code is not None:
            code = self.code

        while(self.index < len(self.code)):
            current_token = self.code[self.index]

            if self.verbose:
                print(f"{self.index}: {current_token}")

            # Loop conditional
            if current_token == '[':
                # Look for the end of the loop
                closing_index = self._find_closing_bracket(self.index)
                assert self.code[closing_index] == ']'
                loop_fragment = self.code[self.index + 1: closing_index]
                self.loop(loop_fragment)
            else:
                self._normal_cmd(current_token)
            
