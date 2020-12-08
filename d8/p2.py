#!/usr/bin/env python3


change = {"nop": "jmp", "acc": "acc", "jmp": "nop"}


if __name__ == "__main__":
    prog = []

    with open("input", "r") as fn:
        for line in fn:
            code, arg = line.strip().split()
            prog.append((code, int(arg)))

    visited = set()
    pc = 0
    acc = 0

    changed = -1

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
            print(f"loop! acc={acc}, pc={pc} changed={changed}")

            if changed != -1:
                prog[changed] = (change[prog[changed][0]], prog[changed][1])
            changed += 1

            if changed < len(prog):
                prog[changed] = (change[prog[changed][0]], prog[changed][1])
                pc = 0
                acc = 0
                visited = set()

            else:
                print("no solution!")
                break

        if pc >= len(prog):
            print(f"end! acc={acc}, pc={pc} changed={changed}")
            break
