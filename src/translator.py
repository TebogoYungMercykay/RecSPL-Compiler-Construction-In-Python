# Target Code Generator for the RecSPL Language

def generate_assembly(input_filename):
    try:
        with open(input_filename, 'r') as file:
            input_code = file.read()
            
        lines = [line.strip() for line in input_code.split('\n') if line.strip()]
        
        output = []
        output.append("; Generated Assembly Code")
        output.append("section .data")
        
        variables = {}
        function_params = {}
        current_function = None
        
        i = 1  # Skip 'main'
        while i < len(lines):
            line = lines[i].strip()
            
            if ',' in line and 'begin' not in line and '(' not in line:
                var_decl = line.rstrip(',')
                parts = var_decl.split()
                var_type = parts[0]
                var_name = parts[1]
                if var_type == 'num':
                    variables[var_name] = 'dq 0'
                else:
                    variables[var_name] = 'db 0'
                    
            elif '(' in line and ')' in line:
                if line.startswith(('num ', 'void ')):
                    func_name = line.split('(')[0].split()[1]
                    params = line.split('(')[1].split(')')[0].split(',')
                    function_params[func_name] = [p.strip() for p in params]
                    
            i += 1
            
        for var_name, var_type in variables.items():
            output.append(f"    {var_name.lower()} {var_type}")
            
        output.append("\nsection .text")
        output.append("global main")
        output.append("extern printf")
        output.append("extern exit\n")
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line == 'main':
                output.append("main:")
                output.append("    push rbp")
                output.append("    mov rbp, rsp")
                
            elif line.startswith(('num ', 'void ')):
                func_name = line.split('(')[0].split()[1]
                current_function = func_name
                output.append(f"\n{func_name.lower()}:")
                output.append("    push rbp")
                output.append("    mov rbp, rsp")
                
            elif line.startswith('print'):
                var_to_print = line.split()[1].rstrip(';')
                output.append(f"    mov rax, [{var_to_print.lower()}]")
                output.append("    push rax")
                output.append("    call printf")
                output.append("    add rsp, 8")
                
            elif line.startswith('if'):
                if 'eq(' in line:
                    condition = line[line.index('(')+1:line.index(')')].split(',')
                    var1, var2 = condition[0].strip(), condition[1].strip()
                    label_else = f".L{i}_else"
                    label_end = f".L{i}_end"
                    
                    output.append(f"    mov rax, [{var1.lower()}]")
                    output.append(f"    cmp rax, [{var2.lower()}]")
                    output.append(f"    jne {label_else}")
                    
            elif line == 'else':
                label_else = f".L{i-1}_else"
                label_end = f".L{i-1}_end"
                output.append(f"{label_else}:")
                
            elif line.startswith('halt'):
                output.append("    mov rax, 60")
                output.append("    mov rdi, 0")
                output.append("    syscall")
                
            elif line == 'skip':
                output.append("    nop")
                
            elif line == 'end':
                if current_function:
                    output.append("    mov rsp, rbp")
                    output.append("    pop rbp")
                    output.append("    ret")
                    current_function = None
                else:
                    output.append("    mov rsp, rbp")
                    output.append("    pop rbp")
                    output.append("    ret")
                    
            i += 1
            
        output_filename = input_filename.replace('.txt', '.asm')
        
        with open(output_filename, 'w') as file:
            file.write('\n'.join(output))
            
        return f"Generated assembly code has been written to {output_filename}"
        
    except FileNotFoundError:
        return f"Error: Could not find the file {input_filename}"
    except Exception as e:
        return f"Error during code generation: {str(e)}"
