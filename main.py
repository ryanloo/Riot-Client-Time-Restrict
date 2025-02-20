import subprocess
import ctypes
import configparser
from datetime import datetime

# Read configuration file
config = configparser.ConfigParser()
config.read("config.ini")

if not config.has_section("Settings") or not all(key in config["Settings"] for key in ["exe_path", "start_time", "end_time"]):
    ctypes.windll.user32.MessageBoxW(0, "Configuration file is missing required settings. Please update config.ini.", "Config Error", 0x40)
    exit()

try:
    exe_path = config.get("Settings", "exe_path").strip()
    start_time_str = config.get("Settings", "start_time").strip()
    end_time_str = config.get("Settings", "end_time").strip()
    
    # Check if any required config values are empty
    if not exe_path or not start_time_str or not end_time_str:
        ctypes.windll.user32.MessageBoxW(0, "Configuration file contains empty values. Please update config.ini.", "Config Error", 0x40)
        exit()
    
    # Validate time format
    start_time = datetime.strptime(start_time_str, "%H:%M").time()
    end_time = datetime.strptime(end_time_str, "%H:%M").time()
except ValueError:
    ctypes.windll.user32.MessageBoxW(0, "Invalid time format in config.ini. Please use HH:MM (24-hour format).", "Config Error", 0x40)
    exit()
except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, f"Unexpected error: {str(e)}", "Config Error", 0x40)
    exit()

def convert_to_am_pm(time_str):
    return datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")

def is_allowed_time():
    current_time = datetime.now().time()
    
    if start_time <= current_time or current_time <= end_time:
        return True
    return False

if is_allowed_time():
    try:
        subprocess.Popen([exe_path])  # Opens the .exe file
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, "Executable file not found. Please check the path in config.ini.", "File Error", 0x40)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"Unexpected error: {str(e)}", "Execution Error", 0x40)
else:
    formatted_start = convert_to_am_pm(start_time_str)
    formatted_end = convert_to_am_pm(end_time_str)
    ctypes.windll.user32.MessageBoxW(0, "Access denied. You can only open this program between {} and {}.".format(formatted_start, formatted_end), "Access Denied", 0x40)
