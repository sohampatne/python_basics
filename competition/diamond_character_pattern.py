# Greeting

print(
    "\n--------------------------------------------------------------------------------"
    + "\n\n\nGreetings! Welcome to my alphabet diamond generator!\n"
)

# Variables
user_input_alphabet = input("Enter an alphabet: ")
user_input_space = input("With what do you want to fill in the missing spaces?: ")
input_ascii = ord(user_input_alphabet)
start_ascii = 65
space_counter = input_ascii - start_ascii
middle_space_counter = 1
current_ascii = start_ascii
reverse = False

# Function definitions
def result():
    print(
        user_input_space * space_counter
        + chr(current_ascii)
        + user_input_space * space_counter
    )


# Main Program

# Processing
while True:  # Never ending while loop
    if current_ascii == input_ascii:
        reverse = True

    # Ascend
    if reverse == False:
        if current_ascii == 65:
            result()
            current_ascii += 1
            space_counter -= 1
        if current_ascii > 65:
            print(
                user_input_space * space_counter
                + chr(current_ascii)
                + user_input_space * middle_space_counter
                + chr(current_ascii)
            )
            current_ascii += 1
            space_counter -= 1
            middle_space_counter += 2

    # Descend
    elif reverse == True:
        if current_ascii == 65:
            result()

        if current_ascii > 65:
            print(
                user_input_space * space_counter
                + chr(current_ascii)
                + user_input_space * middle_space_counter
                + chr(current_ascii)
            )
        current_ascii -= 1
        space_counter += 1
        middle_space_counter -= 2

    if current_ascii < start_ascii:
        break
