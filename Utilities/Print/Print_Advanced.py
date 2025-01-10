# Print the separator
print('-' * 20)
# --------------------

import time
total_steps = 10

for step in range(total_steps):
    print(f"Processing step {step + 1} out of {total_steps}...", end='\r')
    time.sleep(1)  # Simulating some work with a sleep

print("\nProcessing complete!")
# The message "Processing step X out of 10..." updates in place on the same line, rather than being printed on new lines each time. 
# This kind of display is particularly useful for real-time progress updates in command-line applications.
