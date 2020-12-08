#!/usr/bin/env python3


if __name__ == "__main__":
    prog = []

    with open("input", "r") as fn:
        for line in fn:
            code, arg = line.strip().split()
            prog.append((code, int(arg)))

    visited = set()
    pc = 0
    acc = 0

    while True:
        visited.add(pc)
        code, arg = prog[pc]

        if code == "acc":
            acc += arg
            pc += 1

        elif code == "nop":
            pc += 1

        elif code == "jmp":
            pc += arg

        else:
            assert False, "unknown op: " + code

        if pc in visited:
            print(f"loop! acc={acc}, pc={pc}")
            break

        if pc >= len(prog):
            print(f"end! acc={acc}, pc={pc}")
            break
