def get_yes_no(prompt="Please enter yes or no: ") -> bool:
    yes_variants = {"yes", "y", "Y", "Yes" ""}
    no_variants = {"no", "n", "N", "No"}
    
    while True:
        response = input(prompt).strip().lower()
        
        if response in yes_variants:
            return True
        elif response in no_variants:
            return False
        else:
            print("Invalid input. Please enter yes or no.")
