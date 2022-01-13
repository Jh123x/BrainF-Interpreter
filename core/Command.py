"""
Interface for command functions

def (func_name)(array:list, current_ptr: int) -> Optional[int]:
    # Operations here
    return new_current_pointer
"""

import sys


def inc_pointer(array: list, current_ptr: int) -> int:
    """Increment the pointer"""
    while len(array) <= current_ptr + 1:
        array.append(0)
    return current_ptr + 1


def dec_pointer(_, current_ptr: int) -> int:
    """Decrement the pointer"""
    return current_ptr - 1


def inc_data(array: list, current_ptr: int) -> None:
    """Increment the data"""
    array[current_ptr] += 1


def dec_data(array: list, current_ptr: int) -> None:
    """Decrement the data"""
    array[current_ptr] -= 1


def output_byte(array: list, current_ptr: int) -> None:
    """Output the byte at the data"""
    print(chr(array[current_ptr]), end="")


def input_byte(array: list, current_ptr: int) -> None:
    """Input a byte and store it at the data"""
    curr_char = sys.stdin.read(1)
    array[current_ptr] = ord(curr_char)
