import angr
import claripy

input_file_path = './main'
project = angr.Project(input_file_path, main_opts={'base_addr': 0x00000}) 

# Addresses to find and avoid
findaddr = 0x001012f7  # Address where "Correct!" is printed
avoidaddr = 0x00101311 # Address where "Incorrect." is printed

# Initialize state
state = project.factory.full_init_state(args=['./main'])

# Create symbolic variables for inputs
color_vars = [claripy.BVS(f'color_{i}', 8 * 10) for i in range(4)]  # 10 bytes for each color
food_vars = [claripy.BVS(f'food_{i}', 8 * 10) for i in range(4)]   # 10 bytes for each food

# Constraints for colors
state.solver.add(claripy.Or(color_vars[0] == 3, color_vars[1] == 3))  # Green in the first two
state.solver.add(color_vars[3] == 2)  # Last color is blue
state.solver.add(color_vars[2] != 4)  # Second last color is not yellow

# Constraints for foods
state.solver.add(food_vars[0] == 4)  # First food is chicken
state.solver.add(food_vars[3] != 3)  # Last food is not steak
state.solver.add(claripy.Or(food_vars[0] == 2, food_vars[1] == 2, food_vars[2] == 2, food_vars[3] == 2))

# Ensure all choices are unique within each category
for i in range(3):
    for j in range(i + 1, 4):
        state.solver.add(color_vars[i] != color_vars[j])  # No repeat in colors
        state.solver.add(food_vars[i] != food_vars[j])   # 
# Hook the inputs to the symbolic variables
for i, var in enumerate(color_vars + food_vars):
    state.memory.store(state.regs.rbp - 0x80 - (i * 16), var)  # Adjust the offset as per the binary

# Manage simulation
sim_manager = project.factory.simulation_manager(state)
sim_manager.explore(find=findaddr, avoid=avoidaddr)

# Output the solution
if len(sim_manager.found) > 0:
    for i, var in enumerate(color_vars + food_vars):
        print(f'Input {i+1}:', sim_manager.found[0].solver.eval(var, cast_to=bytes))
else:
    print("No solution found.")
