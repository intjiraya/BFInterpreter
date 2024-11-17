import argparse
from brainfuck.interpreter import BrainfuckInterpreter

def main():
    parser = argparse.ArgumentParser(description="Run Brainfuck code from a file.")
    parser.add_argument("file", type=str, help="Path to the Brainfuck file")
    parser.add_argument("--maxmem", type=int, default=30000, help="Maximum memory size (default: 30000 cells)")
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            code = f.read()

        interpreter = BrainfuckInterpreter(code)
        interpreter.run()

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
