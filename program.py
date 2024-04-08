import platform
import psutil
from colorama import init, Fore, Style

class GiBytes:
    BYTES_TO_GIBIBYTES = 1024 ** 3  # 1 GiB = 1024^3 bytes
    
    def __init__(self) -> None:
        pass

# Function to gather system information
def get_system_info():
    system_info = {} # Dictionary to store a OS information
    
    # Retrieve OS name and version using "platform" library
    # platform.system - function returns the name of the operating system dependent module imported
    # platform.release - returns the release version of the operating system
    try:
        system_info["OS Name and Version"] = f"{platform.system()} {platform.release()}"
    except Exception as e:
        system_info["OS Name and Version"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}" #  Style.RESET_ALL - used to reset all text formatting and colors to their default values.
    
    # Retrieve processor information
    try:
        # platform.processor - returns the processor name or a description of the CPU
        system_info["Processor Information"] = f"{platform.processor()}"
    except Exception as e:
        system_info["Processor Information"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve memory information
    try:
        total_memory_bytes = psutil.virtual_memory().total # psutil.virtual_memory().total - outputs an information about the system's virtual memory
        total_memory_gib = total_memory_bytes / GiBytes.BYTES_TO_GIBIBYTES

        # Format the memory information with two decimal places and a unit
        memory_info = f"{round(total_memory_gib, 2)} GB"

        # Assign the formatted memory information to the system_info dictionary
        system_info["Memory (GB)"] = memory_info
    except Exception as e:
        system_info["Memory (GB)"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve available disk space
    try:

        # Retrieve disk usage information for the root directory ('/') and convert free space to gibibytes
        free_disk_space_bytes = psutil.disk_usage('/').free
        free_disk_space_gib = free_disk_space_bytes / GiBytes.BYTES_TO_GIBIBYTES

        # Format the disk space information with two decimal places and a unit
        disk_space_info = f"{round(free_disk_space_gib, 2)} GB"

        # Assign the formatted disk space information to the system_info dictionary
        system_info["Available Disk Space (GB)"] = disk_space_info
    except Exception as e:
        system_info["Available Disk Space (GB)"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve current user
    try:
        system_info["Current User"] = f"{psutil.users()}"
    except Exception as e:
        system_info["Current User"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve IP address
    try:
        system_info["IP Address"] = f"{psutil.net_if_addrs()['Ethernet'][0].address}"
    except Exception as e:
        system_info["IP Address"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve system uptime
    try:
        system_info["System Uptime (Seconds)"] = f"{round(psutil.boot_time())}"
    except Exception as e:
        system_info["System Uptime (Seconds)"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve CPU usage
    try:
        system_info["CPU Usage (%)"] = f"{psutil.cpu_percent()} %"
    except Exception as e:
        system_info["CPU Usage (%)"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve disk partitions
    try:
        disk_partitions = psutil.disk_partitions()
        system_info["Disk Partitions"] = disk_partitions
    except Exception as e:
        system_info["Disk Partitions"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve system architecture
    try:
        system_info["System Architecture"] = f"{platform.architecture()[0]}"
    except Exception as e:
        system_info["System Architecture"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
    
    # Retrieve environment variables
    try:
        system_info["Environment Variables"] = dict(psutil.Process().environ())
    except Exception as e:
        system_info["Environment Variables"] = f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

    return system_info

# Function to print system information
def print_system_info(system_info):
    # Print system information with color formatting
    print(Fore.BLUE + "System Information:" + Style.RESET_ALL)
    for key, value in system_info.items():
        if isinstance(value, list):
            # If value is a list (e.g., running processes), print each item in the list
            print(f"{Fore.GREEN}{key}:{Style.RESET_ALL}")
            for process in value:
                print(f"  {process}")
        elif isinstance(value, dict):
            # If value is a dictionary (e.g., environment variables), print key-value pairs
            print(f"{Fore.GREEN}{key}:{Style.RESET_ALL}")
            for k, v in value.items():
                print(f"  {k}: {v}")
        else:
            # Otherwise, print key-value pair directly
            print(f"{Fore.GREEN}{key}:{Style.RESET_ALL} {value}")

init(autoreset=True)  # Initialize colorama to reset colors after each print
# Get system information
system_info = get_system_info()
# Print system information
print_system_info(system_info)
