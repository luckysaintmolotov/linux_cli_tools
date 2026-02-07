import subprocess
import getpass

# Get user password
password = getpass.getpass("Enter your super user password: ")

# Function to handle the commands
def run_command(command, password):
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Send the password to the command
    stdout, stderr = process.communicate(input=(password + '\n').encode())

    if process.returncode == 0:
        return f"Success: {stdout.decode().strip()}", ""
    else:
        return "", f"Error: {stderr.decode().strip()}"

# Function to contain all maintenance tasks
def maintenance_tasks(password):
    # Define commands to retrieve necessary information for detailed output
    commands = {
        "update": {
            "command": ["sudo", "-S", "apt-get", "update"],
            "details": "Updates the package list from the repositories, ensuring the package index is up to date."
        },
        "upgrade": {
            "command": ["sudo", "-S", "apt-get", "upgrade", "-s"],  # Simulate upgrade to capture details
            "details": "Upgrades all installed packages to the latest versions available in the repositories (simulated)."
        },
        "autoclean": {
            "command": ["sudo", "-S", "apt-get", "autoclean"],
            "details": "Removes package files from the local repository that can no longer be downloaded (cleans up the package cache)."
        },
        "autoremove": {
            "command": ["sudo", "-S", "apt-get", "autoremove", "-s"],  # Simulate removal to capture details
            "details": "Removes packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed (simulated)."
        }
    }

    # Store the last command and status in a dictionary
    last_status_info = {
        "last_command": "",
        "last_status": "N/A"
    }

    while True:
        def show_menu():  
            menu_count = 0  
            print(f"""
{"-"*30}
Please choose from the list:\n{"-"*30}\n""")
            for key in commands:
                menu_count += 1
                print(f"{menu_count}: {key.capitalize()} - {commands[key]['details']}")
            print(f"{menu_count + 1}: Quit")
            print(f"{'-'*100}\nLast Command Run: {last_status_info['last_command'].capitalize() if last_status_info['last_command'] else 'None'}")
            print(f"Last Command Status: {last_status_info['last_status']}\n")
            
            selection = int(input(f"Please select from the menu (1-{menu_count + 1}):\n"))
            
            return selection
        
        selection = show_menu()
        
        if 1 <= selection <= len(commands):
            command_key = list(commands.keys())[selection - 1]
            print(f"\nRunning command: {command_key.capitalize()}...")
            success_msg, error_msg = run_command(commands[command_key]['command'], password)

            if success_msg:
                print(success_msg)
                last_status_info['last_command'] = command_key
                last_status_info['last_status'] = "Success"
            if error_msg:
                print(error_msg)
                last_status_info['last_command'] = command_key
                last_status_info['last_status'] = "Failure"
        elif selection == len(commands) + 1:
            print("Exiting the maintenance tool. Goodbye!")
            break
        else:
            print("Wrong selection made")          

# Execute maintenance tasks
if __name__ == "__main__":
    try:
        maintenance_tasks(password)
    finally:
        # Clear the password variable from memory
        password = None  # Effectively "destroys" the password
