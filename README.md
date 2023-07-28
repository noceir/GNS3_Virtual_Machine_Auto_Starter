### GNS3 Virtual Machine Auto-Starter
- [Python](https://www.python.org/downloads/) (version 3.x)
- [psutil](https://pypi.org/project/psutil/) Python library for process management
- VMware Workstation installed on the system
### Installation
1. Clone or download the script to your local machine.
2. Install the required `psutil` library using pip:
		`pip install psutil`
3. Update the script with the appropriate paths and settings:

- Set `gns3_process_name` to the name of the GNS3 process as shown in the task manager.
- Set `vm_executable_path` to the full path of the `vmrun.exe` executable for VMware Workstation.
- Set `vm_config_path` to the full path of the virtual machine configuration file (VMX).
### Usage
1. Ensure that the virtual machine is properly configured and working within VMware Workstation.
2. The script will continuously monitor GNS3. Once GNS3 is launched, it will automatically start the virtual machine.
3. Put a shortcut of the script in Startup file (using W+R `shell:startup`")
4. Keep the script running in the background while using GNS3. It will handle the monitoring and virtual machine startup process automatically.
### Notes
- Make sure to keep the script running to maintain the monitoring and automatic virtual machine startup functionality.
##### Disclaimer
- This script is provided as-is, without any warranty. Use it at your own risk.
- Ensure that you have the necessary permissions to execute the script and access the required virtual machine and GNS3 resources.