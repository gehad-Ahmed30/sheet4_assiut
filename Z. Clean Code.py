import re

def clean_cpp_code(code):
    
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    
    code = re.sub(r'//.*', '', code)
    
    code = '\n'.join(line for line in code.splitlines() if line.strip())
    
    return code

def main():
    
    input_code = ''
    while True:
        try:
            line = input()
            input_code += line + '\n'
        except EOFError:
            break
    
    cleaned_code = clean_cpp_code(input_code)
   
    print(cleaned_code)

if __name__ == "__main__":
    main()
