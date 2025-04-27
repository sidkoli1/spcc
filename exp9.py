import re

# Function to optimize the code
def optimize_code(code_lines):
    # Step 1: Constant Folding
    # Replace constant expressions with their computed values
    constant_folding = {}
    optimized_code = []

    for line in code_lines:
        # Match assignment statements (like T1 = 5*3+10)
        match = re.match(r'([A-Za-z0-9]+)=(.*)', line.strip())
        if match:
            var = match.group(1)
            expression = match.group(2).strip()

            # Check for constant folding: if the expression is purely arithmetic and can be computed
            try:
                value = eval(expression)
                constant_folding[var] = value
                optimized_code.append(f"{var}={value}")
            except:
                optimized_code.append(line)  # Keep the original line if not computable
        else:
            optimized_code.append(line)

    # Step 2: Copy Propagation
    final_code = []
    for line in optimized_code:
        match = re.match(r'([A-Za-z0-9]+)=(.*)', line.strip())
        if match:
            var = match.group(1)
            expression = match.group(2).strip()
            if expression in constant_folding:
                final_code.append(f"{var}={constant_folding[expression]}")
            else:
                final_code.append(line)
        else:
            final_code.append(line)

    # Step 3: Common Sub-Expression Elimination
    computed_expressions = {}
    final_optimized_code = []

    for line in final_code:
        match = re.match(r'([A-Za-z0-9]+)=(.*)', line.strip())
        if match:
            var = match.group(1)
            expression = match.group(2).strip()

            if expression in computed_expressions:
                final_optimized_code.append(f"{var}={computed_expressions[expression]}")
            else:
                computed_expressions[expression] = var
                final_optimized_code.append(line)
        else:
            final_optimized_code.append(line)

    return final_optimized_code

# Function to print the optimized code
def print_optimized_code(optimized_code):
    for line in optimized_code:
        print(line)

# Function to read the code from an input file
def read_input_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

# Main function
def main():
    # Read the input code from the file
    input_code = read_input_file('input_exp9.txt')

    # Optimize the code
    optimized_code = optimize_code(input_code)

    # Output the optimized code
    print("Optimized Code:")
    print_optimized_code(optimized_code)

if __name__ == "__main__":
    main()
 
# INPUT TEXT: 
# T1= 5*3+10 
# T3=T1 
# T2=T1+T3 
# T5=4*T2 
# T6=4*T2+100 
