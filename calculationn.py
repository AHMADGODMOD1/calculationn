import sys
import time
import random  # For random choice between Red and Green
from datetime import datetime

# ANSI escape sequences for colors (Yellow and Magenta excluded)
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

# Define the correct key
CORRECT_KEY = "@AHMAD_GODMOD1"  # Change this to your desired key

def verify_key():
    while True:  # Loop until a correct key is entered
        key = input(f"{BRIGHT_CYAN}Please enter the key to continue: {RESET}")
        
        if key == CORRECT_KEY:
            print(f"{BRIGHT_GREEN}Key verified! You can now proceed.{RESET}")
            break  # Exit the loop if key is correct
        else:
            print(f"{BRIGHT_RED}Invalid key! Please try again.{RESET}")
            print(f"{BRIGHT_RED}If you don't have a key, please contact AHMAD_GODMOD1 to buy one.{RESET}")

def select_server():
    print(f"{BRIGHT_CYAN}Available Servers:")
    print(f"{BRIGHT_WHITE}1. Server 1")
    print(f"{BRIGHT_WHITE}2. Server 2")
    print(f"{BRIGHT_WHITE}3. Server 3")

    server_choice = input(f"{BRIGHT_CYAN}Please select a server (1/2/3): {RESET}")
    if server_choice in ['1', '2', '3']:
        print(f"{BRIGHT_GREEN}Server {server_choice} connected successfully!{RESET}")
    else:
        print(f"{BRIGHT_RED}Invalid server choice!{RESET}")
        select_server()  # Re-run server selection if invalid choice

def display_welcome_message():
    print(f"{BRIGHT_CYAN}" + "*" * 42)
    print(f"{BRIGHT_BLUE}   Welcome to @AHMAD_GODMOD1 Python Code")
    print(f"{BRIGHT_CYAN}" + "*" * 42 + f"{RESET}")
    time.sleep(2)

def show_calculation_animation(period_number, last_result, second_result, total, final_result):
    steps = [
        f"{period_number} + {last_result} = {total}",
        f"{second_result} - {total} = {final_result}"
    ]

    for step in steps:
        print(f"{BRIGHT_WHITE}{step}{RESET}")
        time.sleep(1.5)

def calculate_result():
    period_number = int(input(f"{BRIGHT_CYAN}Please enter the last 1 period number: {RESET}"))
    last_result = int(input(f"{BRIGHT_CYAN}Please enter the last result number: {RESET}"))
    second_result = int(input(f"{BRIGHT_CYAN}Enter the 2nd result number: {RESET}"))

    total = period_number + last_result
    final_result = abs(second_result - total)

    show_calculation_animation(period_number, last_result, second_result, total, final_result)

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"{BRIGHT_CYAN}" + "=" * 42 + f"{RESET}")
    print(f"{BRIGHT_BLUE}Current Time: {BRIGHT_WHITE}{current_time}{RESET}")
    print(f"{BRIGHT_CYAN}" + "=" * 42 + f"{RESET}")

    input(f"{BRIGHT_GREEN}Calculation is done! Press Enter to get your results.{RESET}")

    accuracy = (30 + (final_result % 71))
    print(f"{BRIGHT_GREEN}Result Accuracy: {BRIGHT_WHITE}{accuracy}%{RESET}")
    print(f"{BRIGHT_CYAN}" + "=" * 42 + f"{RESET}")

    result_message = ""
    if final_result > 10:
        random_result = random.choice(["Red", "Green"])
        if random_result == "Red":
            result_message = f"{BRIGHT_RED}Red{RESET}"
        else:
            result_message = f"{BRIGHT_GREEN}Green{RESET}"
    elif final_result in [2, 4, 0]:
        result_message = f"{BRIGHT_RED}Small Red{RESET}"
    elif final_result in [1, 3]:
        result_message = f"{BRIGHT_GREEN}Small Green{RESET}"
    elif final_result in [5, 7, 9]:
        result_message = f"{BRIGHT_GREEN}Big Green{RESET}"
    elif final_result in [6, 8]:
        result_message = f"{BRIGHT_RED}Big Red{RESET}"
    elif final_result == 10:
        result_message = f"{BRIGHT_WHITE}Skip{RESET}"

    print(result_message)
    print(f"{BRIGHT_CYAN}" + "=" * 42 + f"{RESET}")

def update_results():
    result_input = input(f"{BRIGHT_CYAN}Enter 'W' for Win, 'L' for Loss, 'S' for Skip or 'E' to Exit: {RESET}").strip().upper()

    if result_input == 'E':
        exit_program()
        return
    elif result_input not in ['W', 'L', 'S']:
        print(f"{BRIGHT_RED}Invalid input. Please enter 'W', 'L', 'S', or 'E'.{RESET}")

def exit_program():
    print(f"{BRIGHT_CYAN}Exiting the program...{RESET}")
    time.sleep(1)
    print(f"{BRIGHT_BLUE}Server is disconnected.{RESET}")
    print(f"{BRIGHT_CYAN}Thank you for using the program! Goodbye!{RESET}")
    sys.exit()

def main_loop():
    verify_key()  # Check the key before starting
    display_welcome_message()
    select_server()  # Server selection after key verification
    while True:
        calculate_result()
        update_results()

if __name__ == "__main__":
    main_loop()