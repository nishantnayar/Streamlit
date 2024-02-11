# importing module
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import datetime

########################
# configure logger
########################

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt='%H:%M:%S')

# Get current date and time for filename
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

# Define log filename with timestamp
folder = 'logs'
filename = f"{folder}/app_log_{now}.log"

# Create a file handler and set the formatter
file_handler = TimedRotatingFileHandler(
    filename,
    when="H",  # Rotate every Hour
    interval=1,  # Rotate every 1 interval (1 hour in this case)
    backupCount=2,  # Keep up to 2 archived log files
)

file_handler.setFormatter(formatter)

# Create a logger and add the file handler
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

# Set the log level (e.g., INFO, DEBUG)
logger.setLevel(logging.INFO)


# Close the logger at the end
def shutdown():
    logging.shutdown()


########################
# Cleanup logs
########################
def cleanup_logs(folder_path="logs", max_files=3):
    """
    Clears old log files in a directory, keeping only the most recent ones.

    Args:
        folder_path (str, optional): Path to the folder containing log files. Defaults to "logs".
        max_files (int, optional): Maximum number of log files to keep. Defaults to 5.
    """

    log_files = os.listdir(folder_path)
    log_files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)

    files_to_delete = log_files[max_files:]

    for file in files_to_delete:
        full_path = os.path.join(folder_path, file)
        try:
            os.remove(full_path)
            print(f"Deleted log file: {file}")
            logger.info(f"Deleted log file: {file}")
        except FileNotFoundError:
            print(f"Log file not found: {file}")
        except PermissionError:
            print(f"Log file in use: {file}")


# Log headings

def header(header):
    x = '#' * 50
    logger.info(x)
    logger.info(f"## {header}")
    logger.info(x)
