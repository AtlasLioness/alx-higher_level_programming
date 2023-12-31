#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    length = len(sys.argv) - 1

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            result = add(a, b)
        elif sys.argv[2] == '-':
            result = sub(a, b)
        elif sys.argv[2] == '*':
            result = mul(a, b)
        elif sys.argv[2] == '/':
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
