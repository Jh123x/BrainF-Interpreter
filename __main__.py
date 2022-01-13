from argparse import ArgumentParser

from core import Interpreter


if __name__ == '__main__':
    parser = ArgumentParser(description='Brainfuck interpreter')
    parser.add_argument('file', help='The file to run')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Verbose mode'
    )

    args = parser.parse_args()

    # Read the file
    with open(args.file, 'r') as f:
        data = f.read()

    interpreter = Interpreter(data, verbose=args.verbose)
    interpreter.run()
