
def preprocessor(program):
    STACK = []
    JUMP_TABLE = {}

    for ptr in range(len(program)):
        
        if program[ptr] == "?":
            STACK.append(ptr)

        elif program[ptr] == "[":
            while STACK:
                data = STACK.pop()
                JUMP_TABLE[data] = ptr 
            STACK.append(ptr)

        elif program[ptr] == "]":
            if not STACK:
                raise SyntaxError("Missing [")
            idx = STACK.pop()
            JUMP_TABLE[ptr] = idx
            JUMP_TABLE[idx] = ptr
    
    return JUMP_TABLE