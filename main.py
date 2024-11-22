from typing import List

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

def select_options(options: List[str]) -> List[str]:
    """
    Displays a list of options and allows the user to select one or more options
    by entering the corresponding numbers, separated by spaces, or 'all' to select all.

    Args:
        options (List[str]): A list of strings representing the options.

    Returns:
        List[str]: The selected options.
    """
    if not options:
        print("No options available to select.")
        return []

    # Display the options with their corresponding numbers
    print("Please select one or more options by entering their numbers separated by spaces:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("Type 'all' to select all options.")

    while True:
        # Get the user's input
        user_input = input("\nEnter your selection: ").strip().lower()

        if user_input == "all":
            # Return all options if 'all' is entered
            return options

        # Validate numerical input
        try:
            selected_indices = list(map(int, user_input.split()))
            if all(1 <= idx <= len(options) for idx in selected_indices):
                # Return the selected options
                return [options[idx - 1] for idx in selected_indices]
            else:
                raise ValueError("Input numbers are out of range.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

