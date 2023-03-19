import sys

def main():
    prog = check_com_line_arg()
    print(code_lines_count(prog))

def check_com_line_arg():
    try:
        assert len(sys.argv) > 1, "Too few command-line arguments"
        assert len(sys.argv) < 3, "Too many command-line arguments"
        assert sys.argv[1].endswith(".py") == True, "Not a Python file"
        return sys.argv[1]
    except AssertionError as message:
        sys.exit(message)

def code_lines_count(prog):
    try:
        t = 0
        file = open(prog, "r")
        for line in file:
            if len(line.strip()) !=0 and line.strip().startswith("#") != True:
                t +=1
        file.close()
        return t
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()