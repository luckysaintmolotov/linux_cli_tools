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
        },
        "check_disk_space": {
            "command": ["df", "-h"],
            "details": "Displays disk usage for all mounted filesystems to identify space issues."
        },
        "clear_log_files": {
            "command": ["sudo", "journalctl", "--vacuum-time=7d"],  # Adjust as needed for your log clearing method
            "details": "Deletes log files older than 7 days to free up space."
        },
        "system_health_check": {
            "command": ["sudo", "apt-get", "check"],
            "details": "Checks for broken dependencies and missing packages to ensure system integrity."
        }
    }

    # Store the last command and status in a dictionary
    last_status_info = {
        "last_command": "",
        "last_status": "N/A"
    }

    while True:
        selection = show_menu()
        
        if 1 <= selection <= len(commands):
            command_key = list(commands.keys())[selection - 1]
            print(f"\nRunning command: {command_key.replace('_', ' ').capitalize()}...")
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
