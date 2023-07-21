# define and use a loop variable

def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print("Too few.")
    elif num_cycles > 4:
        print("Too many.")
    else:
        for N in range(1, num_cycles + 1):
            print(f"{N} : Lather and rinse.")

        print("Done.")


user_cycles = int(input())
shampoo_instructions(user_cycles)