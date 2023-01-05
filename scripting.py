import re, time, os, subprocess

def parse(f:str) -> list[tuple[str]]:
    lines = f.splitlines()
    symbols = []
    for a in lines:
        a = re.sub(r'#(\s|\S)+', "", a)
        print(a)
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

def run(symbols:list[str], modules:dict[str, callable]) -> None:
    variables = {} # declare variables context
    loops = {} # declare loops context
    for a in symbols:
        if len(a) < 1:
            continue
        instruction = a[0]
        match instruction:
            case "LOG":
                if a[1] in variables.keys():
                    print(variables[a[1]])
                else:
                    print(a[1:])
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
                raise NotImplementedError("If you look closely, you can see that I couldn't bother to implement this :)")
            case "END":
                raise NotImplementedError("If you look closely, you can see that I couldn't bother to implement this :)")
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
            
f = open("test.ds", "r")
content = f.read()
# print(parse(content))
run(parse(content), {"screenshot": lambda : "L"})
f.close()

while True:    pass