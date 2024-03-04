import angr
import claripy

def main():
    # Load the binary
    p = angr.Project('challenge', auto_load_libs=False)

    # Create a symbolic bitvector for input (adjust length as needed)
    flag_len = 34  # Adjust based on expected input size
    flag_chars = [claripy.BVS(f'flag_char{i}', 8) for i in range(flag_len)]
    flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])  # Append newline

    # Create a state with the symbolic input
    state = p.factory.entry_state(stdin=flag)

    # Add constraints to the flag (e.g., printable ASCII characters)
    for c in flag_chars:
        state.solver.add(c >= 33)  # Space character
        state.solver.add(c <= 126)  # '~'

    # Create a simulation manager
    # Create a simulation manager
    sm = p.factory.simulation_manager(state)

# Adjust the find and avoid parameters based on your program's specifics
    sm.explore(find=lambda s: b"Correct!" in s.posix.dumps(1), 
           avoid=lambda s: b"No good." in s.posix.dumps(1))

# Check if we found a solution
    if sm.found:
        found_state = sm.found[0]
        solution = found_state.solver.eval(flag, cast_to=bytes).rstrip(b'\n')
        print(f"Flag: {solution}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
