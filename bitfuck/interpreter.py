def interpret(program):

    from .preprocessor import preprocessor
    
    MEMORY_SIZE = 30000
    MEMORY_TAPE = [0] * MEMORY_SIZE
    LOOP_STACK = []
    M_Pointer = 0
    B_Pointer = 1
    JUMP_TABLE = preprocessor(program) 
    
    class TapeExhaustionError(Exception):
        pass
    
    
    i = 0
    while i < len(program):
        
        if program[i] == " ":
            pass
        elif program[i] == "!":
            alter = 1 << (8 - B_Pointer)
            MEMORY_TAPE[M_Pointer] ^= alter
        
        elif program[i] == ">":
            old = B_Pointer
            B_Pointer = ((B_Pointer) % 8) + 1
            if old % 8 == 0 and M_Pointer < 30000:
                M_Pointer += 1
            elif M_Pointer == 30000:
                raise TapeExhaustionError("End of Tape")

        elif program[i] == "<":
            if i == len(program) - 1 or program[i+1] == "-":
                if M_Pointer > 0:
                    M_Pointer -= 1
                    B_Pointer = 1
                    i += 1
                else:
                    raise TapeExhaustionError("Cannot go below 0 in memory block")
            else:
                old = B_Pointer
                B_Pointer = ((B_Pointer - 2) % 8) + 1
                if old % 8 == 1 and M_Pointer > 0:
                    M_Pointer -= 1
                elif M_Pointer == 0:
                    raise TapeExhaustionError("Cannot go below memory block 0")


        elif program[i] == ".":
            data = int(MEMORY_TAPE[M_Pointer])
            if i == (len(program) - 1) or program[i+1] != ".":
                print(chr(data), end="")
            else:
                print(data, end="")
                i += 1
                
        elif program[i] == "-":
            if program[i + 1] == ">":
                if M_Pointer < 30000:
                    M_Pointer += 1
                    B_Pointer = 1
                    i += 1
                else:
                    raise TapeExhaustionError("Tape Overflow")
            else:
                raise SyntaxError("- is invalid syntax. Did you mean ->")
                

        elif program[i] == "?":
            LOOP_STACK.append(i)
            loop_count = (bin(MEMORY_TAPE[M_Pointer])).count("1")

        elif program[i] == "[":
            if not LOOP_STACK:
                i = JUMP_TABLE[i]


        elif program[i] == "]":
            if LOOP_STACK:               
                i = JUMP_TABLE[i]
                LOOP_STACK.pop()

        elif program[i] == ",":
            if i != len(program) - 1 and program[i+1] == ",":
                MEMORY_TAPE[M_Pointer] = int(input())
                i += 1
            else:
                MEMORY_TAPE[M_Pointer] = ord(input())

        i += 1

        
