# Load packages
import utils
from utils import logger, shutdown, header
import os
import pandas as pd
import re

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
# data_1 will contain the raw data as loaded from the raw files

data_1 = pd.DataFrame([file_contents]).transpose().rename(columns={0: 'RawText'})

logger.info(f"Number of records loaded {len(data_1)}")

if len(files) == len(data_1):
    logger.info("Number of records match")
else:
    logger.error("Number of records dont match")

# data_2 will contain an additional column
# CleanedText wil contain the cleaned RawText data

def data_processing(text):
    """
    This function will take the raw text field and perform the following functions in that order and return the processed text.
    1. Remove the html tags in case the data is scrubbed from the website
    2. Keep only alphabets and numbers and remove all other special characters
    """
    # Remove html tags
    processed_text = re.sub(r'<.*?>', '', text)
    # Keep only alphabets and numbers
    processed_text = re.sub(r'[^A-Za-z0-9\s\.,;!?-]', '', processed_text)

    return processed_text


data_2 = data_1.copy()
logger.info(f"Copying 'data_1 into data_2")
data_2['CleanedText'] = data_1['RawText'].apply(data_processing)

logger.info(f"'RawText' cleaned and saved as 'CleanedText'")

if len(data_1) == len(data_2):
    logger.info("Number of records in data_1 and data_2 match")
else:
    logger.error("Number of records in data_1 and data_2 dont match")


# Close the logger at the end
shutdown()
