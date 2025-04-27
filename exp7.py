def build_precedence_table():
    precedence_table = {}
    symbols = ['id', '+', '*', '$']
    for a in symbols:
        precedence_table[a] = {}
        for b in symbols:
            if a == 'id':
                precedence_table[a][b] = '>' if b in ['+', '*', '$'] else '-'
            elif a == '+':
                precedence_table[a][b] = '<' if b == 'id' else '>' if b in ['+', '$'] else '<'
            elif a == '*':
                precedence_table[a][b] = '<' if b == 'id' else '>'
            elif a == '$':
                precedence_table[a][b] = '<' if b != '$' else 'accept'
    return precedence_table

def print_precedence_table(precedence_table):
    symbols = ['id', '+', '*', '$']
    print("Precedence Table:")
    print("    " + " ".join(symbols))
    print("-" * 40)
    for row in symbols:
        print(row.ljust(4), " ".join(precedence_table[row][col] for col in symbols))

def get_precedence(precedence_table, a, b):
    return precedence_table[a][b]

def reduce(stack):
    if stack[-1] == 'id':
        stack.pop()
        stack.append('E')
        return "Reduce E -> id"
    elif len(stack) >= 3 and stack[-3] == 'E' and stack[-1] == 'E':
        op = stack[-2]
        if op == '+':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('E')
            return "Reduce E -> E + E"
        elif op == '*':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('E')
            return "Reduce E -> E * E"
    return "Error in reduction"

def parse(input_string):
    precedence_table = build_precedence_table()
    print_precedence_table(precedence_table)
    
    stack = ['$']
    input_list = input_string.split() + ['$']
    
    print("\nStack\t\t\tInput\t\t\tAction")
    print("=" * 70)
    
    while True:
        print(" ".join(stack).ljust(24), " ".join(input_list).ljust(24), end=' ')
        top = stack[-1] if stack[-1] != 'E' else stack[-2]
        next_input = input_list[0] if input_list else '$'
        precedence = get_precedence(precedence_table, top, next_input)

        if precedence == '<':
            action = f"Shift {next_input}"
            stack.append(input_list.pop(0))
        elif precedence == '>':
            action = reduce(stack)
        elif precedence == 'accept':
            print("Accept")
            break
        else:
            print("Error")
            return
        print(action)
        if next_input == '$' and stack == ['$E']:
            print("Accept")
            break

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

input_file = 'input_exp7.txt'
input_string = read_input_from_file(input_file)
parse(input_string)
# Input.txt: 
# id + id * id  
