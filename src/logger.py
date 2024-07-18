# In software development, a logger function is used to record messages that provide information about the execution of a program. These messages can be used for debugging, monitoring, and auditing purposes.

import os
import logging
from datetime import datetime

# Generate a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the full path for the log file, placing it inside a "logs" directory in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure the "logs" directory exists
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file itself
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file to write to
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Set the format for log messages
    level=logging.INFO,  # Set the logging level to INFO
)


# This code snippet sets up a logging system that:

''' 1. Creates a log file named with the current date and time.

2. Ensures the log file is placed in a "logs" directory within the current working directory.

3. Configures the logging format to include the timestamp, line number, logger name, severity level, and message.

4. Sets the logging level to INFO, so messages at this level and higher are recorded.'''