import re, time, os, subprocess

def parse(f:str) -> list[tuple[str]]:
    lines = f.splitlines()
    symbols = []
    for a in lines:
        a = re.sub(r'#(\s|\S)+', "", a)
        found = re.findall(r'("([^"]*)")|(\w+)', a)
        sanitized = []
        line_symbols = []
        for x in found:
            for j in x:
                if j != "":
                    sanitized.append(j)

            line_symbols.append(sanitized[-1])
        symbols.append(line_symbols)
    return symbols

def run(symbols:list[str], modules:dict[str, callable], variables_override:dict={}) -> None:
    variables = variables_override or {} # declare variables context
    in_loop = False # declare loops context
    loop_instructions = []
    loop_times = 0
    loop_varname = ""
    for a in symbols:
        if len(a) < 1:
            continue
        instruction = a[0]
        if in_loop == True:
            print("lul")
            if instruction == "END":
                pass
            else:
                loop_instructions.append(a)
                continue
        match instruction:
            case "LOG":
                if a[1] in variables.keys():
                    print(variables[a[1]])
                else:
                    print(" ".join(a[1:]))
            case "DECLARE":
                if a[1] == "int":
                    variables[a[2]] = int(a[3])
                elif a[1] == "str":
                    variables[a[2]] = a[3]
            case "SET":
                variables[a[1]] = a[2]
            case "INCREMENT":
                if isinstance(a, int):
                    variables[a[1]] += int(a[2])
                else:
                    variables[a[1]] = int(variables[a[1]])
                    variables[a[1]] += int(a[2])
            case "REPEAT":
                in_loop = True
                loop_varname = a[2]
                loop_times = int(a[1])
                # raise NotImplementedError("If you look closely, you can see that I couldn't bother to implement this :)")
            case "END":
                in_loop = False
                for j in range(loop_times):
                    variables[loop_varname] = j+1
                    run(loop_instructions, modules, variables_override=variables)
                loop_instructions = []
                # raise NotImplementedError("If you look closely, you can see that I couldn't bother to implement this :)")
            case "EXEC":
                os.system(a[1])
            case "EXET":
                sp = subprocess.run(a[1], shell=True, capture_output=True)
                variables[a[1]] = sp.stdout
            case "RUN":
                modules[a[1]]()
            case "RUNSET":
                variables[a[2]] = modules[a[1]]()
            case "DEL":
                del variables[a[1]]

# while True:    pass