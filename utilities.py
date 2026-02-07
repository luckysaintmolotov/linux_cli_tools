import time
from prettytable import PrettyTable

def typewriter_effect(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line after the text

def create_menu_table(options):
    # Create a PrettyTable for the menu
    menu_table = PrettyTable()
    menu_table.field_names = ["Option", "Description"]
    
    for option, description in options.items():
        menu_table.add_row([option, description])
    
    return menu_table
