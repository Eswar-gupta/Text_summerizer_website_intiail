import sys
import os

# Add the src directory to the Python path
#sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from textSummarizer.logging.logging import logger

logger.info("This is the custom log of this project")