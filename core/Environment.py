from . import inc_pointer, inc_data, dec_data, dec_pointer, output_byte, input_byte


class Environment(object):
    command_dict: dict = {
        '>': inc_pointer,
        '<': dec_pointer,
        '+': inc_data,
        '-': dec_data,
        '.': output_byte,
        ',': input_byte,
    }

    def __init__(self) -> None:
        """The environment to run in"""
        # Setup the environment
        self.array: list = [0]
        self.current_ptr: int = 0

    def parse_command(self, curr_token: str) -> None:
        """Parsing commands"""
        command = self.command_dict.get(curr_token, None)

        if command is None:
            raise ValueError(f'Invalid code {curr_token}')

        new_ptr = command(self.array, self.current_ptr)
        if new_ptr is not None:
            self.current_ptr = new_ptr
