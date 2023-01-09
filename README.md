# DiSHScript
> **Warning**  
> This language is being ported to general use in favour of pure python for DiSH

## The unified DiSH scripting language
## Usage
1. Install python
2. Install git
3. Type in a terminal 
``` bash
git clone https://github.com/LDevs-Team/DiSHScript/
cd DiSHScript```
4. Create a file (the extension is .ds)
5. Type some code lol
6. Execute it with ```python3 __init__.py (filename)
```

## Supported instructions
LOG: print something. Usage: LOG "text" or LOG variablename

DECLARE: declare a variable. Usage: DECLARE [variablename] [content]

SET: set a variable? Don't use it.

INCREMENT: increment a variable. Usage: INCREMENT [variablename] [increment]

REPEAT: not implemented

END: not implemented

EXEC: executes a command in a shell. Usage: EXEC [command]

EXET: executes a command in a shell and stores the results in a variable. Usage: EXET [command] [variablename]

RUN: runs a submodule (WIP). Usage: RUN [module]

RUNSET: runs a submodule and stores the result in a variable (WIP). Usage: RUNSET [module] [variablename]

DEL: removes a variable. Usage: del [variablename]
