import maintenance_tasks as maintenance
import random
from utilities import typewriter_effect, create_menu_table

# List of themed quotes
quotes = [
    "In the void, we find potential. - Unknown",
    "Embrace the emptiness; it's where innovation begins. - Unknown",
    "From nothingness, everything is born. - Unknown",
    "Nihility is the cradle of order and chaos. - Unknown",
    "In the abyss, we discover the light. - Unknown",
    "The future is a thing we make. - Unknown",
    "What does not exist cannot be destroyed. - Dune",
    "You must first let go of the past; only then can you seize the future. - The Matrix",
    "In the space between thoughts lies the key to our reality. - The Matrix Inspired",
    "The eyes are the windows to the soul, and the soul to the abyss. - Blade Runner Inspired",
    "The only limit is the one you set for yourself. - Unknown",
    "Life is not about finding yourself; it’s about creating yourself. - Unknown",
    "Every choice we make is a step into the void. - Unknown",
    "In a world of chaos, order is a fleeting illusion. - Unknown",
    "To see beyond the stars, you must first look into the void. - Unknown",
]

def display_menu():
    options = {
        "1": "Maintenance Tasks",
        "2": "Quit"
    }

    # Create the menu table
    menu_table = create_menu_table(options)
    
    typewriter_effect("\n" + "=" * 50)
    typewriter_effect("        Welcome to Nihility System Tweaks")
    typewriter_effect("=" * 50)
    typewriter_effect(f"\"{random.choice(quotes)}\"")
    typewriter_effect("=" * 50)
    print(menu_table)
    typewriter_effect("=" * 50)

def main():
    while True:
        display_menu()

        selection = int(input("Select an option (1-2):\n"))
        
        if selection == 1:
            # Placeholder for actual function call
            typewriter_effect(f"Running Nihility System Tweaks")
            maintenance.maintenance_tasks()
        elif selection == 2:
            typewriter_effect("Thank you for using Nihility System Tweaks. Goodbye!")
            break
        else:
            typewriter_effect("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
