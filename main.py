from typing import List, Dict, Callable

def has_no_spaces(s: str) -> bool:
    return ' ' not in s

def get_validated_input(input_func: Callable[[], str], is_valid: Callable[[str], bool], invalid_message: str) -> str:
    """
    Repeatedly calls input_func until the result passes is_valid.

    Args:
        input_func: A function that returns a string (user input).
        is_valid: A function that returns True if the input is valid.

    Returns:
        A valid input string.
    """
    while True:
        user_input = input_func()
        if is_valid(user_input):
            return user_input
        print(invalid_message)


def get_input_with_default(prompt: str, default: str) -> str:
    """
    Prompt the user for input and return their response.
    If they enter nothing, return the provided default value.

    Args:
        prompt (str): The message to show the user.
        default (str): The default value if user inputs nothing.

    Returns:
        str: The user's input or the default value.
    """
    full_prompt = f"{prompt} (default: {default}): "
    user_input = input(full_prompt).strip()
    return user_input if user_input else default

def get_yes_no(prompt="Please enter yes or no") -> bool:
    yes_variants = {"yes", "y", "Y", "Yes" ""}
    no_variants = {"no", "n", "N", "No"}
    
    while True:
        response = input(prompt + ": ").strip().lower()
        
        if response in yes_variants:
            return True
        elif response in no_variants:
            return False
        else:
            print("Invalid input. Please enter yes or no.")

def select_options(options: List[str], single_select: bool = False) -> List[str]:
    options_dict = {str(i): option for i, option in enumerate(options, start=1)}
    return select_options_from_dict(options_dict, single_select=single_select, allow_all=not single_select)


def select_options_from_dict(
    options_dict: Dict[str, str], 
    single_select: bool = False,
    allow_all: bool = True
) -> List[str]:
    """
    Displays options with string keys and lets the user select by typing keys.

    Args:
        options_dict (Dict[str, str]): Keys and option strings.
        single_select (bool): Allow only one selection.
        allow_all (bool): Allow typing 'all' to select all options (only if not single_select).

    Returns:
        List[str]: Selected options (values).
    """
    if not options_dict:
        print("No options available to select.")
        return []

    if single_select:
        print("Please select one option by entering its key:")
    else:
        print("Please select one or more options by entering their keys separated by spaces:")

    max_key_len = max(len(k) for k in options_dict.keys())
    for key, value in options_dict.items():
        print(f"{key.rjust(max_key_len)}. {value}")

    if allow_all and not single_select:
        print("Type 'all' to select all options.")

    keys_set = set(options_dict.keys())

    while True:
        user_input = input("\nEnter your selection: ").strip().lower()

        if allow_all and not single_select and user_input == "all":
            return list(options_dict.values())

        selected_keys = user_input.split()

        if single_select and len(selected_keys) != 1:
            print("Invalid input: Please select exactly one option.")
            continue

        if all(key in keys_set for key in selected_keys):
            return [options_dict[key] for key in selected_keys]
        else:
            print("Invalid input: One or more keys are not valid. Please try again.")


import os
from pathlib import Path

def interactively_select_directory(root_path: Path) -> str:
    """Navigate directories interactively and return the selected directory path."""
    current_path = os.path.abspath(root_path)

    while True:
        # Get directories in the current path
        dirs = [d for d in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, d))]
        dirs.sort()

        # Display current path and available directories
        print(f"\nCurrent Directory: {current_path}\n")
        for i, directory in enumerate(dirs):
            print(f"{i}: {directory}")

        print("\nOptions:")
        print("  - Enter a number to navigate into a directory.")
        print("  - Type 'b' to go back.")
        print("  - Type 'n' to create a new directory.")
        print("  - Press Enter to select this directory.")

        choice = input("\nChoice: ").strip()

        if choice == "":
            return current_path  # User confirms selection

        elif choice.lower() == "b":
            parent_path = os.path.dirname(current_path)
            if parent_path != current_path:  # Prevent going above root
                current_path = parent_path

        elif choice.lower() == "n":
            new_dir_name = input("Enter new directory name: ").strip()
            if new_dir_name:
                new_dir_path = os.path.join(current_path, new_dir_name)
                try:
                    os.makedirs(new_dir_path, exist_ok=True)
                    print(f"Directory '{new_dir_name}' created.")
                except Exception as e:
                    print(f"Error creating directory: {e}")

        elif choice.isdigit():
            index = int(choice)
            if 0 <= index < len(dirs):
                current_path = os.path.join(current_path, dirs[index])

        else:
            print("Invalid choice, please try again.")
