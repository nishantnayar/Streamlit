# Load packages
import utils
from utils import logger, cleanup_logs, shutdown, header
import os
import datetime
import pandas as pd

header("Starting the data loading process")

########################
# Load Data
########################


# Read Files
folder_path = '.\data'
file_extension = '.txt'

# Get a list of all files in the folder with the specified extension
files = [file for file in os.listdir(folder_path) if file.endswith(file_extension)]
print(f"There are {len(files)} files to be loaded")
logger.info(f"There are {len(files)} files to be loaded")

# Create a dictionary to store file names and their contents
file_contents = {}

# Iterate through the files and load their content
for file in files:
    file_path = os.path.join(folder_path, file)

    # Open the file in read mode
    with open(file_path, 'r', encoding='utf-8') as file_content:
        content = file_content.read()

        # Use the file name (without extension) as the key in the dictionary
        file_name_without_extension = os.path.splitext(file)[0]
        file_contents[file_name_without_extension] = content

for file_name, content in file_contents.items():
    logger.info(f"Contents of {file_name} loaded")
print(f"Contents loaded")

# Add contents into a dataframe
data = pd.DataFrame([file_contents]).transpose().rename(columns={0: 'RawText'})

logger.info(f"Number of records loaded {len(data)}")

if len(files) == len(data):
    logger.info("Number of records match")
else:
    logger.error("Number of records dont match")

# Close the logger at the end
shutdown()

