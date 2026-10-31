import sys
from .interpreter import interpret


VERSION = "BitFuck 1.0.0"
HELP = """ 
        BitFuck Interpreter
        
        Usage: 
            btf <file.btf>
        
        Options: 
            --help, -h : Shows this message
            --version, -v : Shows BitFuck Interpreter version
            
        Components:
            Memory Pointer : BitFuck supports a memory tape of 30,000 bytes. Memory Pointer points to the current memory block. 
                             Each Memory block is 8 bits. Indexing starts from 0.
            
            Bit Pointer : Each Memory block has 8 bits, bit pointer points to the current bit, it is initialized at 1st bit of 0th 
                          memory block. Indexing in bits start from 1. If bit pointer is moved to right while it is on 8th bit, it
                          goes to the 1st bit of next block.
                          
            > : Moves bit pointer to right.
            < : Moves bit pointer to left.
            -> : Moves memory pointer to right. Bit pointer is initialised to bit 1.
            <- : Moves memory pointer to left. Bit pointer is initialised to bit 1.
            ! : Flips the bit pointed by bit pointer.
            ? : Stores a loop modifier for the next []. Each '?' is consumed separately, 
                executing the loop body once per set bit in the current memory block.
                The set bit count is recalculated before every execution.
            [ : Loop Start
            ] : Loop Finish
            . : Output as ASCII
            .. : Output as Integer
            , : Input as ASCII
            ,, : Input as Integer
"""

def main():
    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    if args[0] in ("--help", "-h"):
        print(HELP)
        return

    if args[0] in ("--version", "-v"):
        print(VERSION)
        return

    filename = args[0]

    try:
        with open(filename, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"btf: file not found: {filename}")
        sys.exit(1)

    interpret(code)
    
    
if __name__ == "__main__":
    main()

