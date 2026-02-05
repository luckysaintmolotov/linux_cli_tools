import subprocess
import getpass
import re

# Get user password
password = getpass.getpass("Enter your super user password: ")

# Function to handle the commands
def run_command(command, password):
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=password.encode())
    return stdout.decode(), stderr.decode()

# Function to contain all maintenance tasks
def maintenance_tasks(password):
    # Define commands to retrieve necessary information for detailed output
    commands = {
        "update": ["sudo", "-S", "apt-get", "update"],
        "upgrade": ["sudo", "-S", "apt-get", "upgrade", "-s"],  # Simulate upgrade to capture details
        "autoclean": ["sudo", "-S", "apt-get", "autoclean"],
        "autoremove": ["sudo", "-S", "apt-get", "autoremove", "-s"]  # Simulate removal to capture details
    }

    # Update task
    print("Starting 'update'...")
    update_stdout, update_stderr = run_command(commands["update"], password)
    if update_stderr:
        print(f"Error while running 'update':")
        print(update_stderr)
    else:
        print("Finished 'update'.")
        # Capture the number of updates pending
        pending_updates = re.search(r'(\d+) upgraded', update_stdout)
        if pending_updates:
            print(f"You have {pending_updates.group(1)} updates pending.")
        else:
            print("No updates pending.")

    # Upgrade task
    print("Starting 'upgrade'...")
    upgrade_stdout, upgrade_stderr = run_command(commands["upgrade"], password)
    if upgrade_stderr:
        print(f"Error while running 'upgrade':")
        print(upgrade_stderr)
    else:
        print("Finished 'upgrade'.")
        # Capture the size of upgrades
        upgraded_packages = re.search(r'(\d+) upgraded', upgrade_stdout)
        size_match = re.search(r'Total upgrade size: (\d+ \w+)', upgrade_stdout)
        
        if upgraded_packages and size_match:
            print(f"Total upgrades: {upgraded_packages.group(1)} packages, size {size_match.group(1)}.")
        else:
            print("No upgrades available or no packages to upgrade.")

    # Autoclean task
    print("Starting 'autoclean'...")
    autoclean_stdout, autoclean_stderr = run_command(commands["autoclean"], password)
    if autoclean_stderr:
        print(f"Error while running 'autoclean':")
        print(autoclean_stderr)
    else:
        print("Finished 'autoclean'.")

    # Autoremove task
    print("Starting 'autoremove'...")
    autoremove_stdout, autoremove_stderr = run_command(commands["autoremove"], password)
    if autoremove_stderr:
        print(f"Error while running 'autoremove':")
        print(autoremove_stderr)
    else:
        print("Finished 'autoremove'.")

# Execute maintenance tasks
if __name__ == "__main__":
    try:
        maintenance_tasks(password)
    finally:
        # Clear the password variable from memory
        password = None  # Effectively "destroys" the password
