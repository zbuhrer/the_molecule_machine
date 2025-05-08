import logging
import sys

# Create a logger
logger = logging.getLogger(__name__)  # __name__ ensures log messages are specific to the module
logger.setLevel(logging.DEBUG)  # Set the minimum level of messages to log (DEBUG is most verbose)

# Create a handler that outputs to the console
console_handler = logging.StreamHandler(sys.stdout)  # Use sys.stdout for proper Streamlit handling
console_handler.setLevel(logging.DEBUG)  # Set level for console output

# Create a formatter to customize the log message format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Example usage (in other modules):
# from logging_config import logger
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
