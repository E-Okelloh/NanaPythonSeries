"""
Days to Hours Converter

A simple utility to convert days into hours.
This module demonstrates Python basics including functions, type hints, and error handling.
"""

from typing import Union

# Configuration constants
HOURS_PER_DAY = 24
UNIT_NAME = "hours"


def days_to_units(num_of_days: Union[int, float]) -> str:
    """
    Convert days to hours.
    
    Args:
        num_of_days: Number of days to convert (positive number expected).
        
    Returns:
        A formatted string with the conversion result or an error message.
        
    Example:
        >>> days_to_units(2)
        '2 days are 48 hours'
    """
    if num_of_days < 0:
        return "Error: Please enter a positive number!"
    
    if num_of_days == 0:
        return f"{num_of_days} days are 0 {UNIT_NAME}"
    
    total_hours = num_of_days * HOURS_PER_DAY
    return f"{num_of_days} days are {total_hours} {UNIT_NAME}"


def main() -> None:
    """Main function to run the days to hours converter."""
    try:
        user_input = input(
            "Hey user, enter the number of days and I will convert it into hours\n"
        )
        
        # Attempt to convert input to a number (int or float)
        user_input_number = float(user_input)
        
        # Calculate and display result
        result = days_to_units(user_input_number)
        print(result)
        
    except ValueError:
        print("Error: Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
