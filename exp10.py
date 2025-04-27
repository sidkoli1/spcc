# Register and descriptor setup
registers = ["R0", "R1"]
reg_descriptor = {reg: "empty" for reg in registers}
addr_descriptor = {}

def get_free_register():
    for reg in registers:
        if reg_descriptor[reg] == "empty":
            return reg
    return registers[0]  # fallback overwrite

def update_descriptors(var, reg):
    reg_descriptor[reg] = var
    addr_descriptor[var] = reg

def generate_code(statement):
    parts = statement.split("=")
    lhs = parts[0].strip()
    rhs = parts[1].strip()
    code = []

    if '+' in rhs:
        op1, op2 = map(str.strip, rhs.split('+'))

        reg1 = addr_descriptor.get(op1, get_free_register())
        if reg_descriptor[reg1] == "empty":
            code.append(f"MOV {op1}, {reg1}")
            update_descriptors(op1, reg1)

        reg2 = addr_descriptor.get(op2, get_free_register())
        if reg2 != reg1 and reg_descriptor[reg2] == "empty":
            code.append(f"MOV {op2}, {reg2}")
            update_descriptors(op2, reg2)

        code.append(f"ADD {reg2}, {reg1}")
        update_descriptors(lhs, reg1)

    elif '-' in rhs:
        op1, op2 = map(str.strip, rhs.split('-'))
        reg = get_free_register()
        code.append(f"MOV {op1}, {reg}")
        code.append(f"SUB {op2}, {reg}")
        update_descriptors(lhs, reg)

    return code

print("Enter 3AC statements one per line (type 'done' to finish):")
three_ac_code = []

while True:
    stmt = input()
    if stmt.lower() == "done":
        break
    if '=' in stmt:
        three_ac_code.append(stmt.strip())

print("\n{:<15} {:<30}".format("Statement", "Code Generated"))

for stmt in three_ac_code:
    code_lines = generate_code(stmt)
    for line in code_lines:
        print("{:<15} {:<30}".format(stmt, line))
# t=a-b
# u=a-c
# v=t+u
# d=v+u
# done
