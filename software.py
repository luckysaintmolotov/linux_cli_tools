import subprocess
import os
import random
from utilities import typewriter_effect 
from utilities import create_menu_table
def manage_wine(action=None):
        """Manage Wine installation: install or uninstall based on the detected branch."""
        
        def check_gpg_installed():
            """Check if GPG is installed on the system; if not, install it."""
            try:
                subprocess.run(["gpg", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return True
            except FileNotFoundError:
                print("GPG is not installed. Installing it now...")
                try:
                    subprocess.run(["sudo", "apt", "install", "-y", "gnupg2"], check=True)
                    print("GPG installed successfully.")
                    return True
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install GPG: {e}")
                    return False

        def detect_branch():
            """Detect the Ubuntu or Debian branch from /etc/os-release."""
            branch = None
            try:
                with open("/etc/os-release") as f:
                    for line in f:
                        if line.startswith("UBUNTU_CODENAME="):
                            branch = line.split('=')[1].strip().strip('"')
                            break
                        elif line.startswith("VERSION_CODENAME="):
                            branch = line.split('=')[1].strip().strip('"')
                            break
                
                if not branch:
                    raise ValueError("Could not detect the branch from /etc/os-release.")
                return branch
            except Exception as e:
                print(f"Error detecting branch: {e}")
                return None

        def is_wine_installed():
            """Check if Wine is installed."""
            try:
                subprocess.run(["wine", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return True
            except FileNotFoundError:
                return False

        def install_wine(version_name):
            """Install Wine based on the detected branch."""
            try:
                # Step 1: Enable 32-bit architecture
                subprocess.run(["sudo", "dpkg", "--add-architecture", "i386"], check=True)

                # Step 2: Create keyring directory if it doesn't exist
                if not os.path.exists("/etc/apt/keyrings"):
                    os.makedirs("/etc/apt/keyrings", mode=0o755, exist_ok=True)

                # Step 3: Check if GPG is installed
                if not check_gpg_installed():
                    return

                # Step 4: Add the repository key
                subprocess.run(["wget", "-q", "-O", "/tmp/winehq.key", "https://dl.winehq.org/wine-builds/winehq.key"], check=True)
                subprocess.run(["sudo", "gpg", "--dearmor", "-o", "/etc/apt/keyrings/winehq-archive.key", "/tmp/winehq.key"], check=True)

                # Step 5: Add the appropriate repository for the detected branch
                subprocess.run(["sudo", "sh", "-c", f'echo "deb [signed-by=/etc/apt/keyrings/winehq-archive.key] https://dl.winehq.org/wine-builds/debian/ {version_name} main" > /etc/apt/sources.list.d/winehq-{version_name}.list'], check=True)

                # Step 6: Update package list
                subprocess.run(["sudo", "apt", "update"], check=True)

                # Step 7: Install Wine
                subprocess.run(["sudo", "apt", "install", "--install-recommends", "winehq-stable" ,"-y"], check=True)

                print("Wine installation completed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred during installation: {e}")

        def uninstall_wine():
            """Uninstalls Wine and associated packages."""
            try:
                print("Proceeding to uninstall Wine...")
                base_uninstall = [
                    "sudo", "apt", "remove", "--purge", 
                    "winehq-stable", "winehq-devel", "winehq-staging",
                    "wine-devel", "wine-devel-amd64", "wine-devel-i386:i386"
                ]
                subprocess.run(base_uninstall, check=True)
                subprocess.run(["sudo", "apt", "autoremove"], check=True)
                print("Wine has been uninstalled successfully.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while uninstalling: {e}")

        # Main functionality combining install and uninstall
        detected_branch = detect_branch()
        if detected_branch:
            print(f"Detected branch: {detected_branch}")
            if is_wine_installed():
                print("Wine is already installed. Proceeding to uninstall...")
                uninstall_wine()
            elif action == "install":
                install_wine(detected_branch)
            elif action == "uninstall":
                uninstall_wine()
            else:
                print("Invalid action specified. Please choose either 'install' or 'uninstall'.")
        else:
            print("Failed to detect branch. Please specify manually.")

    # Execution

def show_menu():
    options= {
        1: "Manage Wine",
        "q": "Quit"
        
    }
    typewriter_effect(f"------------------------------------------------\n")
    typewriter_effect(f"       ------------SOFTWARE--------------      \n")
    
    for option, description in options.items():
        typewriter_effect(f"|   Option : {option} | Description : {description}    |")
    
    typewriter_effect(f"\n------------------------------------------------")
    
    selection = input("Please Choose: 1-q:\n").strip()
    
    while True:
        if "1" in selection :
            manage_wine()
        if "q" in selection.lower():
            break
        else:
            typewriter_effect("Incorrect Selection/Input. Please try again")
if __name__ == "__main__":
        #user_action = input("Do you want to install or uninstall Wine? (install/uninstall): ").strip().lower()
        #manage_wine(user_action)
        show_menu()