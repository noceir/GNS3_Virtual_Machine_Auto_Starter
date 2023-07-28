# Import necessary libraries
import psutil            # For process management and monitoring
import subprocess       # For running external commands
import time             # For adding delays
import os               # For interacting with the operating system
import sys              # For accessing Python interpreter settings

# Function to check if a process is currently running
def check_process_running(process_name):
    # Use psutil to get a list of running processes
    # Check if the process name (case-insensitive) is present in any of the running process names
    return any(process_name.lower() in proc.info['name'].lower() for proc in psutil.process_iter(['name']))

# Function to start the virtual machine using VMware Workstation
def start_virtual_machine(vm_executable_path, vm_config_path):
    try:
        # Run the 'vmrun' command to start the virtual machine with the specified VMX configuration file
        subprocess.Popen([vm_executable_path, 'start', vm_config_path], shell=True)
        print("Virtual machine is starting...")
    except Exception as e:
        # Print an error message if there is an issue starting the virtual machine
        print(f"Error starting virtual machine: {e}")

# Main function of the script
def main():
    # Define the names and paths required for the GNS3 and virtual machine monitoring
    gns3_process_name = 'gns3'
    vm_executable_path = "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmrun.exe"
    vm_config_path = 'C:\\Users\\CLOUD\\Documents\\Virtual Machines\\GNS3VM\\GNS3VM.vmx'

    # Loop to continuously monitor GNS3 and start the virtual machine when GNS3 is launched
    while True:
        # Wait for GNS3 to be launched by checking if the process is running
        while not check_process_running(gns3_process_name):
            time.sleep(5)   # Sleep for 5 seconds before checking again

        # Wait for VMware Workstation to fully launch (add more time if needed)
        time.sleep(8)

        # GNS3 is running, start the virtual machine using the defined VMX configuration file
        start_virtual_machine(vm_executable_path, vm_config_path)

        # Loop to wait until GNS3 is closed
        while check_process_running(gns3_process_name):
            time.sleep(5)   # Sleep for 5 seconds before checking again

        # GNS3 is closed, print a message, wait, and restart the script to resume monitoring
        print("GNS3 is closed, restarting the script...")
        time.sleep(5)
        python = sys.executable
        os.execl(python, python, *sys.argv)

# Run the 'main' function if this script is executed directly
if __name__ == "__main__":
    main()
