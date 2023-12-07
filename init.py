def collatz_sequence(n):
    steps = 0
    last_three_steps = []
    while n != 1:
        last_three_steps.append(n)
        if len(last_three_steps) > 2:
            last_three_steps.pop(0)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    last_three_steps.append(1)  # Adding 1 to the recorded steps
    return steps, last_three_steps

start_number = 10
steps_to_cycle, last_steps = collatz_sequence(start_number)
print(f"Number of steps to reach 1 in Collatz sequence starting from {start_number}: {steps_to_cycle}")
print(f"Last four steps before reaching the cycle: {last_steps}")
