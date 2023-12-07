def collatz_sequence(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

start_number = 30
steps_to_cycle = collatz_sequence(start_number)
print(f"Number of steps to reach 1 in Collatz sequence starting from {start_number}: {steps_to_cycle}")
